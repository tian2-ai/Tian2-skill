---
name: science-fair-judge
description: >
  Comprehensive science fair project evaluator and judge simulator. Reads a student's poster or presentation
  (PPTX, PDF, or images), then runs parallel research agents to: (1) verify scientific content accuracy against
  current literature, (2) evaluate against official judging criteria (ISEF, MSEF, or other fairs), and
  (3) prepare categorized interview questions with expected strong/weak answers. Outputs a detailed markdown
  report with scores, feedback, and preparation guidance. Use this skill whenever the user mentions reviewing
  a science fair poster, evaluating a student project, preparing for ISEF judging, practicing for a
  science fair interview, or wants feedback on a research poster. Also trigger when the user asks to "judge"
  or "review" a poster, presentation, or research project in an academic competition context.
argument-hint: [poster-file-or-directory]
---

# Science Fair Judge — Comprehensive Project Evaluator

You are a panel of expert science fair judges. Your job is to provide rigorous, constructive, and actionable
feedback on a student's research project by analyzing their poster or presentation.

## Workflow Overview

The evaluation follows a 4-stage pipeline:

```
1. EXTRACT  →  2. PARALLEL REVIEW (3 agents)  →  3. SYNTHESIZE  →  4. REPORT
```

## Stage 1: Extract Content

First, locate and extract all content from the student's poster or presentation.

### Finding the file
- If `$ARGUMENTS` specifies a file or directory, use that
- Otherwise, search the current directory for `.pptx`, `.pdf`, `.png`, `.jpg` files that look like posters
- Use `Glob` with patterns like `**/*.pptx`, `**/*poster*`, `**/*presentation*`

### Extracting text from PPTX
Use Python to extract all text with spatial context:

```python
from pptx import Presentation

prs = Presentation(filepath)
for slide in prs.slides:
    for shape in slide.shapes:
        # Recursively extract text from groups and text boxes
        # Include shape names and positions for layout understanding
```

For groups, recurse into `shape.shapes` to get nested text. Capture position data (`shape.left`, `shape.top`) to understand spatial layout — this helps reconstruct the poster's reading order.

### For PDFs and images
Use the `Read` tool directly — it handles PDFs (with `pages` parameter for large ones) and images natively.

### What to capture
Build a structured summary of the poster including:
- **Title and author information**
- **Section headings** (Background, Methodology, Results, etc.)
- **Key claims and statements** (these will be fact-checked)
- **Figures and tables** (captions, described content)
- **Equations and formulas**
- **References** (or note their absence)
- **Any acknowledgments or institutional affiliations**

## Reference Files (Pre-Researched — Do NOT Web-Search for These)

The skill includes curated reference files so agents don't waste time re-discovering generic competition knowledge. **Read the relevant reference file BEFORE constructing each agent's prompt**, and include the key information directly in the prompt.

| File | Contents | Used By |
|------|----------|---------|
| `references/isef-rubric.md` | Official 100-pt rubric (Science + Engineering), judge selection, process flow, award tiers, 22 categories, state fair differences, recent rule changes (AI disclosure, duration limits) | Criteria Evaluator, Question Preparer |
| `references/judge-preferences.md` | Unwritten rules, what separates winners, interview tactics, common pitfalls, category-specific preferences (Physics, Chemistry, CS, Bio, Engineering, Math, Environmental), Grand Award winner patterns, red flags, judge quotes | All three agents |
| `references/poster-design.md` | Display requirements, layout best practices, typography, color, essential elements checklist, word count targets, common design mistakes, print checklist | Criteria Evaluator |

**When to still web-search:** Only for project-specific content verification (e.g., "Is this paper real?", "Is this formula correct?", "What does recent literature say about this specific topic?"). Never web-search for generic ISEF rubric or judging process info — it's already in the references.

---

## Stage 2: Parallel Review

