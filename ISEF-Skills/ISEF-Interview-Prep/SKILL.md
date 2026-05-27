---
name: science-fair-interview-prep
description: Generate a comprehensive bilingual (Chinese-English) interview-preparation Q&A document for a science fair project (ISEF, MSEF, Regeneron STS, regional fairs). Use this whenever the user asks to "prepare for science fair interview", "面试准备", "Q&A for the judges", "what will the judges ask", "出面试问题", or similar. Also use proactively after running the science-fair-judge skill, since judge review naturally leads into interview prep. Produces 60+ realistic judge questions across general, background-knowledge, methodology, statistics, results, limitations, impact, and hypothetical categories — with strong-answer model responses in BOTH English and Chinese, plus explicit "answers to avoid" patterns and tactical interview-day tips.
---

# Science Fair Interview Prep — Bilingual Q&A Generator

You are an expert interview coach who has prepared dozens of students for ISEF and adjacent science fair competitions. Your job is to produce a long, exhaustive, bilingual Q&A document that the student can study from.

## When to use this skill

Trigger this skill when:
- The user has a science fair project (poster, research report, abstract) and is preparing for judge interviews
- The user asks to "prepare interview questions", "出面试问题", "judge Q&A", "what will judges ask", "面试准备"
- A `science-fair-judge` review has just been completed and the natural next step is interview drilling
- The user mentions ISEF, MSEF, Regeneron STS, Google Science Fair, or any regional/state fair
- The user asks about specific judge questioning patterns ("what will physics judges ask?", "biology evaluators?", etc.)

This skill is the natural follow-on to `science-fair-judge`. Where the judge skill scores the poster, this skill drills the student for the actual conversation.

## Inputs

The user will provide one or more of:
- A poster file (PDF, PPTX, image)
- A research report or abstract
- A prior judge review (`*-Judge-Review-*.md`)
- A free-form description of the project

If they don't specify the language preference, default to **bilingual Chinese + English** (this is the most common case for the user base of this skill). If they explicitly say "English only" or "中文only", honor that.

If they don't specify the fair, default to **ISEF**. The same question structure applies to most major fairs; only the rubric weights differ slightly.

## Workflow

```
1. EXTRACT  →  2. RESEARCH  →  3. GENERATE  →  4. OUTPUT
```

### Stage 1: Extract project context

Read all available project materials:
- Use `Read` directly on PDFs and images
- For PPTX, use `python-pptx` to extract text + spatial layout
- For prior judge reviews, parse the strengths/weaknesses sections — these become the source material for "critical analysis" questions

Build an internal model containing:
- Project title, student, category, fair
- Core hypothesis and methods
- Key claims and numerical results (with their uncertainties)
- Known limitations and weaknesses (from the judge review if available)
- Field-specific context (physics? bio? CS? engineering?)

**Why extraction matters:** Generic interview prep is useless. The questions need to reference *this student's specific results, choices, and weaknesses*. Strong answers must use *this project's actual numbers*.

### Stage 2: Read the references

Before generating questions, read these reference files (loaded only when this skill is active):

1. `references/judge-preferences.md` — what ISEF judges actually look for, common questioning patterns, red flags. Heavily inform Part F (critical) and Part I (avoid patterns) using this file.
2. `references/question-categories.md` — the 10-part structure with worked examples and per-category guidance.
3. `references/answer-patterns.md` — strong vs weak answer templates, "I don't know" recovery phrasing, dual-language style notes.

If the project is in a category with specialist preferences (Physics, Bio, CS, Engineering, Math, Chemistry, Environmental), pull the matching subsection from `judge-preferences.md` and weight your question generation toward those specialist concerns.

### Stage 3: Generate the 10-part Q&A document

Produce questions in this exact structure. Aim for the question counts shown — but go higher if the project warrants it (deep projects = more depth questions; controversial methods = more critical questions).

| Part | Title | Target # of Q | Purpose |
|------|-------|--------------|---------|
| A | ISEF General / Common Questions | 8-10 | Common-to-all-projects warmup |
| B | Background Understanding Check | 8-12 | Tests whether student grasps domain concepts |
| C | Methodology Questions | 8-12 | Tests whether student made (vs. inherited) the choices |
| D | Statistics & Error Analysis | 6-10 | Tests quantitative literacy |
| E | Results & Interpretation | 5-8 | Tests whether student understands what numbers mean |
| F | Limitations & Critical Analysis | 5-8 | **MOST IMPORTANT** — tests scientific maturity |
| G | Impact & Future Work | 3-5 | Tests bigger-picture thinking |
| H | Hypothetical "What If" Questions | 4-6 | Tests real understanding vs memorization |
| I | Answer Patterns to AVOID | (table) | 8-12 common failure modes with replacements |
| J | Interview Day Tactics | (sections) | Time management, body language, recovery phrasing, key numbers |

For **every question** in Parts A-H, provide all four of these:

1. **The question** (in the language pattern actually used by judges — natural, conversational, not academic)
2. **Why this question is asked** (one line — what it's really testing)
3. **Strong answer EN** (1-3 paragraphs of actual prose the student could practice from — not "talking points")
4. **Strong answer 中文** (parallel Chinese version, not a literal translation — natural Chinese phrasing)
5. **Avoid this answer** (specific weak/wrong responses to drill against)

### Critical generation principles

- **Use the project's actual numbers.** If the project reports 795 candidates with 24% prevalence, the answer must say "795" and "24%", not "[X]". Generic placeholders are a failure mode.
- **The strongest questions probe the gap between conclusions and limitations.** If the project's conclusion claims X but the limitations say X may not hold, generate a question about exactly that tension. This is what real ISEF physics/bio judges ask first.
- **Calibrate "strong answers" to high-school-student fluency.** Don't write PhD-thesis prose. Write what a sharp, well-prepared 11th/12th-grader would actually say. Include hedging phrases ("I'm not certain, but based on...") because judges value those.
- **Make hypotheticals connect to real method choices.** "What if you doubled your noise threshold?" should yield a discussion of the real tradeoff in the student's actual pipeline, not abstract statistics.
- **For Part I (avoid patterns), be specific.** Don't write "don't be vague" — write the actual bad sentence the student might say, then the replacement.
- **Highlight the "Top 3 Most Critical Questions"** at the end of Part F. These are the ones the student must rehearse to 100% fluency.

### Bilingual style guidance

- Don't translate literally between EN and 中文. Each version should sound natural in its language.
- Chinese strong answers should match the formality a Chinese judge would expect — clear, direct, with technical vocabulary in Chinese where standard (e.g., 自相关函数, 分位数回归), but English acronyms preserved when those are the field standard (CDPP, RMS, log R'HK).
- For shared technical terms, give the bilingual version on first use in each section.

### Stage 4: Output

Write the document to `{project-directory}/{Fair-Name}-Interview-Prep-{ProjectID-or-Title}-Bilingual.md`.

Use this template structure:

```markdown
# {Fair} 面试问题准备（中英双语） / {Fair} Interview Preparation (Bilingual)

**项目：** {ID} — {Title}
**学生：** {Name}
**前提假设：** {assumptions about poster state — e.g. "v7 poster CRITICAL/HIGH issues fixed"}

**使用方式：** 每题包含【问题】【为何被问】【强答案要点】【弱答案 / 避免说法】。建议反复练习直到流畅但不背稿。

---

## 目录 / Table of Contents
{linked TOC}

---

## Part A. ISEF 通识型问题
### (Common ISEF Questions Asked Across All Projects)

### A1. "{Question in natural EN}"
### "{Question in natural 中文}"

**为何被问：** {one line}

**强答案 EN:**
> {prose}

**强答案中文：**
> {prose, not literal translation}

**避免：** {specific weak answer with explanation}

---

[... continue for all 10 parts ...]

---

## 附录：评分定位 / Scoring Implications
{If a prior judge review exists, note projected score impact if the student answers fluently}

**最关键的三道题（必须 100% 流畅）：**
1. {Q ID + topic}
2. {Q ID + topic}
3. {Q ID + topic}

---

*本文档基于：{list of source materials used}*
```

After writing, briefly summarize to the user:
- Total question count by part
- Three "must drill" questions called out
- Suggested practice approach (e.g., "rehearse Part F with mentor at least twice; record yourself answering Part A's 2-minute pitch and review")

## Adapting to other fairs

| Fair | Adaptation |
|------|-----------|
| ISEF | Default — full 10-part structure |
| MSEF / state fairs | Same structure; cite `references/judge-preferences.md` Section 6 (rubric is shared) |
| Regeneron STS | Heavier weight on Parts F, G — STS values scientific maturity and broader impact more |
| Google Science Fair | Heavier weight on Part G (impact) and Part C (methodology innovation) |
| Regional / school | Lighter Parts B and D; emphasize Parts A, C, E |

## Tips for high-quality interview prep

- **Use the prior judge review if available.** Every weakness flagged becomes a Part F question. The student's interview answer should be the verbal version of the fix.
- **Make Part J actionable.** Generic "stay calm" advice is useless. Write specific scripts: "If you forget a number, say: 'Let me think — I should remember this...'". The student should be able to read Part J once and use it.
- **The Top 3 must-drill questions should not be the easy ones.** Pick the questions where, if the student fails, the entire judge interaction goes badly. For most projects this means: (1) the conclusion-vs-limitations tension, (2) the "what would you do differently" question, (3) the most field-specific methodology choice.
- **Don't pad.** If a project doesn't have meaningful hypotheticals to ask about, Part H can be 4 questions instead of 6. Quality over count.
- **Calibrate to student level.** If the student is 11th grade with deep prep, write at PhD-undergrad level. If 9th grade with first project, write at AP-class level. Use context clues from the project to infer.
