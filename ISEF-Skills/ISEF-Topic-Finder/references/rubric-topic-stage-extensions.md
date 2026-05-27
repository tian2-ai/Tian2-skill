# Topic-stage predictive rubric (extends the official ISEF rubric)

**Purpose:** Estimate the probability that a topic will be well-received by ISEF judges *before* the project is built. Layered on top of the official 100-point ISEF rubric at `references/rubric.md` (which judges actual posters & interviews). This layer is predictive; the official rubric is evaluative.

**Rubric version:** 2026.1

---

## §0 — What this rubric is, and is not

This rubric measures **falsifiable proxies for the conditions under which a creative project tends to win**. It does NOT measure creativity itself; nothing automated can.

- A high score is *evidence* that judges are likely to find the topic exciting. It is not a verdict that the topic is good.
- A low score is reason to think harder, not reason to abandon.
- A range output (e.g., `73–86`) means evidence is mixed or sources are missing. Treat the range, not a single number.

**Two safeguards prevent rubric-optimization pathology:**

1. **Hypothesis-articulation gate (A15)** — `score` mode requires a 1-sentence falsifiable hypothesis from the student before scoring. No falsifiable hypothesis → no rubric output.
2. **Range-not-point reporting (A10)** — until Phase 1.5 back-testing validates calibration against ≥30 known winners + ≥30 known non-placers (AUC ≥ 0.70 gate), every score is a range with explicit confidence, and tier labels are suppressed.

---

## §1 — Tier 1: Award-tier signals (60 pts)

These dimensions are the strongest predictors of placing at ISEF. They mirror the official rubric's "Creativity & Potential Impact" (Category IV) and the Interview component's "degree of independence" + "clear, concise, thoughtful responses."

### T1.1 Conceptual creativity (30 pts)

Mirrors ISEF's 20-pt Creative Ability + Impact category but weighted higher at the topic stage because at this phase creativity is the differentiator. The three sub-checks each carry 10 points:

| Sub-check | Pts | What earns full marks |
|-----------|-----|-----------------------|
| (a) Reframing signal | 10 | Topic phrasing recasts a known mechanism/object in a different formal lens (e.g., origami → statistical-mechanics ensemble). Pure application of method-X to dataset-Y earns ≤3. |
| (b) Cross-disciplinary bridge | 10 | Topic explicitly names ≥2 fields from distinct ISEF categories (e.g., PHYS + BMED, MATH + ENBM). One-field topics earn ≤5. |
| (c) Anti-saturation | 10 | OpenAlex velocity (category-normalized percentile) puts this topic-concept-cluster in the 30th–70th percentile within its category. 90th+ percentile or 5th– percentile earns ≤3. |

### T1.2 Verifiable student ownership (15 pts)

The single biggest "is this real" signal. ISEF judges spend 4+ interview minutes probing this.

| Sub-check | Earns full marks if… |
|-----------|---------------------|
| No mentor/lab black-box | Topic doesn't require access to a specific PI's lab, proprietary dataset, or unobtainable equipment |
| Validates against a known solution | The first deliverable is reproducing a known result before extending — a built-in sanity check |
| Equipment/data accessibility | School-grade equipment, public datasets, open-source code, or budget <$500 |
| Defensibility | Student can explain every methodological choice without invoking "my mentor said" |

### T1.3 Cross-disciplinary legibility (15 pts)

Mixed-discipline judging panels rotate every ~15 minutes. The topic must be graspable in 6 minutes by a judge from an adjacent field.

| Sub-check | Earns full marks if… |
|-----------|---------------------|
| One-sentence pitch test | Topic can be stated in 1 sentence that a chemist understands and a physicist understands |
| Visualizable result | The eventual finding is a graph, image, video, or working device — not just a number |
| Connects to a known concern | Ties to something the panel already cares about (climate, disease, energy, computation efficiency) |

**Anti-clamp rule:** If T1.1 ≥ 25, T1.3 has a floor of 10/15. Don't punish PHYS021-style topics for being too novel to be immediately legible to *every* panelist; full-panel legibility is unrealistic for genuine reframings.

---

## §2 — Tier 2: Feasibility gates (30 pts)

