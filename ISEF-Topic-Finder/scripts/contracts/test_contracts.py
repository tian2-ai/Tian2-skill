#!/usr/bin/env python3
"""Contract tests for external dependencies.

Run with:  python3 -m unittest scripts/contracts/test_contracts.py -v

Each test loads a saved API response (fixture) and asserts that the
parser in search_*.py extracts expected fields. Fixtures are captured
from real API calls during Phase 4 build. When an API's schema drifts,
the corresponding test fails — that's the signal to update the parser.

Refresh fixtures with:
  curl ... > fixtures/<source>_<query>.{json,xml}
"""
import json
import sys
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

# Allow importing search_* modules
HERE = Path(__file__).parent.parent
sys.path.insert(0, str(HERE))

FIXTURES = Path(__file__).parent / "fixtures"


class OpenAlexContract(unittest.TestCase):
    """OpenAlex /works endpoint shape."""
    def test_velocity_group_by_shape(self):
        data = json.loads((FIXTURES / "openalex_velocity.json").read_text())
        self.assertIn("group_by", data, "OpenAlex must return a group_by array when group_by=publication_year")
        if data["group_by"]:
            item = data["group_by"][0]
            self.assertIn("key", item, "Each group_by item must have a 'key' (the year)")
            self.assertIn("count", item, "Each group_by item must have a 'count'")

    def test_search_returns_results_or_empty(self):
        data = json.loads((FIXTURES / "openalex_velocity.json").read_text())
        # When group_by is used, OpenAlex returns 'results' (may be empty) plus 'meta'
        self.assertIn("meta", data, "OpenAlex response must include meta")


class ArxivContract(unittest.TestCase):
    """arXiv /api/query endpoint shape — Atom XML."""
    NS = "{http://www.w3.org/2005/Atom}"

    def test_atom_root(self):
        root = ET.fromstring((FIXTURES / "arxiv_search.xml").read_bytes())
        self.assertTrue(root.tag.endswith("feed"), "arXiv response must be an Atom feed root")

    def test_entry_required_fields(self):
        root = ET.fromstring((FIXTURES / "arxiv_search.xml").read_bytes())
        entries = root.findall(f"{self.NS}entry")
        if not entries:
            self.skipTest("Fixture has zero entries; can't assert per-entry shape")
        e = entries[0]
        for field in ("title", "id", "published"):
            self.assertIsNotNone(
                e.findtext(f"{self.NS}{field}"),
                f"arXiv entry must have <{field}>",
            )


