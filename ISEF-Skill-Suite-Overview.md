# ISEF Skill Suite — full overview

Twelve Claude Code skills covering the end-to-end ISEF student journey, from "I want to compete
but don't have a topic yet" through "I'm walking onto the booth at competition day."

All skills are installable by copy-paste into `~/.claude/skills/<skill-name>/`. Each skill is
self-contained — no external services required for the core scoring/checking workflows. Where
skills wrap other capabilities (statistical analysis, scientific writing, LaTeX poster
typesetting), they leverage existing scientific-skill libraries common in Claude Code setups.

## The student journey, mapped to skills

```
  topic    research   compliance   experiment   analysis   abstract   poster   interview   fair    next-year
  choice    plan       + IRB                                                              day      continuation
    │         │          │             │           │          │          │         │          │
    ▼         ▼          ▼             ▼           ▼          ▼          ▼         ▼          ▼
 [TOPIC-  [RESEARCH-  [COMPLIANCE-  [DATA-      [DATA-     [ABSTRACT-  [POSTER-  [INTERVIEW-PREP  [JUDGE]
  FINDER]  PLAN-       WALKER]      ANALYSIS-   ANALYSIS-   OPTIMIZER]  DESIGNER]  /PREP-FEEDBACK]
           DRAFTER]                 TUTOR]      TUTOR]                              /JUDGING-
                                                                                    PANEL-
                                                                                    RESEARCHER]

       ┌──────────────────────────────────────────────────────────────────────┐
       │ AFFILIATED-FAIR-NAVIGATOR (CASTIC 8 regions, Ying Cai, HK, Sichuan) │
       │ MENTOR-FINDER (OpenAlex search + ethical outreach drafting)         │
       └──────────────────────────────────────────────────────────────────────┘
```

## The twelve skills

### 1. ISEF-Topic-Finder

`/isef-topic-finder discover` for interest-first topic discovery; `/isef-topic-finder score "topic"`
for stress-testing a topic the student already has. Cross-validates against OpenAlex, PubMed,
bioRxiv, arXiv, and a local TF-IDF index of 62,000+ past ISEF projects. Predictive rubric that
weights creativity over rigor, with a hypothesis-articulation gate and a readiness off-ramp.
Returns score-as-range with explicit confidence; tier labels suppressed until rubric back-test
validates.

### 2. ISEF-Compliance-Walker

Walks the student through ISEF's form/approval requirements grounded in the official 2026 Rules
Book + All-Forms.pdf + DS-Rules.pdf. Asks structured intake (humans? animals? tissue?
hazardous? field?), classifies into substrate clusters, and emits the exact ISEF forms required
with the right pre/post-experimentation timing and the right review body (SRC, IRB, IACUC, IBC).
Surfaces the ISEF 2026 Generative-AI-Use Matrix when relevant.

### 3. ISEF-Affiliated-Fair-Navigator

Navigates the affiliated-fair pathway from a student's country/region to ISEF qualification.
For China-track students: covers CASTIC's 8 regional competitions + Ying Cai Plan + ISEF Hong
Kong Preliminary + ISEF Sichuan (international-school students). For US students: outlines the
regional → state → ISEF advancement path. Cites the official source (regeneronisef.org.cn,
societyforscience.org) with last-verified dates and instructions for annual refresh.

### 4. ISEF-Research-Plan-Drafter

Drafts the ISEF Research Plan in the SRC-required structure (A. Rationale, B. Research
Question/Hypothesis, C. Methodology, D. Risk Assessment, E. Data Analysis, F. Bibliography).
Walks the student through structured prompts per section — **does not invent content**, only
structures what the student provides. Includes a SRC-readiness critique pass (MUST/SHOULD/NICE)
to flag issues before submission.

### 5. ISEF-Abstract-Optimizer

Critiques and tightens an ISEF abstract against the official 250-word limit and the one-page
requirement (per Book.pdf line 241). Checks structural balance (purpose / method / results /
significance), 10+ specific failure modes (methods-bloat, vague significance, missing impact,
mentor-credit ambiguity, undisclosed AI use), and produces a rewrite + per-line critique. Two
worked before/after examples included.

### 6. ISEF-Judging-Panel-Researcher

Briefs the student on what to expect from ISEF judges by category and sub-category. Critical
honesty: ISEF does NOT publish individual judge bios pre-event, so the skill cannot research
specific judges by name. What it CAN do: per-category persona briefings (PHYS judges emphasize
creativity-over-rigor; BMED judges scrutinize ownership; ROBO judges want working demo) plus
interview-day tactics (15-min format, what to bring, what to wear). Persona table covers all 22
categories.

### 7. ISEF-Data-Analysis-Tutor

