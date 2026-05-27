# Flow: `score` mode

Triggered by `/isef-topic-finder score "topic text"`. Student already has an idea; you give it a rigorous proxy-score and suggest pivots.

## §1 — Prologue

1. Confirm depth + language.
2. Load `references/rubric-topic-stage-extensions.md`.

## §2 — Category inference

Infer the ISEF category from the topic text. If ambiguous (covers 2+ categories), ask the student which they're targeting. Use `references/category-map.md` to map.

## §3 — Hypothesis-articulation gate (REQUIRED — A15)

Before any rubric scoring, emit:

```
HYPOTHESIS GATE
================
What would make you wrong? Write one sentence describing what experimental or
analytical result would falsify your hypothesis. If you cannot answer this
in 1 sentence, your topic is not yet a research project — it is a research
interest. The skill will help you sharpen it.

Examples:
- "If origami crease patterns sample uniformly across configurations, my
  statistical-mechanics analogy is wrong."
- "If patients with diabetes show no correlation between metric X and Y,
  my hypothesis is wrong."

Your hypothesis:
```

**Refusal cases** (do not proceed with scoring; instead enter the sharpening sub-dialog):

- Blank
- Contains only verbs like "study", "investigate", "explore" with no concrete failure mode
- Names a topic, not a falsifiable prediction (e.g., "AI and mental health" — what about it?)
- Has no measurable variables

### Sharpening sub-dialog

When the gate refuses, conduct 2–4 turns of clarification:

1. *"What's the question — what would a yes-or-no answer to it look like? Don't tell me the topic, tell me the question."*
2. *"If you ran the experiment and got the result you DON'T expect, what would the result look like?"*
3. (If still vague) *"Pick a specific variable you'd measure. What unit is it in?"*
4. (If still vague) Refuse the score gracefully: *"I can't score this yet — the hypothesis is still at the interest stage. Want to switch to `discover` mode to explore framings?"*

Cache the passed hypothesis with the topic so reruns don't re-prompt.

## §4 — Cross-validate

Once hypothesis gate passes, run `scripts/cross_validate.py` on the topic. Returns evidence pack.

## §5 — Score

`scripts/score_topic.py` → scorecard JSON.

## §6 — Generate pivots (2–3 alternatives)

For each of the lowest-scoring dimensions (lowest 2–3 of T1.1, T1.2, T1.3, T2.1, T2.2, T2.3), suggest one concrete pivot that would lift that dimension while preserving the student's core interest.

Example:
```
WEAKEST DIMENSIONS

T1.1 Creativity (16/30) — Reframing signal is weak; you're applying a known
method (logistic regression) to a known domain (UCI heart-disease dataset).

  Pivot A — Reframe the dataset, not the method.
  Instead of predicting heart disease from features, ask: "Can the feature
  vector for a healthy patient be deformed continuously into the feature vector
  for a diseased patient? What's the geodesic distance?" Now it's a manifold-
  learning problem with biomedical motivation. T1.1 → ~24/30, T2.2 (curriculum)
  drops slightly because manifold learning is post-AP, but T1.3 (legibility)
  goes up because the geometric framing is visualizable.

  Pivot B — Reframe the question, not the answer.
  Instead of "predict disease from features," ask: "Which subset of features
  is causally upstream of disease (vs. correlated)?" Now it's a causal-
  inference problem with HS-friendly do-calculus framing. T1.1 → ~22, M2
  (accessibility) high (open-source causal-inference libraries exist).

T2.1 Resource feasibility (7/10, capped due to IRB mention)
  Pivot — drop the human-subject angle. ...
```

If overall score < 55, also suggest: *"Consider running `/isef-topic-finder discover` from your underlying interest instead of stress-testing this specific framing."*

## §7 — Render

Render depth-aware. Use the templates in `references/flow-discover.md` §10 but adapted for single-topic output:

- **light:** scorecard table + composite range + top 2 pivot suggestions (1 line each)
- **medium (default):** full tier breakdown with rationale + 3 anchor citations + ≥2 pivots (2 paragraphs each) + compliance flags
- **heavy:** medium + literature window for the topic + per-dimension pivot deep-dive + 12-week timeline + form list

Tail with SKILL.md epilogue.

## §8 — Off-ramp branch

If T2.3 < 5 OR if the hypothesis-articulation sub-dialog terminated without a passable hypothesis, do NOT emit pivot suggestions. Instead emit the readiness off-ramp from `references/readiness-off-ramp.md`. Be kind about it — these students are often well-meaning beginners.
