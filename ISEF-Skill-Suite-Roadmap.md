# ISEF Skill Suite — what exists, what's next

This is a map of Claude Code skills that help a high-school student through the full ISEF arc. It documents what's already built, what's partly built, and where the highest-leverage future skills could go.

---

## The student journey

A typical competitive ISEF project is a 12 to 18-month arc. The student picks a topic, drafts a research plan, gets compliance approvals, runs experiments, analyzes data, writes an abstract, builds a poster, prepares for interviews, competes at regional and state fairs, and (if they advance) at ISEF itself. Each step has its own failure modes and its own skill-shaped opportunities.

```
   topic    research    compliance    experiment    analysis    abstract    poster    interview    fair    next-year
   choice    plan        + IRB                                                                    day      continuation
     │         │           │              │             │           │          │          │           │           │
     ▼         ▼           ▼              ▼             ▼           ▼          ▼          ▼           ▼           ▼
  [TOPIC-                                                                              [INTERVIEW
   FINDER]                                                                            -PREP /PREP-FEEDBACK]   [JUDGE]
                                                                                                    ▲
                                                                                                    │
                                                                                              works on final
                                                                                              poster + practice
```

---

## What exists

### isef-topic-finder

Helps a student pick a topic that has a defensible probability of winning. Two modes (`discover` from interests; `score` an existing topic). Cross-validates against OpenAlex, PubMed, bioRxiv, arXiv, and a local index of 62k+ ISEF projects. Has a hypothesis-articulation gate and a readiness off-ramp. Ships score-as-range with explicit confidence bands until back-testing validates tier labels.

### science-fair-judge

Evaluates a finished poster or presentation. Reads PPTX, PDF, or images. Runs parallel agents to fact-check content, evaluate against the official ISEF rubric, and generate categorized interview questions. Outputs a detailed report.

### science-fair-interview-prep

Generates a 60+ question bilingual (English-Chinese) Q&A document covering background knowledge, methodology, statistics, results, limitations, impact, and hypothetical questions. Includes strong-answer models and patterns to avoid.

### science-fair-prep-feedback

The second-pass companion to interview-prep. Consumes the student's annotated version of the prep document and produces tactical question-by-question responses to their factual corrections, proposed rewrites, anxieties, and additions.

---

## What's missing — high-leverage opportunities

### isef-compliance-walker (new)

The forms maze is the single largest non-research bottleneck. A student with a vertebrate animal project faces Form 1, 1A, 1B, 2, 5A or 5B, possibly 3, possibly 7 — plus SRC or IACUC pre-approval, plus the Research Plan, plus the Adult Sponsor and Qualified Scientist signatures. The compliance-form-decision-tree in the isef-research-playbook captures the trigger matrix, but it's a 380-line document. A skill that walks a student through a structured intake ("any humans? any animals? any tissue? any hazardous materials?") and produces a personalized form checklist with deadlines, approval bodies, and the specific signatures needed would save weeks. Bonus: surface the BSL-1 / BSL-2 checklist when relevant; surface the Field Work Safety Plan when relevant. This is mostly a structured walk through documented rules — a skill that's high-impact, medium-effort.

### isef-research-plan-drafter (new)

The Research Plan / Project Summary is the document that drives every approval. It has a specific structure (rationale, research questions, materials, methodology, procedures, risk assessment, bibliography) and must be written before experimentation. Students often write it as an afterthought, then have to revise after the SRC rejects it. A skill that takes a topic + hypothesis (from topic-finder) and drafts the Research Plan in the required format, with prompts for each section and a critique pass — this would compress a typical 2-week struggle into 2 days. Critical to do this without writing the science for the student; the skill should structure their thinking, not replace it.

### isef-data-analysis-tutor (new)

Once experiments produce data, students often fall into one of two failure modes: under-analyzing (just a bar chart and a mean) or over-analyzing (deep-learning a 30-sample dataset). A skill that takes their dataset, infers what tests are appropriate for the design (paired t-test vs. ANOVA vs. non-parametric), runs them, produces publication-quality figures, and writes a methods-section paragraph would lift the rigor floor. Has to be deeply tied to the rubric's T1.3 legibility: judges should be able to grasp the analysis in 6 minutes.

### isef-affiliated-fair-navigator (new for China-track)

