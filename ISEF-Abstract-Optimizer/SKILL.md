---
name: isef-abstract-optimizer
description: >
  Critique and tighten an ISEF abstract against the official constraints (250 words max, one
  page, SRC-approved version is the only one displayed at the booth). Checks word count,
  structural balance (purpose → method → results → significance), specific failure modes
  (missing impact statement, methods-bloat, vague significance, mentor-credit ambiguity),
  and rubric alignment (the abstract is part of the 10-point poster score per the official
  ISEF rubric). Outputs a rewritten draft + a critique. Use this skill whenever the student
  mentions "ISEF abstract", "abstract review", "shorten my abstract", "改简介", "摘要修改",
  "250 words", or has finished experimentation and is preparing the Official Abstract for
  SRC submission and booth display.
argument-hint: [--max-words 250] [--lang en|zh|both] [--target-grade nine|ten|eleven|twelve]
allowed-tools: Read, Grep, Glob, Bash, Skill
rubric_version: 2026.1
---

# ISEF Abstract Optimizer

The Official Abstract & Certification is one of the few documents physically present at the
ISEF booth (vertically displayed, per DS-Rules.pdf), and it's the first thing judges read.
The SRC-approved version is the only one allowed. Word limit is 250 (per Book.pdf line 241).

You critique and tighten the student's draft against three things:
1. **Hard constraints** — word count, one-page format
2. **Structural balance** — purpose / method / results / significance proportions
3. **Common failure modes** — methods-bloat, vague significance, mentor-credit ambiguity, AI-use undisclosed

You output a rewritten draft and a per-line critique. The student decides what to keep.

## When to use

- Student says "review my abstract", "shorten my abstract", "改简介", "250 words"
- Student has data and is preparing the Official Abstract for SRC submission
- Coach/teacher running cohort-level abstract review

Don't use this for: writing the abstract from scratch when the student doesn't yet have results
(they need to do the science first), or for non-ISEF abstracts (general conference abstracts
have different conventions).

## Hard constraints (from ISEF 2026 official rules)

| Constraint | Value | Source |
|---|---|---|
| Word count | 250 maximum | Book.pdf line 241 (verified extract in playbook §Stage 4) |
| Page | 1 page | DS-Rules.pdf §3 (vertically displayed at booth) |
| Style | "Summarizes the current year's work" | Book.pdf line 245 |
| Continuation projects | Must reference and differentiate from prior abstract (Form 7) | Book.pdf 286-298 |
| AI use | Must be disclosed per Generative-AI-Use Matrix | playbook §5 AI-Use Matrix |

## Workflow

### Step 1 — Accept input

The student pastes their draft. Validate:
- Word count (warn if >250 or wildly under 200)
- Title separate or in body? (title should be separate)
- Single paragraph or multi? (single is conventional)
- Author byline included? (should be OFF the abstract for display)

### Step 2 — Structural balance check

Decompose the draft into 4 components and report their word counts:

| Component | Target words | Why |
|---|---|---|
| Purpose / question / hypothesis | 30-50 | Sets up the why |
| Method (1 sentence) | 30-50 | Just enough to credibilize; not a procedure dump |
| Results | 60-90 | The heart — specific, quantified |
| Significance / impact | 40-70 | What judges read for the "so what" |
| Transitions | 10-20 | Smooth, not padding |

Flag imbalances:
- Method > 80 words: methods bloat. Cut.
- Results < 40 words: under-claimed. Where are the numbers?
- Significance < 30 words: judges' loadbearer is anemic.
- Total < 200: under the limit; you have room to strengthen impact.
- Total > 250: HARD FAIL. Must cut.

### Step 3 — Specific failure-mode checks

Run these checks; flag any that fire:

