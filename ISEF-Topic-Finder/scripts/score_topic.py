#!/usr/bin/env python3
"""
score_topic.py — rubric calculator for ISEF topic-stage prediction.

Hybrid architecture: heuristics for measurable signals (T1.1.c, T2.1 substrate
detection, M1/M3/M4 from evidence pack), accepts LLM-supplied overrides for
judgment-required dimensions (T1.1.a/b, T1.2, T1.3, T2.2, T2.3). Calling flow
(Claude) computes those after reading the evidence pack and passes them in.

CLI:
    python score_topic.py \\
        --topic "MCMC sampling of origami and linkages" \\
        --category PHYS \\
        --evidence /path/to/evidence.json \\
        --scores /path/to/judgment_scores.json

Output: scorecard JSON per references/rubric-topic-stage-extensions.md §5.

Determinism (A6): given identical evidence + scores inputs, output is
bit-identical. No randomness; no temperature; no Claude calls from inside
this script.
"""
import argparse
import json
import re
import sys
from pathlib import Path
from typing import Optional


RUBRIC_VERSION = "2026.1"

# Per-category multipliers (§4 of rubric extensions).
# multipliers apply to TIER SUBSCORES ONLY (not modulators).
CATEGORY_MULTIPLIERS = {
    "PHYS": 1.10, "MATH": 1.10,
    "BMED": 1.05, "CELL": 1.05,
    "ROBO": 1.05, "EBED": 1.05,
    "EGSD": 1.05, "ENEV": 1.05,
}

# Substrate keyword patterns (for T2.1 compliance bias rule).
SUBSTRATE_PATTERNS = {
    "human": [
        r"\bhuman\b", r"\bpatient", r"\bparticipant", r"\bsurvey",
        r"\bquestionnaire", r"\bclinical\b", r"\binterview\b",
        r"\badolescent", r"\bteen", r"\bminor\b", r"\bchild",
        r"\bIRB\b", r"\binformed consent",
    ],
    "animal": [
        r"\bvertebrate", r"\bmamm(al|alian)\b", r"\bmouse\b|\bmice\b",
        r"\brat\b|\brats\b", r"\brabbit", r"\bdog\b|\bdogs\b",
        r"\bcat\b|\bcats\b", r"\bfish\b", r"\bbird", r"\banimal model",
        r"\bzebrafish",
    ],
    "tissue": [
        r"\btissue\b", r"\bblood\b", r"\bcell line", r"\bprimary cell",
        r"\brDNA\b", r"\bplasmid", r"\borgan(oid|elle)",
    ],
    "pathogen": [
        r"\bpathogen", r"\bbacteri(a|um)\b", r"\bvirus\b|\bviral\b",
        r"\bmicroorganism", r"\bMRSA\b", r"\bE\.?\s?coli\b",
        r"\bBSL-?[12]\b", r"\bantibiotic", r"\bantimicrobial",
    ],
    "hazardous": [
        r"\bhazardous\b", r"\bDEA\b", r"\bcontrolled substance",
        r"\bcarcinogen", r"\bradioactive", r"\bexplosive", r"\btoxic",
    ],
    "field": [
        r"\bfield (work|study|sampling|deployment)",
        r"\bsoil\b", r"\bwater (sampling|quality)",
    ],
}


def detect_substrate_clusters(topic: str, hypothesis: str = "") -> dict:
    """Return which substrate clusters the topic mentions, for compliance bias."""
    text = (topic + " " + (hypothesis or "")).lower()
    triggered = {}
    for cluster, patterns in SUBSTRATE_PATTERNS.items():
        matches = []
        for pat in patterns:
            if re.search(pat, text, flags=re.IGNORECASE):
                matches.append(pat)
        if matches:
            triggered[cluster] = matches
    return triggered


