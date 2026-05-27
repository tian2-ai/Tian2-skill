# ISEF Topic Finder: the AI that tells you whether your science fair idea will actually win

Your kid has a science fair idea. You read it. It sounds smart. But you have no idea whether it's the kind of thing that wins ISEF, or the kind of thing that quietly places "honorable mention" while a tenth-grader from Texas walks off with the grand award for re-folding origami into a statistical mechanics problem.

This is the skill that tells you the difference.

---

## What it actually does in 30 seconds

You install it into Claude Code. You type one of two commands.

`/isef-topic-finder discover` walks your student through five questions about what excites them, what they know, what they have access to, how much time they have, and how comfortable they are with math and code. Then it suggests two or three ISEF categories that fit, generates topic candidates, and scores each one against a rubric that knows what wins.

`/isef-topic-finder score "my project idea"` takes a topic the student already has, runs it through the same rubric, and tells you where it's strong, where it's weak, and what to pivot on.

Both modes end with a score range, a confidence band, and a list of citations that prove the rubric isn't making things up.

---

## Who this is for

The Chinese high schooler whose mentor has handed them a "safe" project that will compete, but will not win.

The parent who can read the abstract and the methodology and still has no way to tell if the project is genuinely creative or just polished.

The teacher running a science research class with thirty students, who cannot personally vet each topic against the latest literature.

The student who has a real spark of an idea but doesn't know whether it's been done forty times already.

---

## Three things it does that nothing else does

**It weights creativity over rigor.** Most "is this a good project" rubrics reward bigger datasets, more sophisticated methods, more impressive instruments. This one doesn't. The ISEF judge who decides the grand award is looking for the project that made them sit up and think "I haven't seen that before." This skill is calibrated for that, not for the project that looks like a grad-school paper.

**It cross-validates against five real research sources.** OpenAlex for trend data. PubMed and bioRxiv for life-sci freshness. arXiv for physics, math, CS, robotics. A local index of 62,000 actual ISEF projects from 2004 through 2026 for pattern matching. The skill won't tell you a topic is novel because of a vibe. It tells you a topic is in the 17th percentile of papers-per-year within its category, with four preprints in the last six months on adjacent work, and no structurally similar ISEF winner in the last five years. That's evidence, not opinion.

**It refuses to overpromise.** If two of the five research sources are unreachable, the skill widens the score range and tells you the confidence is low. If the topic involves human subjects, it caps the feasibility score because IRB approval is a real time tax. If the student isn't ready, the skill walks them onto a preparatory tier and says so honestly. There is no tier label like "grand award contender" until the rubric has been back-tested against real winners — the calibration honesty is built into the math.

---

## The two best things to ask it

If your student already has an idea, try this:

> /isef-topic-finder score "applying graph theory to the metabolic networks of extremophile bacteria"

You'll get a score range, a per-dimension breakdown, three real anchor citations, and two or three pivots to lift whichever dimension is weakest.

If your student is still exploring, try this:

> /isef-topic-finder discover

It will run the five-question intake and walk them through category fit and topic candidates. Setting `--depth heavy` produces a full project sketch including a twelve-week timeline and the ISEF forms they'll need. Setting `--lang both` outputs bilingual English-Chinese, useful for the CASTIC pipeline.

---

## What the score actually means

A range of 80 to 95 with high confidence means the topic has the structural shape of past grand-award contenders. A range of 60 to 75 means it's solid but needs a sharper hook. A range below 55 means pivot. A range with low confidence means too few sources reached — the skill is telling you it doesn't know enough to commit.

The skill also surfaces compliance flags, which is to say if your topic mentions humans or animals or hazardous chemicals, it tells you which ISEF forms you'll need and which review boards will gate your timeline. This alone saves weeks of confusion.

---

## What it deliberately doesn't do

It doesn't write the abstract for you. It doesn't draft the research plan. It doesn't generate code for the project. It doesn't promise wins. It is a topic scout, not a project ghostwriter. ISEF 2026 has explicit AI-use disclosure requirements, and every output of this skill ends with a reminder that the research itself must be the student's own.

It also doesn't replace `science-fair-judge`, which is the sibling skill that evaluates a finished poster. Topic Finder ends where a poster begins.

---

## What's under the hood

The rubric has six tiered dimensions: creativity, verifiable student ownership, cross-disciplinary legibility, resource feasibility, high-school curriculum fit, and learning-curve gradient. Four modulators adjust the score: trend velocity, accessibility signal, preprint freshness, and prior-winner alignment. The last one is inverted — it penalizes you for looking too much like a recent winner in the same category, because copying past winners is the opposite of what judges reward.

There's a hypothesis gate that refuses to score a topic until the student can state, in one sentence, what would prove their hypothesis wrong. If they can't, the skill explains that what they have is a research interest, not a research project, and helps them sharpen it.

There's a readiness off-ramp. If the student is a freshman who has six weeks and one Python tutorial under their belt, the skill won't pretend they're ready for a competition-grade topic. It will recommend a preparatory skill-builder project instead, sized to their actual level. This is harder to write than it sounds. Most tools tell every student they can do anything. This one tells the truth.

---

## How to install

The skill lives at `~/.claude/skills/isef-topic-finder/` and auto-discovers in Claude Code. The repo also packages the three sibling skills (Judge, Interview Prep, Prep Feedback) and a brainstorm document of further ISEF skills that could be built next.

If you've ever found yourself looking at a high schooler's project idea and wishing someone with a PhD and a deep knowledge of fifteen years of ISEF history could just look at it and tell you whether it's worth the year of work — this is that.
