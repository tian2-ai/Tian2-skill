# Phase 1.5 — Calibration report (v0)

**Date:** 2026-05-26
**Rubric version:** 2026.1
**Status:** PARTIAL — tier labels remain SUPPRESSED

## Honest summary

The plan calls for back-testing the rubric against ≥30 known winners + ≥30 known non-placers with AUC ≥ 0.70 as the gate for releasing tier labels. **We cannot complete that back-test today** because the ISEF-Scrape archive provides project titles, categories, and years but **no award outcomes** (no top-3 / honorable mention / finalist-no-placement labels). Without outcome labels, ROC/AUC is undefined.

This document records what we DID validate as a v0 calibration:

1. PHYS021 (real 2026 PHYS grand-award contender) scored against real evidence
2. Anti-pattern "ResNet on Kaggle chest X-rays" scored against synthesized adversarial evidence
3. Behavioral rule validation via the contract test suite (12 tests pass)

Tier labels stay SUPPRESSED until a labeled cohort exists. Score output is range-with-confidence-band only.

## What was tested (v0 anchors)

### Anchor 1 — PHYS021 (`examples/score-phys021.md`)

End-to-end run: `cross_validate.py` against real APIs + `score_topic.py` with PHYS-specific judgments.

| Configuration | Final | Range | Confidence | Sources |
|---|---|---|---|---|
| Hand-crafted fixture evidence (rich) | 86 | 83–89 | high | all 5 + archive |
| Real APIs (PHYS021 not excluded from archive — self-match) | 75 | 62–88 | low | OpenAlex + arXiv + archive only |
| Real APIs + `--exclude-slug phys021-mcmc-sampling-of-origami-and-linkages` | 80 | 67–93 | low | same, no self-penalty |

**Interpretation:** when external evidence sources are sparse on a genuinely novel topic (arXiv 0 hits, no preprints, Perplexity unavailable), the confidence band widens to "low" and the score range becomes broad. This is correct — the rubric communicates uncertainty rather than overclaiming.

### Anchor 2 — Anti-pattern (`examples/score-saturated-topic.md`)

"Trained ResNet to classify chest X-rays for pneumonia on Kaggle dataset" with synthesized adversarial evidence:

| Final | Range | Reason |
|---|---|---|
| 44 | 41–47 | T1.1 = 7/30 (low reframing); M1 = −5 (saturated); M4 = −5 (cargo-cult) |

**Differential:** PHYS021 (86) − ResNet (44) = **42-point spread**. The creativity dimension alone accounts for 21 points; the modulators amplify the gap.

### Anchor 3 — Compliance bias + off-ramp behaviors

| Topic | Trigger | Verified behavior |
|---|---|---|
| "Survey on social media use and teen anxiety" | substrate=`human` detected | T2.1 capped 9 → 7; flags `['human']` |
| Topic with T2.3=3 | `off_ramp_triggered=True` | Calling flow redirects to `readiness-off-ramp.md` |

## Why the full back-test isn't possible today

The ISEF-Scrape `output/projects-<year>-full/project-inventory.json` files contain title + category + year + URL only. The award annotations live on the per-project ProjectBoard pages, which the scraper hasn't extracted at scale yet.

Workable paths to get a real labeled cohort (any of these unblocks Phase 1.5 v1):

1. **Re-run ISEF-Scrape** with the per-project page parser that captures the "Awards" section (largest effort; most accurate)
2. **Mine the Chinese guide's top-312 list** (`ISEF-Scrape/ISEF竞赛完全指南-完整版.md` ch. 7) for confirmed 2025 grand-award winners — ~312 labeled winners + we'd need to randomly sample non-placers from same categories/years
3. **Hand-label** 30 winners from publicly-known ISEF grand-award lists (Society for Science press releases) + 30 random non-placers from the inventories

Until labels exist, tier-label thresholds cannot be derived from the data; they would be made up. The plan is explicit: **don't ship tier labels until back-testing validates them.**

## What's locked in regardless of back-test

These don't require labels to validate:

- The 4 behavioral rules (anti-clamp, compliance bias, off-ramp, inverted M4) — verified via contract tests
- The rubric arithmetic — `clamp(round(modded × 100 / 106), 0, 100)` — verified by computing PHYS021 by hand and matching
- The substrate detection — verified to catch human/animal/tissue/pathogen/hazardous mentions
- The score-as-range output — verified to widen with missing sources

## Cadence

- **Annual recalibration tickler:** re-run this validation at start of each ISEF cycle (~September). When the rubric is updated, bump `rubric_version` in `SKILL.md` frontmatter and re-publish.
- **Trigger for v1 of this report:** acquisition of any labeled cohort (≥30 winners + ≥30 non-placers).

## Files referenced

- `examples/score-phys021.md` — per-dimension transparency for the PHYS021 calibration
- `examples/score-saturated-topic.md` — anti-pattern run
- `scripts/contracts/test_contracts.py` — 12 behavioral assertions
- `references/rubric-topic-stage-extensions.md` — rubric source of truth