def compute_T1_1_c(evidence: dict) -> tuple[int, str]:
    """Anti-saturation sub-score from OpenAlex category-normalized percentile.

    Returns (score 0-10, rationale)."""
    openalex = evidence.get("openalex") or {}
    pct = openalex.get("category_normalized_percentile")
    if pct is None:
        return 5, "OpenAlex unavailable; defaulting to mid-score"
    if 30 <= pct <= 70:
        return 10, f"sweet spot ({pct}th pct within category)"
    if (10 <= pct < 30) or (70 < pct <= 90):
        return 6, f"near sweet spot ({pct}th pct)"
    if pct > 90:
        return 2, f"saturated ({pct}th pct in category — many active groups)"
    return 2, f"vapor ({pct}th pct — few or no papers)"


def compute_M1(evidence: dict) -> tuple[int, str]:
    """Trend velocity modulator (±5)."""
    openalex = evidence.get("openalex") or {}
    pct = openalex.get("category_normalized_percentile")
    slope = openalex.get("trend_slope")  # papers/year delta, signed
    if pct is None:
        return 0, "OpenAlex unavailable; M1 omitted"
    if 30 <= pct <= 70 and slope and slope > 0:
        return 5, f"rising, {pct}th pct — active but not saturated"
    if 30 <= pct <= 70:
        return 3, f"{pct}th pct, flat slope"
    if (10 <= pct < 30) or (70 < pct <= 90):
        return 2, f"{pct}th pct, slope={slope}"
    if pct > 90:
        return -5, f"saturated ({pct}th pct)"
    if pct < 5:
        m3 = evidence.get("biorxiv", {}).get("preprints_last_6mo", []) + evidence.get("arxiv", {}).get("papers_last_6mo", [])
        if len(m3) == 0:
            return -5, f"genuine vapor: {pct}th pct + no preprints"
        return -3, f"low velocity ({pct}th pct) but recent preprints exist"
    return 0, "M1 thresholds did not match"


def compute_M3(evidence: dict) -> tuple[int, str]:
    """Preprint freshness modulator (±3)."""
    biorxiv = evidence.get("biorxiv", {}).get("preprints_last_6mo", [])
    arxiv = evidence.get("arxiv", {}).get("papers_last_6mo", [])
    total = len(biorxiv) + len(arxiv)
    if total >= 3:
        return 3, f"{total} preprints in last 6mo (active field)"
    if total >= 1:
        return 1, f"{total} preprint in last 6mo"
    if biorxiv == [] and arxiv == [] and "biorxiv" not in evidence and "arxiv" not in evidence:
        return 0, "preprint sources unavailable; M3 omitted"
    return -1, "no preprints in last 6mo"


def compute_M2(evidence: dict) -> tuple[int, str]:
    """Accessibility signal modulator (±3). Repurposed from press/funding."""
    perplexity = evidence.get("perplexity", {})
    if perplexity.get("status") == "stub" or perplexity.get("status") == "unavailable":
        return 0, "Perplexity unavailable; M2 omitted"
    hs_precedent = perplexity.get("hs_precedent_found", False)
    industry_only = perplexity.get("industry_only", False)
    if hs_precedent:
        return 3, "high-school precedent found (open-source kits or prior HS projects)"
    if industry_only:
        return -2, "topic appears only in industry/PI-lab contexts; not accessible to HS"
    return 0, "Perplexity returned no clear signal"


def compute_M4(evidence: dict) -> tuple[int, str, str]:
    """Inverted M4: penalty for cargo-cult, bonus for cross-category import.

    Returns (value, arm_label, rationale)."""
    archive = evidence.get("isef_archive", {})
    if archive.get("status") != "ok":
        return 0, "no_signal", f"ISEF archive unavailable (status={archive.get('status')})"
    return (
        archive.get("m4_value", 0),
        archive.get("m4_arm", "no_signal"),
        archive.get("m4_arm_rationale") or f"computed by search_isef_archive: {archive.get('m4_arm')}",
    )


def apply_anti_clamp(t1_1: int, t1_3: int) -> tuple[int, bool]:
    """If T1.1 ≥ 25, T1.3 floor is 10/15."""
    if t1_1 >= 25 and t1_3 < 10:
        return 10, True
    return t1_3, False


