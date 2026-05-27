# Research Plan Critique Rubric

Run this rubric on the drafted Research Plan in Step 4. Output critique as
`Research-Plan-Critique.md` with items grouped by severity:

- **MUST FIX**: SRC will reject or interview-defense will fail
- **SHOULD FIX**: significantly weakens the plan
- **NICE TO HAVE**: polish

## Per-section critique checks

### §A Rationale

| Check | MUST / SHOULD / NICE |
|---|---|
| Specific real-world need or scientific gap stated (not generic "X is important") | MUST |
| Cites at least one source for "the gap" | SHOULD |
| Connects to a specific stakeholder population | SHOULD |
| Cross-disciplinary angle articulated (if applicable) | NICE |

### §B Hypothesis / Research Question

| Check | MUST / SHOULD / NICE |
|---|---|
| Falsifiable: states what result would prove the hypothesis wrong | MUST |
| Variables clearly identified (DV, IV, controls) | MUST |
| Hypothesis is a *prediction*, not a description | MUST |
| Hypothesis is specific enough to be testable in the time window | SHOULD |

### §C Methodology / Procedures

| Check | MUST / SHOULD / NICE |
|---|---|
| Another student could follow the procedure step-by-step | MUST |
| Sample size stated with rationale | MUST |
| Controls explicit | MUST |
| Equipment specifications named (model, source) | SHOULD |
| Pilot status disclosed (done / not done / planned) | SHOULD |
| Contingency for methodological failure | SHOULD |

### §D Risk Assessment

| Check | MUST / SHOULD / NICE |
|---|---|
| All substrate clusters from `/isef-compliance-walker` are addressed | MUST |
| Mitigation listed for every identified hazard | MUST |
| Required forms (per `/isef-compliance-walker`) explicitly named | SHOULD |
| For human-participant: privacy + consent process detailed | MUST if cluster B |
| For animal: husbandry + endpoint criteria | MUST if cluster A |

### §E Data Analysis

| Check | MUST / SHOULD / NICE |
|---|---|
| Stated BEFORE experimentation (not after) | MUST |
| Specific statistical test named (not just "I'll analyze the data") | MUST |
| Test is appropriate for the design (paired vs unpaired, parametric vs not) | SHOULD |
| Outlier policy stated | SHOULD |
| Pre-registered vs exploratory distinction made | SHOULD |

### §F Bibliography

| Check | MUST / SHOULD / NICE |
|---|---|
| ≥5 sources | MUST |
| ≥3 primary research papers (not just reviews) | SHOULD |
| Citation style consistent | MUST |
| No citation appears in plan body without appearing in bibliography (and vice versa) | MUST |
| Recent (last 5 years) sources for the methodology | SHOULD |

## Common pitfalls flagged automatically

The critique should also flag these student-frequent issues:

1. **"I will study X"** — vague. Replace with "I will test whether X causes Y."
2. **"Sample size: as many as possible"** — invalid. Name a target with rationale.
3. **"Control: nothing"** — invalid. Either name a baseline or explain why no control applies (rare).
4. **"I'll use statistics to analyze"** — vague. Name the specific test.
5. **"My mentor will handle the IRB"** — risky. The student must own the compliance flow.
6. **No mention of AI use** when the project uses AI/ML — violates ISEF 2026 disclosure rules.

## Output format

```
RESEARCH PLAN CRITIQUE — [project title]
=========================================

MUST FIX (gates SRC submission)
────────────────────────────────
- [section §X] [issue with one-line rationale]
- ...

SHOULD FIX (gates competitive interview)
─────────────────────────────────────────
- [section §X] [issue with one-line rationale]
- ...

NICE TO HAVE
─────────────
- [polish suggestions]

OVERALL: [Ready for SRC | Needs revision | Major rework needed]
```