ISEF requires entry through an affiliated fair. For Chinese students, that means CASTIC + one of four regional fairs (北京, 上海, 武汉, 重庆). Each fair has different deadlines, different supplementary requirements, different judge cultures. A skill that takes the student's location and category and outputs a personalized timeline — when to register for which fair, what the local SRC expects beyond the ISEF baseline, what the historical advancement rate looks like by category — would be invaluable for the CASTIC pipeline. Most US-centric resources don't cover this.

### isef-abstract-optimizer (new)

The official ISEF abstract is 250 words maximum, one page, must be SRC-approved, and is what judges read first. Students typically over-pack it with methods and under-emphasize impact. A skill that takes a draft abstract and applies the structural critique used by Society for Science abstract reviewers (purpose → method → results → significance, with the impact statement load-bearing) would lift the poster-judging score (worth 10 points out of 100 in the official rubric). Could share the bilingual capability with interview-prep.

### isef-poster-designer (new — distinct from science-fair-judge)

Judge evaluates a finished poster. There's room for a sibling skill that helps design the poster from scratch — typography hierarchy, figure placement, the 6-minute reading test, the booth-footprint constraints from DS-Rules.pdf (76×122×240 cm; LED-only lighting; no Class 3B+ lasers). Could integrate with the existing latex-posters skill or pptx-posters skill to produce print-ready files. Critic of the poster goes to science-fair-judge; designer of the poster is missing.

### isef-mentor-finder (new — risky but high-impact)

Many ISEF projects benefit from a mentor at a university or industry lab. Finding one is a closed-network problem — students with parents in academia have a huge advantage; students without don't. A skill that takes a topic, finds matching faculty via OpenAlex affiliations, identifies which are listed on departmental "available for mentorship" pages, and drafts personalized outreach emails would democratize access. This needs careful design to avoid feeling spammy or to give kids without academic networks the same shot as those with one. Worth doing carefully.

### isef-judging-panel-researcher (new — strategy-tier)

ISEF assigns finalists to category teams of 4+ judges. Judge bios are published. A skill that takes the student's category, finds the published judge list for their fair (regional, state, or ISEF), researches each judge's background (PhD field, current role, recent publications), and produces a "what each judge will likely care about" briefing — this is what professional debate teams do. For ISEF interview prep, knowing whether the judge across from you is a biophysicist or a clinical pathologist changes which framing of your project lands. Probably most useful in the 48 hours before judging day.

### isef-continuation-strategist (new — for returning students)

Form 7 lets a student continue a previous project. The continuation rules are subtle: the project must demonstrate meaningful progression, not just re-running last year's experiment with more data. A skill that reads last year's abstract and Research Plan and helps the student articulate what's genuinely new versus what's iterative — this would help advancing students avoid the common trap of "I did more of the same and they rejected me."

---

## Medium-leverage future skills

- **isef-logbook-organizer** — converts a student's scattered Notion / Google Doc lab notes into a properly-dated lab notebook that judges respect. Probably a Notion or Obsidian integration.
- **isef-budget-planner** — most ISEF-track schools don't fund research. A skill that estimates project budget, identifies grants (Davidson, Society for Science, regional STEM funds), and drafts grant applications.
- **isef-presentation-practice** — voice-based interview rehearsal. The student practices answering judge questions; the skill scores delivery (pacing, filler words, confidence, technical accuracy) and gives feedback. Probably a tmux + voice-call skill integration.
- **isef-photo-and-figure-cleaner** — many poster figures are screenshot-quality. A skill that takes raw figures and outputs print-ready 300-dpi vector or hi-res PNGs, with consistent typography.

---

## Lower-leverage but pleasant skills

- **isef-affiliate-deadline-tracker** — calendar integration for fair deadlines.
- **isef-team-coordination** — for 2-3 student teams: divide labor, track contributions, prepare for the "what did each member do" interview question.
- **isef-press-release-drafter** — for students who advance, drafts a press release for their school / local paper / college applications.

---

## What I'd build next, if I were the user

In rough priority:

1. **isef-compliance-walker** — highest impact per hour of work; rules are documented; saves real weeks of student frustration.
2. **isef-affiliated-fair-navigator (China-track)** — high impact for the CASTIC pipeline; underserved by US-centric resources.
3. **isef-research-plan-drafter** — natural downstream of isef-topic-finder; closes the loop from idea to approval.
4. **isef-abstract-optimizer** — small surface, high leverage; lifts the 10-point poster score with relatively little code.
5. **isef-judging-panel-researcher** — strategy-tier; most useful 48 hours before judging.

The other skills are valuable but lower-priority. Build what serves the specific bottleneck in front of you.