def apply_compliance_bias(t2_1: int, substrate_clusters: dict) -> tuple[int, bool]:
    """Cap T2.1 ≤ 7 if any human/animal/tissue/pathogen/hazardous mention."""
    risky = {"human", "animal", "tissue", "pathogen", "hazardous"}
    if substrate_clusters and any(c in risky for c in substrate_clusters):
        return min(t2_1, 7), True
    return t2_1, False


def confidence_from_sources(missing_sources: list[str]) -> tuple[str, int]:
    """Returns (confidence, half-width-of-range)."""
    n_missing = len(missing_sources)
    if n_missing == 0:
        return "high", 3
    if n_missing <= 2:
        return "medium", 6
    return "low", 13


def score_topic(
    topic: str,
    category: str,
    evidence: dict,
    judgment_scores: dict,
    hypothesis: str = "",
) -> dict:
    """Compute the scorecard.

    judgment_scores must contain LLM-provided per-dimension scores for:
      T1_1_a_reframing (0-10), T1_1_b_crossdisc (0-10),
      T1_2_ownership (0-15), T1_3_legibility (0-15),
      T2_2_curriculum (0-10), T2_3_learncurve (0-10),
      T2_1_feasibility_base (0-10)  -- before compliance cap

    Each dimension also has a rationale string the LLM provided.
    """
    warnings = []
    js = judgment_scores

    # Validate inputs (be strict — don't silently default).
    required_judgments = [
        "T1_1_a_reframing", "T1_1_b_crossdisc",
        "T1_2_ownership", "T1_3_legibility",
        "T2_1_feasibility_base", "T2_2_curriculum", "T2_3_learncurve",
    ]
    for k in required_judgments:
        if k not in js:
            warnings.append(f"missing required judgment score: {k} (defaulted to 0)")
            js[k] = {"score": 0, "rationale": "missing"}

    # Heuristic sub-scores
    t1_1_c, t1_1_c_rationale = compute_T1_1_c(evidence)
    t1_1 = js["T1_1_a_reframing"]["score"] + js["T1_1_b_crossdisc"]["score"] + t1_1_c

    t1_2 = js["T1_2_ownership"]["score"]
    t1_3_raw = js["T1_3_legibility"]["score"]
    t1_3, anticlamp_applied = apply_anti_clamp(t1_1, t1_3_raw)

    # Compliance bias on T2.1
    substrate = detect_substrate_clusters(topic, hypothesis)
    t2_1_base = js["T2_1_feasibility_base"]["score"]
    t2_1, compliance_cap_applied = apply_compliance_bias(t2_1_base, substrate)
    t2_2 = js["T2_2_curriculum"]["score"]
    t2_3 = js["T2_3_learncurve"]["score"]
    off_ramp_triggered = t2_3 < 5

    # Modulators
    m1, m1_rat = compute_M1(evidence)
    m2, m2_rat = compute_M2(evidence)
    m3, m3_rat = compute_M3(evidence)
    m4, m4_arm, m4_rat = compute_M4(evidence)

    # Math composition
    tier_subscore = t1_1 + t1_2 + t1_3 + t2_1 + t2_2 + t2_3
    cat_mult = CATEGORY_MULTIPLIERS.get(category, 1.0)
    adjusted = tier_subscore * cat_mult
    modded = adjusted + m1 + m2 + m3 + m4
    final_point = max(0, min(100, round(modded * 100 / 106)))

    # Confidence + range
    missing_sources = [
        s for s in ["openalex", "pubmed", "biorxiv", "arxiv", "perplexity", "isef_archive"]
        if not evidence.get(s) or evidence.get(s, {}).get("status") in (None, "stub", "unavailable", "empty")
    ]
    confidence, half_width = confidence_from_sources(missing_sources)
    final_range = [max(0, final_point - half_width), min(100, final_point + half_width)]

    # Tier label suppressed until Phase 1.5 back-testing
    tier_label = "[SUPPRESSED — pending Phase 1.5 back-test validation]"

    scorecard = {
        "rubric_version": RUBRIC_VERSION,
        "topic": topic,
        "inferred_category": category,
        "tiers": {
            "T1_1_creativity": {
                "score": t1_1, "max": 30,
                "sub": {
                    "reframing": js["T1_1_a_reframing"]["score"],
                    "crossdisc": js["T1_1_b_crossdisc"]["score"],
                    "antisat": t1_1_c,
                },
                "rationale": (
                    f"reframing: {js['T1_1_a_reframing'].get('rationale','')}; "
                    f"crossdisc: {js['T1_1_b_crossdisc'].get('rationale','')}; "
                    f"antisat: {t1_1_c_rationale}"
                ),
            },
            "T1_2_ownership": {"score": t1_2, "max": 15, "rationale": js["T1_2_ownership"].get("rationale", "")},
            "T1_3_legibility": {
                "score": t1_3, "max": 15,
                "rationale": js["T1_3_legibility"].get("rationale", ""),
                "anticlamp_applied": anticlamp_applied,
                "raw_score_before_anticlamp": t1_3_raw if anticlamp_applied else None,
            },
            "T2_1_feasibility": {
                "score": t2_1, "max": 10,
                "rationale": js["T2_1_feasibility_base"].get("rationale", ""),
                "compliance_cap_applied": compliance_cap_applied,
                "substrate_clusters_detected": list(substrate.keys()),
                "base_before_cap": t2_1_base if compliance_cap_applied else None,
            },
            "T2_2_curriculum": {"score": t2_2, "max": 10, "rationale": js["T2_2_curriculum"].get("rationale", "")},
            "T2_3_learncurve": {
                "score": t2_3, "max": 10,
                "rationale": js["T2_3_learncurve"].get("rationale", ""),
                "off_ramp_triggered": off_ramp_triggered,
            },
        },
        "category_multiplier": cat_mult,
        "multiplier_scope": "tier_subscores_only",
        "modulators": {
            "M1_trend_velocity": {"value": m1, "evidence": m1_rat},
            "M2_accessibility": {"value": m2, "evidence": m2_rat},
            "M3_preprint_freshness": {"value": m3, "evidence": m3_rat},
            "M4_prior_alignment": {"value": m4, "arm": m4_arm, "evidence": m4_rat},
        },
        "composite": {
            "tier_subscore": tier_subscore,
            "adjusted": round(adjusted, 2),
            "modded": round(modded, 2),
            "final_point": final_point,
            "final_range": final_range,
            "confidence": confidence,
            "tier_label": tier_label,
            "missing_sources": missing_sources,
        },
        "compliance_flags": list(substrate.keys()),
        "anchor_citations": _extract_anchor_citations(evidence),
        "warnings": warnings,
    }
    return scorecard