Tutors a student through analyzing experimental data in a way that passes ISEF judging without
over-engineering. Decision flowchart from design → test (paired vs unpaired, parametric vs
non-parametric, multiple-comparison correction). Wraps `/statistical-analysis` and
`/exploratory-data-analysis` for the heavy lifting; this skill provides the HS-context layer
(right-sizing complexity, judge-grasp legibility). 8 anti-patterns flagged automatically.
Fallback scipy script included if upstream skill is unavailable.

### 8. ISEF-Poster-Designer

Produces a printable, easy-to-edit ISEF poster fitted to booth constraints (76×122×240 cm per
DS-Rules.pdf). Provides parallel templates:
- **LaTeX** (tikzposter): for typography-heavy / equations / Chinese support via xeCJK
- **PowerPoint** (A0 metric or 48×36 inch): editable in PowerPoint, Keynote, Google Slides

Python builder (`build_pptx.py`) accepts a content YAML and produces a print-ready PPTX.
Legibility validator (`check_legibility.py`) checks font sizes, margins, image DPI against
WCAG-AA accessibility minimums. Outputs a booth-day checklist with what to print, what to bring,
and what NOT to bring.

### 9. ISEF-Mentor-Finder

Helps a student identify potential research mentors. Searches OpenAlex by topic and
affiliation, scores candidates on topic match + recent activity + reachability + junior-friendly
signal. Drafts personalized outreach emails — **never auto-sends**. Strong ethical guards: no
non-public-source scraping; respect researcher availability statements; one-follow-up max.
Includes alternatives section (Polygence, Pioneer Academics, AAAS, NIH STEP-UP, NSF REU,
university programs) for students for whom cold-emailing isn't the right route.

### 10. ISEF-Judge (existing)

Comprehensive science fair project evaluator and judge simulator. Reads a student's poster
(PPTX, PDF, images), runs parallel agents to fact-check content + evaluate against official
ISEF rubric + generate interview Q&A. Outputs detailed scorecard.

### 11. ISEF-Interview-Prep (existing)

Generates a 60+ bilingual (English-Chinese) Q&A document covering background knowledge,
methodology, statistics, results, limitations, impact. Strong-answer models + patterns to avoid
+ tactical interview-day tips.

### 12. ISEF-Prep-Feedback (existing)

Second-pass companion to interview-prep. Consumes the student's annotated version of the prep
document and produces question-by-question tactical responses to factual corrections, proposed
rewrites, anxieties, and additions.

---

## How they compose

**Year-out planning**:
`/isef-affiliated-fair-navigator` → `/isef-topic-finder discover` → `/isef-mentor-finder`

**Pre-experimentation (4–8 weeks before lab work)**:
`/isef-compliance-walker` → `/isef-research-plan-drafter`

**During experimentation**:
`/isef-data-analysis-tutor` (iteratively as data comes in)

**Post-experimentation packaging**:
`/isef-abstract-optimizer` → `/isef-poster-designer`

**Pre-competition**:
`/isef-judging-panel-researcher` → `/science-fair-interview-prep` → `/science-fair-judge` (on finished poster)

**Day-of judging**:
`/science-fair-prep-feedback` (after rehearsal)

**Post-competition continuation**:
`/isef-research-plan-drafter` for Form 7 continuation (next cycle)

## Source-of-truth philosophy

These skills are deliberately built to **avoid hallucinating ISEF rules**. Every form, deadline,
size constraint, or rubric weight is traceable to a specific source document:

- Official ISEF 2026 PDFs (SHA256-verified) via the `isef-research-playbook`:
  `/Volumes/Mac-Mini/workspaces/tian2-edu/Competitions/isef-research-playbook/`
- Official Society for Science webpages: `https://www.societyforscience.org/isef/`
- Official Regeneron ISEF China registration page: `https://www.regeneronisef.org.cn/registration`
- ISEF-Scrape historical projects archive (62,000+ projects 2004–2026)

When sources don't have the information (e.g., individual judge bios pre-event), the skill
**says so honestly** rather than making something up.

## Compatibility with existing scientific skills

Several new skills explicitly wrap or hand off to existing scientific skills in the
`scientific-agent-skills` ecosystem (https://github.com/K-Dense-AI/scientific-agent-skills) or
on the user's local install:

- `/statistical-analysis`, `/exploratory-data-analysis` ← wrapped by `isef-data-analysis-tutor`
- `/scientific-writing` ← handoff from `isef-research-plan-drafter`
- `/scientific-visualization` ← handoff from `isef-data-analysis-tutor`
- `/latex-posters`, `/pptx-posters` ← wrapped by `isef-poster-designer`
- `/literature-review`, `/paper-interpreter` ← handoff from `isef-research-plan-drafter`

If those skills aren't installed, the new skills degrade gracefully — but they're recommended.

## License + contribution

Same CC BY-NC 4.0 license as the rest of the repo.

Contributions welcome — especially for grounding-corrections (a deadline shifts; a form changes;
a rule updates between ISEF cycles). Submit a PR with the updated source citation and the
relevant skill's reference file updated.
