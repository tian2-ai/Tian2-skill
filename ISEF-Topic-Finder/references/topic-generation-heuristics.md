# Topic Generation Heuristics

**Purpose:** When `discover` mode generates candidate topic phrases (`flow-discover.md` §4), this file constrains the generation. Without these constraints, the highest-variance step in the pipeline produces rare-keyword combos that score well on the rubric but mean nothing.

The Critic's v1 BLOCKER on "rubric measures byproducts of insight, not insight" is mitigated here — not in §4.0 of the rubric.

## §1 — Mandatory constraints (every candidate must satisfy all 3)

Every generated topic phrase must satisfy ALL of:

1. **Instantiate a pattern from `references/winner-patterns.md`.** Name the pattern explicitly (e.g., "P1: Reframe mechanism as statistical ensemble"). No free-form generation.
2. **Name a substrate cluster** from `references/compliance-quickref.md` §1 (A–F). The cluster determines forms and time profile.
3. **Name a 2nd discipline** for the cross-disciplinary bridge (T1.1.b). The 2nd discipline must be from a DIFFERENT ISEF category than the primary one.

Internal scratchpad for each candidate (NOT shown to student):

```
Candidate phrase: "Statistical-mechanics analysis of HVAC airflow patterns in a school building"
Pattern instantiated: P1 (Reframe mechanism as stat ensemble) + P7 (Local empirical)
Substrate cluster: D (field work — air sampling)
Primary category: PHYS (Mechanics)
2nd discipline: EAEV (atmospheric science)
M4 arm: cross_category_import (PHYS framing imported to EAEV substrate)
```

## §2 — Rejection rules (silently regenerate)

Reject and regenerate (without showing the student) any candidate that:

| Rejection rule | What it catches |
|----------------|-----------------|
| No pattern instantiated | Free-form generation; rare-keyword pathology |
| 2nd discipline same as primary | Not cross-disciplinary; T1.1.b will score low |
| Title-token cosine similarity > 0.7 to any ISEF top-3 winner from last 3 years | M4 cargo-cult penalty applies |
| Topic matches any anti-pattern from `winner-patterns.md` §3 | E.g., "train [NN] on [public dataset]" |
| 2nd discipline named but never used substantively in the topic phrasing | Tokenistic; will be penalized in T1.1.b evidence |
| Requires equipment the student didn't list | T2.1 will fail; waste of a candidate slot |
| Requires more time than the student has | T2.3 will fail |
| Requires substrate cluster A, B, or C when student didn't mention having access to relevant approval pathways | T2.1 compliance bias caps it |

## §3 — Generation prompt scaffold (internal)

When generating a candidate, follow this internal prompt structure:

```
Given the student profile:
  interests: ...
  background: ...
  resources: ...
  time: ...
  math/code: ...

For the target category [X]:
  1. Pick a pattern from winner-patterns.md (P1–P7). Justify why this pattern fits this student.
  2. Name a 2nd discipline from a different ISEF category that the student has at least *some* exposure to.
  3. Pick a substrate cluster (A–F) compatible with the student's time and resources.
  4. Phrase the topic in 1 sentence (≤ 20 words). The phrasing must read as a question or a verb-led statement, not as a fragment.
  5. Self-check against the rejection rules in §2. If any rule fires, regenerate.
```

## §4 — Diversity rule

When generating multiple candidates for the same category, ensure diversity:

- No two candidates should instantiate the same pattern.
- No two candidates should share the 2nd discipline.
- Substrate clusters should span at least 2 different letters across the candidate set (don't generate 3 cluster-B human-subject candidates when the student has no IRB pathway).

## §5 — What this is not

This file does NOT teach Claude how to think creatively. It cannot. What it does is:
- Block obvious failure modes (rare-keyword combos, derivative topics, infeasible setups)
- Force every generation to anchor to a known winning structure
- Ensure cross-disciplinary signal is real, not tokenistic

Genuine creativity in topic suggestion comes from the student's own articulation of what excites them (`flow-discover.md` §2 intake) — Claude amplifies and structures it, but does not originate it.

## §6 — Quality bar (informal)

A good generated candidate, when shown to a domain expert, should produce one of two reactions:
- *"Oh, that's a neat angle — I haven't seen anyone try it."* (TARGET)
- *"That's straightforward but solid for a high schooler."* (ACCEPTABLE)

It should never produce:
- *"What does that even mean?"* (rare-keyword failure)
- *"That's been done a hundred times."* (cargo-cult failure)
- *"You can't actually do that in a high-school setting."* (feasibility failure)

If a candidate would produce any of the three failure reactions, regenerate.
