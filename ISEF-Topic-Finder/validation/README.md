# Rubric back-testing — Phase 1.5

**Currently empty.** Phase 1.5 deliverable; gates the release of tier labels.

## Purpose

Verify that the rubric (`../references/rubric-topic-stage-extensions.md`) actually separates ISEF winners from non-placers at chance + AUC ≥ 0.70. Without this validation, tier labels in the scorecard are SUPPRESSED and the skill ships qualitative-only.

## Procedure (to be executed in Phase 1.5)

1. **Build `backtest-cohort.jsonl`** — ≥30 past top-3 winners + ≥30 known non-placers from ISEF-Scrape + Chinese guide ch. 7's top-312 keyword analysis. Cover PHYS, BMED, ROBO, CELL, MATH at minimum. Schema per line: `{"id": ..., "category": ..., "year": ..., "title": ..., "abstract": ..., "outcome": "top3"|"finalist_no_top10", "evidence_source": "ISEF-Scrape"|"Chinese-guide"}`
2. **Run `backtest-runner.py`** — applies `../scripts/score_topic.py` to each entry using a pre-built cached evidence pack. Computes ROC curve and AUC overall + per-category.
3. **Produce `backtest-report.md`** — embed the ROC plot PNG, per-category AUC table, per-tier ablation (does T1.1 alone separate? T1.1+T1.2? full composite?).
4. **Gate decision:**
   - AUC ≥ 0.70 overall → enable tier labels with thresholds from Youden's J
   - 0.65 ≤ AUC < 0.70 in 2+ categories → enable tier labels per-category only
   - AUC < 0.65 → ship qualitative-only; tag rubric for redesign in v2

## Files (when populated)

- `backtest-cohort.jsonl` — ≥60 labeled topics
- `backtest-runner.py` — scorer + ROC computation
- `backtest-report.md` — human-readable report with embedded plots

## Re-run cadence

- After every major rubric change (re-run before shipping)
- Annual recalibration tickler (start of each ISEF cycle, ~September)
