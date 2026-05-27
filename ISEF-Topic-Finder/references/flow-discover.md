# Flow: `discover` mode

Triggered when the user invokes `/isef-topic-finder discover` (or just types something like "help me find an ISEF topic"). Interest-first flow: the student doesn't have to know their category upfront.

## §1 — Prologue (run silently, then ask)

1. Confirm depth + language (single bundled question; see SKILL.md "Prologue").
2. Load `references/rubric-topic-stage-extensions.md`.
3. Load `references/winner-patterns.md` (skim only — full file is for grounding the topic-generation step).

## §2 — Intake (5 questions, asked one at a time)

Ask one at a time. Wait for each answer. Use plain text — these need free-form answers, not multiple choice.

1. **Interests** — *"Tell me what excites you in 2–4 sentences. What's the kind of question you've found yourself thinking about even when no one's making you?"*
2. **Background** — *"What are you good at? List up to 3 things — coursework, hobbies, technical skills. Be specific: 'AP Bio + Python' beats 'science and coding.'"*
3. **Resources** — *"What do you have access to? School lab equipment, datasets, a microscope, a 3D printer, a community garden, an internship at X? Anything specific."*
4. **Time** — *"How many weeks can you work on this before your fair?  And how many hours per week?"*
5. **Math/code comfort** — *"On a scale of 1–5: how comfortable are you with multivariable math? With reading a paper that has equations? With writing 100+ lines of Python?"*

After all 5 answers, write a 3-sentence student profile summary back to the student and ask: *"Does this capture you accurately? Anything to add?"* — this is the determinism anchor (A6); cache by hash of this confirmed profile.

## §3 — Category mapping

Based on the confirmed profile, propose **2–3 ISEF categories** that fit. Use `references/category-map.md` rules; do NOT just pick the most obvious one. Justify each in 1 sentence.

Example output:
```
Based on your profile (AP Bio + Python + school lab + microscope + 14 weeks + math/code 4/5),
three categories fit:
1. CELL — your microscope access + biology interest naturally lands here, but watch the IRB/IACUC
   pathway if anything moves toward animal/human work.
2. BMED — same biology but more applied; if you're motivated by translational impact, this is a
   stronger fit than CELL.
3. CBIO — your Python comfort opens computational biology; this category rewards students who
   can fuse wet-lab and code.
Want me to explore topics in all three, or narrow to one?
```

If the student narrows, proceed with their choice. If they say "all three," proceed but cap topic generation at 2 candidates per category (= 6 total before prefilter).

## §4 — Topic generation (anchored, not free inference)

Generate 6–10 candidate topic phrases. **CRITICAL: each candidate must follow the scaffold in `references/topic-generation-heuristics.md`.** Specifically each candidate must:

1. Instantiate a recurring winner pattern from `references/winner-patterns.md` (the file lists them). Don't invent free-form.
2. Name a substrate cluster (A=vertebrate, B=human participants, C=PHBA/tissue, D=field, E=hazardous, F=low-substrate) — picked from `references/compliance-quickref.md`.
3. Name a 2nd discipline (for cross-disciplinary bridge per T1.1.b).

Reject (silently regenerate) any candidate that:
- Uses pure rare-keyword combos with no winner pattern (e.g. "quantum origami in vegan biomes")
- Doesn't name a 2nd discipline
- Is identical to a topic that won the same category in the last 3 years (M4 penalty arm — checked via `search_isef_archive.py`)

## §5 — Cheap prefilter (T1.1 only)

Run T1.1 scoring on each candidate using Claude inference alone (no API calls yet). Keep the top 5. This prevents the expensive cross-validation step from fanning out to weak candidates and blowing the context window in `--depth heavy` mode.

## §6 — Cross-validate

For each of the 5 surviving candidates, invoke `scripts/cross_validate.py` (parallel HTTP fan-out + Perplexity skill-wrap). It returns an evidence pack per topic.

## §7 — Score

For each candidate, invoke `scripts/score_topic.py` against its evidence pack. Get a scorecard JSON per topic.

## §8 — Hypothesis gate (only on final selection)

Show the student the top 3 candidates with their scores and short rationales. Ask: *"Which of these grabs you? Pick one and I'll go deeper. If none feel right, tell me why and I'll regenerate."*

Once they pick, run the hypothesis gate from `references/flow-score.md` §3. No deep-dive rendering until they pass the gate.

## §9 — Render

Render depth-aware. Use the templates in §10 below.

If the chosen topic's T2.3 < 5, **abort the deep-dive** and emit the readiness off-ramp from `references/readiness-off-ramp.md` instead.

## §10 — Output templates

### Light (≤ 1 page/topic, 3 topics)

```
# Top topics for your profile

## 1. [Topic name]                                              Score: 73–82 (medium)
**Pitch (1 paragraph):** ...
| Tier | Sub-score | Notes |
| T1   | 48/60    | Reframing strong; cross-disc weak |
| T2   | 21/30    | Feasible; some IRB risk |
| Mods | +5        | Trend velocity favorable |
**Top anchor:** Smith et al. 2024, "...". OpenAlex W4385...
**Compliance flags:** none

## 2. ... (same template)
## 3. ...
```

### Medium (2–3 pages/topic, 3 topics) — DEFAULT

For each topic, include:
- Pitch (1 paragraph, ≤ 100 words)
- Tier breakdown (full table with all 6 dimensions + 4 modulators, with rationale per row)
- 3 anchor citations (year, source, 1-line why-it-matters, ID)
- Week-1 concrete task (≤ 50 words)
- Top 3 risks (1 line each)
- Compliance flags (form numbers if any)

### Heavy (4–5 pages/topic, ≤ 3 topics)

Medium template + literature window (1 page summarizing 8–12 papers in this niche) + 12-week timeline + budget/equipment estimate + ISEF forms list.

Always tail with the SKILL.md epilogue (AI-use disclosure + handoff to `science-fair-judge`).
