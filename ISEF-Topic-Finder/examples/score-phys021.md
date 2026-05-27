# Example: `/isef-topic-finder score "MCMC sampling of origami and linkages"`

**Purpose:** Calibration anchor. PHYS021 was a 2026 ISEF PHYS grand-award contender; the rubric should not penalize it.

This example shows the per-dimension transparency required by §4.5 of `references/rubric-topic-stage-extensions.md`. Re-run after rubric changes to verify calibration drift.

## Input

```
Topic:     MCMC sampling of origami and linkages
Category:  PHYS
Lang:      both
Depth:     medium
Hypothesis: If origami crease patterns sample uniformly across configurations,
            the statistical-mechanics analogy is wrong.
```

## How the score was computed

### Step 1 — Evidence fan-out (`cross_validate.py`)

Real APIs queried 2026-05-26. ~1s parallel fan-out.

| Source | Status | Key fields |
|---|---|---|
| OpenAlex | ok | papers/year = 5 avg; percentile = 17 (sweet spot); trend slope = +0.32 |
| arXiv | ok | 0 hits for "MCMC AND sampling AND origami" — genuinely novel framing |
| PubMed | not routed (PHYS category) | n/a |
| bioRxiv | not routed (PHYS category) | n/a |
| Perplexity | unavailable (skill-wrap) | M2 omitted |
| ISEF archive | ok | with `--exclude-slug` phys021: no in-category structural twin → M4 = 0 |

### Step 2 — LLM-judgment scores (provided by the calling flow)

```json
{
  "T1_1_a_reframing":   {"score": 9,  "rationale": "Recasts mechanism configuration space as a stat-mech ensemble"},
  "T1_1_b_crossdisc":   {"score": 10, "rationale": "Origami (engineering) + statistical mechanics (PHYS) bridge"},
  "T1_2_ownership":     {"score": 14, "rationale": "Pure computational; reproduces known foldability before extending"},
  "T1_3_legibility":    {"score": 12, "rationale": "Pitch works for PHYS/MATH judges; slight priming for BMED"},
  "T2_1_feasibility_base": {"score": 9, "rationale": "Pencil + Python + MCMC; no IRB/IACUC; <$50"},
  "T2_2_curriculum":    {"score": 8,  "rationale": "AP Physics C (DoF) + AP Stats (sampling)"},
  "T2_3_learncurve":    {"score": 8,  "rationale": "Week-1: Metropolis sampler on 2-fold linkage"}
}
```

### Step 3 — Heuristic sub-scores

| Sub-check | Computed | Source |
|---|---|---|
| T1.1.c anti-saturation | 6 | OpenAlex pct=17 → "10 ≤ pct < 30" range → 6/10 |
| Substrate detection | none | No human/animal/tissue/pathogen/hazardous keywords |

### Step 4 — Rule application

- **Anti-clamp** (T1.1 ≥ 25 → T1.3 floor = 10): not triggered (T1.3 = 12 already above floor)
- **Compliance bias**: not triggered (no risky substrates detected)
- **Off-ramp** (T2.3 < 5): not triggered (T2.3 = 8)

### Step 5 — Tier subscore + multiplier

```
T1.1 = 9 + 10 + 6   = 25 /30
T1.2 =                14 /15
T1.3 =                12 /15
T2.1 =                9  /10
T2.2 =                8  /10
T2.3 =                8  /10
tier_subscore       = 76 /90

PHYS multiplier × 1.10:
adjusted = 76 × 1.10 = 83.6
```

### Step 6 — Modulators

| Mod | Value | Rationale |
|---|---|---|
| M1 trend velocity | **+2** | 17th pct, slope +0.32 → "near sweet spot" |
| M2 accessibility | 0 | Perplexity unavailable; M2 omitted |
| M3 preprint freshness | −1 | 0 preprints in last 6mo on this exact framing |
| M4 prior alignment | 0 | Self-excluded; no in-category twin within sim ≥ 0.6 |
| **Sum** | **+1** | |

```
modded = 83.6 + 1 = 84.6
final  = round(84.6 × 100 / 106) = round(79.8) = 80
```

### Step 7 — Range + confidence

3 of 6 sources reachable (OpenAlex, arXiv, ISEF archive); pubmed/biorxiv/perplexity missing → **confidence: low, half-width: 13** per `references/rubric-topic-stage-extensions.md` §4.2.

```
range = [80 − 13, 80 + 13] = [67, 93]
```

## Final output

```
Score: 67–93 / 100  (range = ±13)
Confidence: low  (missing: pubmed, biorxiv, perplexity)
Tier label: [SUPPRESSED — pending Phase 1.5 back-test validation]
Rubric version: 2026.1
```

## What this calibration confirms

- **Creativity dimension dominates as designed.** T1.1 = 25/30 reflects the genuine reframing.
- **PHYS multiplier amplifies correctly** without double-counting modulators (multiplier_scope = `tier_subscores_only`).
- **M4 self-exclusion behaves correctly** when `--exclude-slug` is passed.
- **Score-as-range honestly communicates uncertainty.** With richer evidence the range tightens; with sparse evidence the range widens.

## Why the score range overlaps the anti-pattern

The lower bound (67) is above the anti-pattern's upper bound (47), but only by 20 points. If we had Perplexity online + a richer PubMed/bioRxiv contribution, M2 would land at +3 (HS precedent for MCMC kits) and M3 would land at +2 (adjacent preprints), tightening the range and raising the final to ~85.

This is the intended honesty: a great topic can still land in a wide range if the evidence layer is thin. The skill refuses to overclaim.