class ScoreTopicSchemaContract(unittest.TestCase):
    """score_topic.py output schema must remain stable (it's the contract with SKILL.md)."""
    def test_output_has_required_top_level_keys(self):
        import score_topic
        evidence = {
            "openalex": {"status": "ok", "category_normalized_percentile": 50, "trend_slope": 0.1, "top_papers": []},
            "arxiv": {"status": "ok", "papers_last_6mo": []},
            "isef_archive": {"status": "ok", "m4_value": 0, "m4_arm": "no_signal"},
        }
        scores = {
            "T1_1_a_reframing": {"score": 5, "rationale": ""},
            "T1_1_b_crossdisc": {"score": 5, "rationale": ""},
            "T1_2_ownership": {"score": 8, "rationale": ""},
            "T1_3_legibility": {"score": 9, "rationale": ""},
            "T2_1_feasibility_base": {"score": 7, "rationale": ""},
            "T2_2_curriculum": {"score": 7, "rationale": ""},
            "T2_3_learncurve": {"score": 7, "rationale": ""},
        }
        sc = score_topic.score_topic("test", "PHYS", evidence, scores)
        for k in ("rubric_version", "topic", "inferred_category", "tiers",
                  "category_multiplier", "modulators", "composite",
                  "compliance_flags", "anchor_citations", "warnings"):
            self.assertIn(k, sc, f"scorecard must contain top-level key '{k}'")
        # composite fields
        for k in ("tier_subscore", "adjusted", "modded", "final_point",
                  "final_range", "confidence", "tier_label", "missing_sources"):
            self.assertIn(k, sc["composite"], f"composite must contain '{k}'")

    def test_anti_clamp_fires_when_t1_1_high(self):
        import score_topic
        evidence = {"isef_archive": {"status": "ok", "m4_value": 0, "m4_arm": "no_signal"}}
        scores = {
            "T1_1_a_reframing": {"score": 10, "rationale": ""},
            "T1_1_b_crossdisc": {"score": 10, "rationale": ""},
            "T1_2_ownership": {"score": 10, "rationale": ""},
            "T1_3_legibility": {"score": 5, "rationale": ""},  # below floor
            "T2_1_feasibility_base": {"score": 7, "rationale": ""},
            "T2_2_curriculum": {"score": 7, "rationale": ""},
            "T2_3_learncurve": {"score": 7, "rationale": ""},
        }
        sc = score_topic.score_topic("t", "PHYS", evidence, scores)
        # T1.1 = 10+10+~5 (heuristic default since no openalex) = 25; floor should engage
        # If T1.1 >= 25, T1.3 floor = 10
        if sc["tiers"]["T1_1_creativity"]["score"] >= 25:
            self.assertGreaterEqual(sc["tiers"]["T1_3_legibility"]["score"], 10,
                                    "Anti-clamp must lift T1.3 to floor when T1.1 >= 25")
            self.assertTrue(sc["tiers"]["T1_3_legibility"]["anticlamp_applied"])

    def test_compliance_cap_fires_on_human_substrate(self):
        import score_topic
        evidence = {"isef_archive": {"status": "ok", "m4_value": 0, "m4_arm": "no_signal"}}
        scores = {
            "T1_1_a_reframing": {"score": 5, "rationale": ""},
            "T1_1_b_crossdisc": {"score": 5, "rationale": ""},
            "T1_2_ownership": {"score": 10, "rationale": ""},
            "T1_3_legibility": {"score": 10, "rationale": ""},
            "T2_1_feasibility_base": {"score": 10, "rationale": ""},  # would be 10 without cap
            "T2_2_curriculum": {"score": 7, "rationale": ""},
            "T2_3_learncurve": {"score": 7, "rationale": ""},
        }
        sc = score_topic.score_topic("Survey of human patients on anxiety", "BEHA", evidence, scores)
        self.assertLessEqual(sc["tiers"]["T2_1_feasibility"]["score"], 7,
                             "Compliance bias must cap T2.1 <= 7 on human-substrate topics")
        self.assertTrue(sc["tiers"]["T2_1_feasibility"]["compliance_cap_applied"])
        self.assertIn("human", sc["compliance_flags"])

    def test_off_ramp_triggers_when_t2_3_low(self):
        import score_topic
        evidence = {"isef_archive": {"status": "ok", "m4_value": 0, "m4_arm": "no_signal"}}
        scores = {
            "T1_1_a_reframing": {"score": 5, "rationale": ""},
            "T1_1_b_crossdisc": {"score": 5, "rationale": ""},
            "T1_2_ownership": {"score": 10, "rationale": ""},
            "T1_3_legibility": {"score": 10, "rationale": ""},
            "T2_1_feasibility_base": {"score": 7, "rationale": ""},
            "T2_2_curriculum": {"score": 7, "rationale": ""},
            "T2_3_learncurve": {"score": 3, "rationale": ""},  # below 5
        }
        sc = score_topic.score_topic("t", "PHYS", evidence, scores)
        self.assertTrue(sc["tiers"]["T2_3_learncurve"]["off_ramp_triggered"])

    def test_score_as_range_widens_when_sources_missing(self):
        import score_topic
        evidence_few = {"openalex": {"status": "unavailable"}, "isef_archive": {"status": "ok", "m4_value": 0, "m4_arm": "no_signal"}}
        evidence_all = {
            "openalex": {"status": "ok", "category_normalized_percentile": 50, "trend_slope": 0.1, "top_papers": []},
            "pubmed": {"status": "ok", "papers": []},
            "arxiv": {"status": "ok", "papers_last_6mo": []},
            "biorxiv": {"status": "ok", "preprints_last_6mo": []},
            "perplexity": {"status": "ok", "hs_precedent_found": False},
            "isef_archive": {"status": "ok", "m4_value": 0, "m4_arm": "no_signal"},
        }
        baseline_scores = {
            "T1_1_a_reframing": {"score": 5, "rationale": ""},
            "T1_1_b_crossdisc": {"score": 5, "rationale": ""},
            "T1_2_ownership": {"score": 10, "rationale": ""},
            "T1_3_legibility": {"score": 10, "rationale": ""},
            "T2_1_feasibility_base": {"score": 7, "rationale": ""},
            "T2_2_curriculum": {"score": 7, "rationale": ""},
            "T2_3_learncurve": {"score": 7, "rationale": ""},
        }
        sc_few = score_topic.score_topic("t", "PHYS", evidence_few, baseline_scores)
        sc_all = score_topic.score_topic("t", "PHYS", evidence_all, baseline_scores)
        width_few = sc_few["composite"]["final_range"][1] - sc_few["composite"]["final_range"][0]
        width_all = sc_all["composite"]["final_range"][1] - sc_all["composite"]["final_range"][0]
        self.assertGreater(width_few, width_all, "Range should widen when sources are missing")

    def test_tier_label_suppressed_until_backtest(self):
        import score_topic
        evidence = {"openalex": {"status": "ok", "category_normalized_percentile": 50, "trend_slope": 0.1, "top_papers": []}}
        scores = {k: {"score": 10, "rationale": ""} for k in
                  ["T1_1_a_reframing", "T1_1_b_crossdisc", "T1_2_ownership",
                   "T1_3_legibility", "T2_1_feasibility_base", "T2_2_curriculum", "T2_3_learncurve"]}
        sc = score_topic.score_topic("t", "PHYS", evidence, scores)
        self.assertIn("SUPPRESSED", sc["composite"]["tier_label"],
                      "Tier label must remain SUPPRESSED until Phase 1.5 back-test validates")


class IsefArchiveContract(unittest.TestCase):
    """ISEF archive search must be able to load the corpus."""
    def test_corpus_resolves(self):
        import search_isef_archive
        root = search_isef_archive.resolve_isef_scrape_root()
        # Either it resolves to a real path, or the test environment doesn't have it
        if root is None:
            self.skipTest("ISEF_SCRAPE_ROOT not set in test environment")
        self.assertTrue(Path(root).is_dir())

    def test_m4_arm_values_are_known(self):
        import search_isef_archive
        result = search_isef_archive.search("nonsense topic gibberish xyz", "PHYS")
        if result.get("status") != "ok":
            self.skipTest(f"archive search did not return ok: {result.get('status')}")
        self.assertIn(result["m4_arm"], {
            "no_signal", "cargo_cult_penalty", "cross_category_bonus",
            "no_signal_sparse_coverage",
        })


if __name__ == "__main__":
    unittest.main(verbosity=2)