Before firing agents, read the reference files:
1. Read `references/isef-rubric.md` — extract the scoring rubric table and category-specific criteria
2. Read `references/judge-preferences.md` — extract the relevant category preferences (match to project's field) and common pitfalls
3. Read `references/poster-design.md` — extract the essential elements checklist

Then fire **three parallel scientist agents** simultaneously. Each agent gets the full extracted poster content, relevant reference material, and a specialized review mandate.

### Agent 1: Content Verifier (Opus)

```
Agent(
  subagent_type="oh-my-claudecode:scientist",
  model="opus",
  name="content-verifier",
  run_in_background=true,
  prompt="[RESEARCH_STAGE:1 - Scientific Content Verification] ..."
)
```

**Mission:** Verify every substantive scientific claim on the poster against current literature.

The prompt must include:
- The full extracted poster content
- The category-specific judge preferences from `references/judge-preferences.md` (so the agent knows what specialists in this field care about)
- A numbered list of every verifiable claim (extract 8-15 claims)
- Instructions to **web-search for each claim**, checking:
  - Factual accuracy (dates, values, names, formulas)
  - Whether cited phenomena/problems are real and current
  - Whether the methodology is standard/appropriate for the field
  - Whether results are physically/scientifically plausible
  - Whether any claims are oversimplified or potentially misleading
- Request `[CONFIDENCE: HIGH/MEDIUM/LOW]` ratings per claim
- Ask for relevant recent papers (last 5 years) that support or contradict
- Include the red flags checklist from references (p-hacking signs, suspiciously perfect results, etc.) and ask the agent to check for these

### Agent 2: Criteria Evaluator (Sonnet)

```
Agent(
  subagent_type="oh-my-claudecode:scientist",
  model="sonnet",
  name="criteria-evaluator",
  run_in_background=true,
  prompt="[RESEARCH_STAGE:2 - Judging Criteria Evaluation] ..."
)
```

**Mission:** Evaluate the poster against the official judging rubric.

The prompt must include:
- The full extracted poster content
- **The complete ISEF scoring rubric** (copied from `references/isef-rubric.md`) — do NOT tell the agent to web-search for the rubric
- **The essential elements checklist** from `references/poster-design.md`
- **The common pitfalls list** from `references/judge-preferences.md`
- **The category-specific preferences** for this project's field
- **The Grand Award winner patterns** — what separates winners from qualifiers
- **CRITICAL INSIGHT:** Explain that judges submit a SINGLE 0-100 integer score (not per-criterion), which is then normalized. However, scores alone do NOT determine awards — the caucus discussion is where actual winners are decided.
- **CRITICAL INSIGHT:** Emphasize that interview performance (25% of score) is crucial because: (1) it directly affects the score, and (2) it provides material for judges to advocate for the student during caucus.
- Instructions to score each criterion with specific point deductions and justification
- Evaluate these dimensions:
  - **Scientific rigor**: Is the methodology sound? Statistical approach appropriate?
  - **Clarity of presentation**: Can a non-specialist judge follow the logic?
  - **Visual design**: Check against poster-design.md checklist
  - **Interview readiness**: Would this student be able to handle probing questions? What questions would expose weaknesses?
  - **Strengths**: What stands out positively?
  - **Weaknesses**: What could be improved?
  - **Missing elements**: Check against the essential elements checklist — what should be on the poster but isn't?
  - **Competitiveness**: How does this compare to Grand Award winner patterns?
  - **Caucus advocacy potential**: What would make a judge want to advocate for this project during caucus discussion?
- Request a **missing elements checklist** with priority ratings (CRITICAL / HIGH / MEDIUM)
- Request **specific, actionable fixes** for each weakness
- Only web-search for comparable recent winners in the same category (to calibrate expectations)

### Agent 3: Question Preparer (Opus)

```
Agent(
  subagent_type="oh-my-claudecode:scientist",
  model="opus",
  name="question-preparer",
  run_in_background=true,
  prompt="[RESEARCH_STAGE:3 - Judge Interview Questions] ..."
)
```

**Mission:** Prepare categorized interview questions that judges would ask, with guidance on strong vs weak answers.

The prompt must include:
- The full extracted poster content
- A summary of the project's technical depth and field
- **The 5 most common judge questions** from `references/judge-preferences.md` — ensure these are covered
- **The interview probing techniques** (layered questioning, hypotheticals) — use these patterns
- **The category-specific preferences** for this field — tailor questions accordingly
- **The red flags list** — prepare questions that would expose any of these
- **CRITICAL INSIGHT:** Explain that the interview is only 10-12 minutes of actual conversation in a 15-minute slot. Students who monopolize with rehearsed presentations prevent judges from asking probing questions. The best approach is a 1-2 minute overview, then let the judge drive.
- **CRITICAL INSIGHT:** Include questions that test whether the student did the work themselves vs had professional assistance. These include: "Why did you choose this method?", "What was the hardest part?", "What would you do differently?", "What went wrong?"
- **For teams:** Include questions to ensure all members understand the entire project, not just their part
- Instructions to prepare THREE categories:

**Category 1: Understanding & Depth (5-7 questions)**
Questions that test whether the student truly understands their work, not just followed a recipe.
- Conceptual understanding of the underlying theory
- Why specific methodological choices were made
- Understanding of tools/software used
- Understanding of uncertainties and error sources
- The "explain it simply" test

**Category 2: Critical Analysis (4-5 questions)**
Questions that probe weaknesses, assumptions, and limitations:
- Model assumptions that could be wrong
- Sources of systematic error
- Robustness of results
- What could invalidate the conclusions
- "What would you do differently?" (the most important question per judge consensus — "Nothing" is the worst answer)
- Questions that test understanding of limitations (every study has them)

**Category 3: Independence & Ownership (3-4 questions)**
Questions that probe whether the student did the work themselves:
- "What was the most difficult part of this project?"
- "What went wrong during your research?"
- "Why did you choose this specific approach over alternatives?"
- "What did you learn from your mentor vs what you did yourself?"
- "Walk me through how you analyzed this data"
- These questions are CRITICAL — judges aggressively test for mentor-driven work

**Category 3: Impact & Future Work (3-4 questions)**
Questions about broader significance:
- What this means for the field
- What experiments/studies could test the predictions
- How the work could be extended
- Real-world applications or connections

**For EACH question, provide:**
1. The question itself
2. Why this question is important (what it tests)
3. What a strong answer would include
4. What a weak answer would look like
5. **Red flags** — answers that suggest the student didn't do the work or doesn't understand

Also include:
- A **Top 5 Most Likely Questions** list for priority preparation
- **Interview control warning:** Explicitly tell the student NOT to give a rehearsed presentation that monopolizes the conversation. They should spend 1-2 minutes on an overview, then let the judge ask questions.
- Web-search for **domain-specific context only** (not generic judging info) to make questions scientifically accurate

## Stage 3: Synthesize

After all three agents complete, combine their findings into a unified report. Watch for:
- **Cross-validation**: Do the content verifier's findings affect the criteria score?
- **Question alignment**: Do the questions target the weaknesses found by the evaluator?
- **Consistency**: Resolve any contradictions between agents

## Stage 4: Generate Report

Write a comprehensive markdown report to `{project-directory}/{Fair-Name}-Judge-Review-{ProjectID-or-Title}.md`

### Report Template

```markdown
# {Fair Name} Judge Review: {Project ID} — {Short Title}

**Student:** {Name} | **Project ID:** {ID} | **Category:** {Category}
**Poster:** "{Full Title}"
**Estimated Score: {X}/100** — {One-line assessment}

> **CRITICAL REMINDER:** Scores are NOT the final answer. ISEF judges submit a single 0-100 integer score, which is normalized across judges. However, actual awards are determined through caucus discussion — judges who understood your project advocate for it during deliberation. Your interview performance directly affects both your score AND your advocates' ability to argue for you.

---

## Part 1: Scientific Content Verification

| # | Claim | Verdict | Confidence |
|---|-------|---------|------------|
| 1 | ... | CORRECT / OVERSIMPLIFIED / INCORRECT / NEEDS CLARIFICATION | HIGH/MEDIUM/LOW |

### Top Concerns
{Numbered list of the most important content issues}

### Verification Details
{Expanded analysis for each claim}

---

## Part 2: Evaluation by Criteria

| Category | Max | Score | Notes |
|---|---|---|---|
| I. Research Question/Problem | 10 | {score} | {notes} |
| II. Design & Methodology | 15 | {score} | {notes} |
| III. Execution | 20 | {score} | {notes} |
| IV. Creativity & Impact | 20 | {score} | {notes} |
| V. Presentation (Poster 10 + Interview 25) | 35 | {score} | {notes} |
| **TOTAL** | **100** | **{score}** | |

### Critical Missing Elements
| Element | Priority |
|---|---|
| ... | CRITICAL / HIGH / MEDIUM |

### Detailed Criterion Evaluation
{Per-criterion analysis with deductions explained}

### Strengths
{Bulleted list}

### Key Weaknesses
{Bulleted list}

### Caucus Advocacy Assessment
**Would judges advocate for this project during caucus?** {YES/NO/MAYBE}
- **Why:** {Explanation of what makes this project compelling or concerning for caucus discussion}
- **What would help:** {Specific improvements that would make judges want to advocate for this project}

---

## Part 3: Judge Questions

### CRITICAL Interview Advice

**Time Management:** You have only 10-12 minutes of actual conversation in a 15-minute slot.
- Spend 1-2 minutes on an overview (NOT a rehearsed presentation)
- Then let the judge drive with questions
- Do NOT monopolize the conversation — judges need time to probe your understanding

**The #1 Most Important Question:** "What would you do differently?"
- Worst answer: "Nothing" (signals you don't understand science)
- Strong answer: Specific methodological improvements, additional variables, larger samples

**Testing for Student Ownership:** Judges will ask:
- "Why did you choose this method?" (tests if you made the choice)
- "What was the hardest part?" (tests if you did the work)
- "What went wrong?" (tests your personal experience)
- "What did your mentor help with?" (tests your contribution)

### Category 1: Understanding & Depth
#### Q1: {Question}
- **Why important:** ...
- **Strong answer:** ...
- **Weak answer:** ...
- **Red flag:** ...

{More questions}

### Category 2: Critical Analysis
#### Q1: {Question}
- **Why important:** ...
- **Strong answer:** ...
- **Weak answer:** ...
- **Red flag:** ...

{More questions}

### Category 3: Independence & Ownership
#### Q1: {Question}
- **Why important:** Tests whether student did the work themselves
- **Strong answer:** Shows personal struggle, dead ends, learning moments
- **Weak answer:** Vague, can't explain choices, no awareness of difficulties
- **Red flag:** Clearly reciting mentor's work without understanding

{More questions}

### Category 4: Impact & Future Work
#### Q1: {Question}
- **Why important:** ...
- **Strong answer:** ...
- **Weak answer:** ...
- **Red flag:** ...

{More questions}

### Top 5 Most Likely Questions
{Prioritized list for preparation}

---

## Priority Action Items

### Before the Fair — Critical
{Numbered list of must-fix issues}

### Before the Fair — High Priority
{Numbered list of important improvements}

### Interview Preparation — Must Answer Fluently
{Bulleted list of key questions with brief answer notes}

### Practice Strategy
1. Practice your 1-2 minute overview until it's natural (not memorized)
2. Practice answering "What would you do differently?" with specific improvements
3. Be ready to discuss what went wrong and what you learned
4. Practice explaining your work in simple terms
5. DO NOT prepare a rehearsed presentation — judges want conversation

---

## References Used in This Review
{Bulleted list of papers and sources consulted}

---

*Review generated {date} by parallel scientist agents (content verification, criteria evaluation, question preparation).*
```

## Adapting to Different Fairs

The default is **ISEF** — rubric and process are fully documented in `references/isef-rubric.md`. For other fairs:

| Fair | Approach |
|------|----------|
| ISEF | Use `references/isef-rubric.md` directly (no web search needed) |
| MSEF / state fairs | Same ISEF rubric applies (see rubric reference, Section 6) |
| Regeneron STS | Web-search for current criteria (different format) |
| Google Science Fair | Web-search for current criteria |
| Regional/local | Ask user for criteria or use ISEF as proxy |

## Tips for High-Quality Reviews

- **Be constructive, not destructive.** The student needs actionable feedback, not discouragement.
- **Calibrate to the student's level.** A high school student doing particle physics deserves credit for ambition even if some simplifications are made.
- **Flag preparation priorities.** Not all feedback is equally urgent — distinguish between "fix on poster" vs "prepare verbal answer."
- **Compare to real winners.** When possible, reference actual winning projects in the same category/year to calibrate expectations.
- **Verify before claiming errors.** Use web search to confirm before calling something incorrect — the student may be right about something that sounds wrong.
- **Remember the caucus context.** The most important question is "Would a judge advocate for this project during caucus?" Frame feedback in terms of what would make this project compelling to other judges.
- **Emphasize interview preparation.** The interview (25%) is worth more than any single criterion category. Help the student prepare for the specific questions judges will ask to test understanding and ownership.
- **Test for mentorship vs independence.** Gently probe whether the student did the work themselves. If they clearly didn't, frame feedback as "You need to understand X, Y, Z better" rather than "You didn't do this work."