def _extract_anchor_citations(evidence: dict) -> list[dict]:
    """Pull the top-N anchor citations from evidence, preferring OpenAlex."""
    out = []
    for src in ("openalex", "pubmed", "biorxiv", "arxiv"):
        papers = (evidence.get(src) or {}).get("top_papers", []) or (evidence.get(src) or {}).get("papers", [])
        for p in papers[:3]:
            out.append({
                "title": p.get("title", "")[:200],
                "year": p.get("year"),
                "source": src,
                "id": p.get("id") or p.get("doi") or p.get("pmid") or "",
                "why_it_matters": p.get("why_it_matters", ""),
            })
        if out:
            break
    return out[:5]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--topic", required=True)
    parser.add_argument("--category", required=True)
    parser.add_argument("--evidence", required=True, help="Path to evidence pack JSON")
    parser.add_argument("--scores", required=True, help="Path to LLM-judgment scores JSON")
    parser.add_argument("--hypothesis", default="", help="Student's falsifiable hypothesis (for substrate detection)")
    args = parser.parse_args()

    evidence = json.loads(Path(args.evidence).read_text())
    scores = json.loads(Path(args.scores).read_text())

    scorecard = score_topic(args.topic, args.category, evidence, scores, args.hypothesis)
    json.dump(scorecard, sys.stdout, indent=2)
    return 0


if __name__ == "__main__":
    sys.exit(main())
