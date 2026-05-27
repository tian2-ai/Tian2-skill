# Example: `/isef-topic-finder score "trained ResNet to classify chest X-rays for pneumonia on Kaggle dataset"`

**Purpose:** Anti-pattern anchor. Saturated CS application of a known method to a public dataset. The rubric should land it well below the competition-finalist tier.

## Input

```
Topic:     trained ResNet to classify chest X-rays for pneumonia on Kaggle dataset
Category:  SFTD
Lang:      both
Depth:     medium
Hypothesis: If a ResNet-50 fine-tuned on the NIH ChestX-ray14 dataset performs
            below AUC 0.85 on the held-out test split, my model has not learned
            useful features.
```

(The hypothesis passes the gate — it's falsifiable. Hypothesis pass doesn't mean the topic is good; only that we can score it.)

## Evidence layer

| Source | Status | Key fields |
|---|---|---|
| OpenAlex | ok | percentile=96 (saturated); thousands of follow-up papers since CheXNet 2019 |
| arXiv | ok | dozens of preprints last 6mo on the same architecture/dataset |
| PubMed | ok (BMED-adjacent) | many clinical papers but topic is methodological-CS |
| bioRxiv | ok (no matches) | not a preprint-active niche |
| Perplexity | ok | hs_precedent_found: TRUE — many HS Kaggle attempts (but mostly identical) |
| ISEF archive | ok | sim 0.7 to multiple SFTD/CBIO winners last 5y → M4 = −5 cargo_cult_penalty |

## Scores

LLM judgments:
```json
{
  "T1_1_a_reframing":  {"score": 2, "rationale": "Known method on known dataset; no reframing"},
  "T1_1_b_crossdisc":  {"score": 3, "rationale": "CS-only; medical context is data, not methodology"},
  "T1_2_ownership":    {"score": 9, "rationale": "Student wrote pipeline; but architecture and dataset are public"},
  "T1_3_legibility":   {"score": 12, "rationale": "Image classification is visualizable + panel-grasped"},
  "T2_1_feasibility_base": {"score": 9, "rationale": "Free dataset; Colab; trivial budget"},
  "T2_2_curriculum":   {"score": 8, "rationale": "AP CSA + AP Stats; CNNs slightly beyond AP"},
  "T2_3_learncurve":   {"score": 8, "rationale": "Modular; week 1 = load + baseline train"}
}
```

Heuristic:
- T1.1.c anti-saturation = 2 (pct 96 → "> 90" → 2/10)
- Substrate detection = none (no human-subjects despite medical context)

## Computation

```
T1.1 = 2 + 3 + 2  =  7 /30
T1.2 =               9 /15
T1.3 =              12 /15
T2.1 =               9 /10  (no compliance cap — synthetic dataset)
T2.2 =               8 /10
T2.3 =               8 /10
tier_subscore     = 53 /90

SFTD multiplier × 1.00:
adjusted = 53 × 1.00 = 53

Modulators:
M1 = −5  (96th pct — saturated)
M2 = +3  (HS precedent abundant — but undifferentiated)
M3 = +1  (1+ preprint adjacent)
M4 = −5  (cargo-cult — multiple SFTD winners pattern-match)
sum     = −6

modded = 53 − 6 = 47
final  = round(47 × 100 / 106) = round(44.3) = 44
```

Confidence: high (all 6 sources reached).
range = [44 − 3, 44 + 3] = [41, 47].

## Final output

```
Score: 41–47 / 100  (range = ±3)
Confidence: high  (all sources reached)
Tier label: [SUPPRESSED — pending Phase 1.5 back-test validation]
Rubric version: 2026.1

Pivots suggested:
  • Pivot A: shift T1.1 by reframing the question (causal feature analysis
    instead of classification). Adds ~12 pts on creativity, drops 2 on
    curriculum fit.
  • Pivot B: shift to a niche underexplored dataset (rare disease, low-
    resource setting). Improves M1 from saturated to sweet spot.
  • Pivot C: invert M4 — apply ResNet-style CNN to a non-image substrate
    (audio for respiratory diagnostics) where the visual-domain prior
    becomes a methodological choice, not a default.
```

## What this anchor confirms

- **Saturated public-dataset application** lands well below 55 (the "category finalist likely" floor implied by `references/rubric-topic-stage-extensions.md` §4.3 calibration anchors).
- **M2 accessibility (+3) doesn't rescue a saturated topic** — the +3 is overwhelmed by M1 (−5) + M4 (−5).
- **No compliance cap** despite "chest X-rays" appearing in the topic — the rubric correctly identifies that working with a synthesized public dataset doesn't involve human participants in the IRB sense.
- **High confidence + tight range** when evidence is dense, even when the score is bad.

## Spread vs. PHYS021

|  | PHYS021 | ResNet anti-pattern | Gap |
|---|---|---|---|
| T1.1 creativity | 25/30 | 7/30 | 18 |
| M1 | +2 | −5 | 7 |
| M4 | 0 | −5 | 5 |
| **Final point** | **80** | **44** | **36** |
| Final range | 67–93 | 41–47 | non-overlap by 20+ when both at high confidence |

This is the design intent: a genuinely creative reframing beats a saturated application even when both are equally feasible.