| Check | Pattern | Flag |
|---|---|---|
| Vague significance | "could potentially help", "may inform future studies", "could improve" | Replace with specific stakeholder + specific benefit |
| Methods-as-list | semicolon-chain of techniques | Compress to one method sentence |
| Results without numbers | "improvement was observed" without %/p-value/effect size | Add quantification |
| Hedged claims | "tends to", "appears to", "suggests" (used >2x) | Replace ≥1 with declarative if data supports |
| Acronym-without-expansion | first use of MRSA/PCR/CRISPR/etc. without expansion | Expand on first use |
| Title-redundant first sentence | first sentence repeats the title | Cut |
| Mentor-credit ambiguity | "we" without team disclosure; "in the lab of Dr. X" | Either acknowledge team explicitly OR make ownership crisp |
| Future-tense for completed work | "will investigate" when results are already in | Flag — abstract is past-tense for done work |
| Continuation undisclosed | this year's vs prior year's | Must reference per Book.pdf 286-298 |
| AI use undisclosed | project used AI but abstract is silent | Add 1 sentence; aligns with 2026 disclosure rule |

### Step 4 — Produce rewrite + critique

Output:

```
================================================================================
REWRITTEN DRAFT ([X] words)
================================================================================
[The proposed rewrite. Same content, tightened structure. Footnote any
deletions or paraphrases the student should verify.]

================================================================================
PER-COMPONENT CRITIQUE
================================================================================

Purpose ([X]/[target] words)
  ✓ what's working
  ✗ what to fix

Method ([X]/[target] words)
  ...

Results ([X]/[target] words)
  ...

Significance ([X]/[target] words)
  ...

================================================================================
FAILURE-MODE CHECKS
================================================================================
[ ] vague significance         [pass/fail]
[ ] methods-as-list             [pass/fail]
[ ] results without numbers     [pass/fail]
[ ] hedged claims               [pass/fail]
[ ] acronym-without-expansion   [pass/fail]
[ ] title-redundant opener      [pass/fail]
[ ] mentor-credit ambiguity     [pass/fail]
[ ] future-tense for done work  [pass/fail]
[ ] continuation undisclosed    [pass/fail or N/A]
[ ] AI use undisclosed          [pass/fail or N/A]

================================================================================
NEXT STEPS
================================================================================
1. Review the rewrite. The proposed wording is suggestion; YOUR voice is what
   judges connect with. Edit freely.
2. Submit the final version to your SRC for approval. The SRC-approved version
   is the only one allowed at the booth.
3. Continuation projects: attach prior year's abstract + Research Plan.
4. For interview prep, after the abstract is finalized: /science-fair-interview-prep
```

### Step 5 — Bilingual rendering

If `--lang both` or the input was Chinese, output both EN and CN versions.

CN-track note: the SRC submission must be in English (ISEF rule); the Chinese version is for
the student's own clarity and possibly for the CASTIC submission package (which accepts both
languages depending on the regional fair).

## What this skill does NOT do

- Write the abstract from scratch (the student must have results to summarize)
- Replace SRC review (the SRC is the gating reviewer; this skill is a pre-review check)
- Validate the science itself (use `/science-fair-judge` for that)

## File map

```
SKILL.md (this file)
references/
  abstract-rules.md       ← extracted constraints from ISEF Book.pdf + DS-Rules.pdf
  rewrite-examples.md     ← worked examples (good vs bad)
```

## Source provenance

Word count and one-page rule: `/Volumes/Mac-Mini/workspaces/tian2-edu/Competitions/isef-research-playbook/05-analysis/project-workflow-and-category-map-2026-05-01.md` Stage 4, citing
Book.pdf line 241.

Display requirement: same playbook source citing DS-Rules.pdf.

AI-use disclosure: playbook compliance-quickref §5 AI-Use Matrix (14 rows, sourced from
Generative-AI-Use-Table.pdf).

## Output footer

```
🤖 isef-abstract-optimizer · rubric_version: 2026.1
ISEF 2026 AI-use disclosure: This skill provided a structural critique and
suggested wording. The data, the interpretation, and the final SRC-submitted
abstract are the student's own work.
```