These are pre-conditions — you can't compete if you can't do the work. They are not on the official rubric (you wouldn't even reach judging if you failed them).

### T2.1 Resource feasibility (10 pts)

| Sub-check | Earns full marks if… |
|-----------|---------------------|
| Equipment + data + software | All available without insider access |
| Cost | <$500 OR has a clear funding path |
| Time | Fits the student's stated time window (typically 12–20 weeks) |
| Compliance | Passes ISEF triage (no impossible IRB/IACUC pathways in the available timeline) |

**Compliance bias rule (A7):** If the topic mentions humans, animals, tissue, pathogens, or hazardous chemicals — even in passing — T2.1 is capped at 7/10 until a human review confirms the compliance pathway is realistic. Bake the safety bias into the score so students cannot ignore a flag.

### T2.2 High-school curriculum hook (10 pts)

If a student can't anchor a topic in something they're being taught, they'll struggle to explain it to a teacher (who is usually their first reviewer) and to a non-specialist judge.

| Sub-check | Earns full marks if… |
|-----------|---------------------|
| Course mapping | Maps to a specific AP / IB / CN-gaokao / A-level course (e.g., AP Physics C: Mechanics for PHYS021's degrees-of-freedom analysis) |
| Teacher explainability | Student can explain the conceptual foundation to a non-specialist teacher in 5 minutes |
| Textbook existence | The foundational chapter exists in a standard textbook (not just papers) |

See `references/high-school-curriculum-anchors.md` for the full mapping.

### T2.3 Learning-curve gradient (10 pts)

| Sub-check | Earns full marks if… |
|-----------|---------------------|
| Week-1 task is concrete | "Implement Metropolis sampler on a 2-fold linkage" beats "read the literature" |
| Modular milestones | Each 3–4 week milestone is independently presentable; the project doesn't collapse if a later phase fails |
| No all-or-nothing | The student has a publishable result even if the most ambitious extension doesn't work |

**Off-ramp rule (A14):** If T2.3 < 5/10, do not output competition-grade topic recommendations. Instead output the preparatory project tier from `references/readiness-off-ramp.md`. A 14-year-old whose week-1 task is "read 30 papers" is not ready for ISEF and needs to build skills first; serving them PHYS021-tier topics produces failure, not winners.

---

## §3 — Tier 3: Discovery modulators (±13 pts)

Modulators **adjust** the Tier-1+2 score. They never stand alone. Range is intentionally smaller than Tier 1/2 because these are weak signals built on smaller datasets.

**Order of operations** (important — different implementations would otherwise produce different scores):

```
tier_subscore  = T1.1 + T1.2 + T1.3 + T2.1 + T2.2 + T2.3                 # 0–90 pre-multiplier
adjusted       = tier_subscore × category_multiplier                       # multiplier ∈ [1.0, 1.2]; applies to TIER SUBSCORES ONLY
modded         = adjusted + M1 + M2 + M3 + M4                              # max ≈ 108 + multiplier headroom; min ≈ −13
final          = clamp(round(modded × 100 / 106), 0, 100)
```

### Modulators

| ID | Modulator | Range | Logic |
|----|-----------|-------|-------|
| M1 | **Trend velocity** | ±5 | OpenAlex papers/year for the topic's concept cluster, **category-normalized percentile**. Sweet spot: 30th–70th percentile within category → +5. 90th+ percentile (saturated) → −5. 5th– percentile (vapor) → −3. |
| M2 | **Accessibility signal** | ±3 | Perplexity query: `"<topic>" high school OR undergraduate research`. Bonus if there's known HS precedent (open-source kits, school-friendly datasets, robotics-club analogs). Penalty if topic only surfaces in industry/PI-lab contexts. **REPURPOSED from "press/funding momentum"** (v1) — adult funding poorly predicts student success. |
| M3 | **Preprint freshness** | ±3 | bioRxiv/arXiv last 6 months: ≥3 preprints on or adjacent to the topic → +3. Zero preprints → −1. |
| M4 | **Prior-winner alignment (INVERTED)** | −5 to +2 | ISEF-Scrape pattern match. **Penalty** if same category has had a structurally-similar winner in the last 5 years (cargo-cult risk). **Bonus (max +2)** only if the topic *imports a winning structure from a different category* — e.g., a PHYS-winning statistical-mechanics framing applied to a BMED problem. M4 = 0 when the ISEF-Scrape corpus has sparse coverage for that category-year. |

### Per-category multipliers (apply to `tier_subscore` only)

Some categories weight criteria differently in judging. Apply these multipliers to T1.1+T1.2+T1.3 (Tier 1) and leave Tier 2 unmultiplied. Source: `science-fair-judge/references/judge-preferences.md` + ISEF-Scrape PHYS judging guide.

| Category | Multiplier | What it amplifies | Source |
|----------|------------|-------------------|--------|
| PHYS, MATH | 1.10 | Creativity (judges reward reframing) | PHYS-judging-guide-2026-05-13.md |
| BMED, CELL | 1.05 (cap on T1.2 only) | Feasibility scrutiny — judges deeply audit student ownership | judge-preferences.md |
| ROBO, EBED | 1.05 (cap on T1.3 only) | Concrete prototype required for legibility | judge-preferences.md |
| EGSD, ENEV | 1.05 (T1.3 only) | Real-world impact framing | judge-preferences.md |
| All others | 1.00 | No specific adjustment | — |

---

## §4 — Composite scoring & confidence

### §4.1 Score-as-range

Until Phase 1.5 back-testing produces an AUC ≥ 0.70 on a winner/non-winner cohort, every output is:

```
Score: 73–86 / 100  (range = ±13 from missing sources/uncertainty)
Confidence: medium  (Perplexity unavailable; M2 not applied)
Tier label: [SUPPRESSED — pending back-test validation]
Rubric version: 2026.1
```

After Phase 1.5, if AUC ≥ 0.70, tier labels become available. Tier thresholds are derived from the back-test (Youden's J or equivalent), NOT from a single anecdote.

### §4.2 Confidence bands

| Sources reachable | Range width | Confidence | Tier label emitted? |
|-------------------|-------------|------------|---------------------|
| All 5 | ±3 | high | Yes (after Phase 1.5) |
| 3–4 | ±6 | medium | No |
| 0–2 | full range | low | No |

When confidence < high, the rendered output has a banner explaining which sources are missing and what that means for interpretation.

### §4.3 Calibration anchors (illustrative; to be re-derived in Phase 1.5)

These are NOT authoritative. The real values come from the back-test. They are placeholders to sanity-check the implementation:

| Topic | Expected score range | Why |
|-------|---------------------|-----|
| PHYS021 "MCMC Sampling of Origami and Linkages" (2026 grand-award contender) | ~85–93 | Reframing + cross-disciplinary + verifiable + accessible |
| "Trained ResNet to classify chest X-rays on a Kaggle dataset" | ~40–55 | Known method, public dataset, low T1.1, M1 penalty (saturated) |
| "Survey high schoolers about social media use" | ~30–45 | IRB-heavy compliance bias caps T2.1; T1.2 low (mentor or template-driven) |
| "Cross-category import: stat-mech analysis of a BMED tissue-folding problem" | ~75–88 | T1.1 reframing high; M4 cross-category bonus arm |
| "First-time programmer's idea: build an AI chatbot for homework help" | trigger readiness off-ramp | T2.3 < 5 |

Per-dimension working for PHYS021 is in `examples/score-phys021.md` and must be re-derived from back-tested rubric before tier labels go live.

---

## §5 — Scorecard JSON schema

`scripts/score_topic.py` emits one of these per topic:

```json
{
  "rubric_version": "2026.1",
  "topic": "string",
  "inferred_category": "PHYS|MATH|BMED|...",
  "tiers": {
    "T1_1_creativity": {"score": 28, "max": 30, "sub": {"reframing": 9, "crossdisc": 10, "antisat": 9}, "rationale": "..."},
    "T1_2_ownership":  {"score": 14, "max": 15, "rationale": "..."},
    "T1_3_legibility": {"score": 13, "max": 15, "rationale": "...", "anticlamp_applied": false},
    "T2_1_feasibility":{"score": 9,  "max": 10, "rationale": "...", "compliance_cap_applied": false},
    "T2_2_curriculum": {"score": 8,  "max": 10, "rationale": "..."},
    "T2_3_learncurve": {"score": 8,  "max": 10, "rationale": "...", "off_ramp_triggered": false}
  },
  "category_multiplier": 1.10,
  "multiplier_scope": "tier1_only",
  "modulators": {
    "M1_trend_velocity":    {"value": 4,  "evidence": "OpenAlex percentile=42 within PHYS"},
    "M2_accessibility":     {"value": 2,  "evidence": "open-source MCMC kits, HS precedent in 2 prior winners"},
    "M3_preprint_freshness":{"value": 2,  "evidence": "4 arXiv preprints in last 6mo on adjacent topics"},
    "M4_prior_alignment":   {"value": 1,  "arm": "cross_category_import", "evidence": "no in-category structural twin; imports stat-mech framing"}
  },
  "composite": {
    "tier_subscore": 80,
    "adjusted":      87.5,
    "modded":        96.5,
    "final_point":   91,
    "final_range":   [88, 93],
    "confidence":    "high",
    "tier_label":    "[SUPPRESSED — pending Phase 1.5]",
    "missing_sources": []
  },
  "compliance_flags": [],
  "anchor_citations": [{"title": "...", "year": 2024, "source": "OpenAlex", "id": "W123...", "why_it_matters": "..."}],
  "warnings": []
}
```

Any field present in the schema but unverified (e.g., M1 evidence is "estimated, source unavailable") must be flagged in `warnings`.

---

## §6 — What gets emitted to the student

Depth-aware. See `references/flow-discover.md` and `references/flow-score.md` for full templates. Summary:

- **light**: 1-paragraph pitch per topic + tier breakdown table + composite range. ≤ 1 page/topic.
- **medium**: pitch + tier rationales + 3 anchor citations + week-1 task + key risks. 2–3 pages/topic.
- **heavy**: medium + 1-page literature window + 12-week timeline + form/compliance checklist + budget. 4–5 pages/topic, ≤ 3 topics.

All depths end with the epilogue defined in SKILL.md.
