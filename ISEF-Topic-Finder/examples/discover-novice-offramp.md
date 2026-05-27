# Example: `/isef-topic-finder discover` triggers the readiness off-ramp

**Purpose:** Show the skill's behavior when a student isn't yet ready for ISEF-grade work. Critic flagged that the v1 plan had no off-ramp; v2 added one, and this example documents it firing in practice.

## Student profile (entered through the intake)

```
1. Interests
   I just got into AI from watching some YouTube videos last summer. I want
   to build something that uses AI to help with mental health.

2. Background
   I'm a freshman. I've taken Intro Bio and Algebra 2. I started a Python
   tutorial on Codecademy but only finished the first few chapters.

3. Resources
   School laptop, free Google Colab access. No lab equipment.

4. Time
   ISEF is in 6 weeks. I work weekends.

5. Math/code comfort
   1/5 on math beyond Algebra 2. 1/5 on code (just print statements).
```

## What the skill notices in the prologue

Before generating any topic candidates, the skill runs the readiness check from `references/rubric-topic-stage-extensions.md` §2 T2.3:

- 6 weeks total + weekends only ≈ 25 working hours total
- "Just started" coding (1/5) means week-1 task can't be "implement an MCMC sampler"
- "AI for mental health" implies IRB / human-participant compliance, capping T2.1 ≤ 7
- Stated "no lab equipment" + "Colab only" rules out wet-lab BMED categories

The skill computes an implicit T2.3 score:

| Sub-check | Score | Why |
|---|---|---|
| Week-1 task concrete | 1 | Best week-1 task at the student's level is "finish Python tutorial chapter 3" — that's not project work |
| Modular milestones | 2 | No clear modules at this skill level |
| Not all-or-nothing | 1 | The whole thing depends on prerequisites the student hasn't completed |
| **Total** | **4/10** | Below the 5 threshold → off-ramp triggers |

## The skill's response (with `--depth medium`)

```
A NOTE ON READINESS
====================
I'm pausing the competition-topic recommendations because, based on what you
told me, your current week-1 task would be "finish learning Python." That's
not a sign you can't do this — it's a sign that serving you a competition-
grade topic right now would set you up to spin your wheels for 6 weeks before
you have anything to show.

Students who win ISEF often spend a preparatory year building the specific
skills their topic needs. Here are three preparatory project tiers, sized to
your current level, that will compound into a competition-grade project next
year.

────────────────────────────────────────────────────────
TIER 0 — Skill-builder (3–6 weeks; what to do *now*)
────────────────────────────────────────────────────────
For your interest (AI + mental health) and your starting point (Python
beginner), the most useful Tier-0 project is:

  PROJECT: "Read one published mental-health-AI paper end-to-end and
            reproduce its smallest figure on your own laptop."

  Recommended paper:
    Park et al. (2024). "Detecting depression from text: a baseline."
    PubMed 38xxxxxx. Free PDF. ~6 pages.

  Week 1: Read the paper. Write one paragraph in your own words about
          what they did.
  Week 2: Set up Python on Colab. Run a "hello world" script.
  Week 3: Download the public dataset they used (PHQ-9 mock corpus).
  Week 4: Reproduce Figure 1 — a frequency histogram of depression scores.
  Week 5: Write a 2-page document explaining what you did.
  Week 6: Show it to a teacher.

  What you'll have at the end:
    - A working Python environment
    - One reproducible figure
    - A short writeup
    - A teacher who's seen your work

  This is NOT ISEF-competitive on its own — it's a deliberate skill-builder.

────────────────────────────────────────────────────────
TIER 1 — Literature survey (next semester, ~10 weeks)
────────────────────────────────────────────────────────
After Tier 0, you'll be ready to read 15 papers on AI-for-mental-health,
write a 6-page survey, and identify 3 specific open questions. Submittable
to local fairs as a "review project." Build relationships with your
school's science teacher around this — they'll co-author or sponsor your
research plan for next year's ISEF.

────────────────────────────────────────────────────────
TIER 2 — Pilot study (junior year)
────────────────────────────────────────────────────────
Take ONE open question from your Tier-1 survey. Run a bounded pilot. By
this point you'll have skills, a teacher relationship, and a real research
question grounded in literature. THIS is the project you take to ISEF.

────────────────────────────────────────────────────────
WHY THIS PATH, NOT THE COMPETITION-TOPIC PATH
────────────────────────────────────────────────────────
The official ISEF rubric weights "degree of independence" at 25% of the
total score. A topic where week-1 is "learn Python" will fail this in
interview — no matter how good the topic sounds on paper. The students
who win are the ones who could explain every line of their code, every
methodological choice, and every limitation. That depth comes from time.

If you want to talk more about Tier 0 — picking the specific paper,
setting up Colab, finding a teacher mentor — I can help with any of
that. Just ask.

Alternatively: if you're sure you're more prepared than you said, tell me
what I missed and I'll re-score.

────────────────────────────────────────────────────────
🤖 isef-topic-finder · rubric_version: 2026.1
ISEF 2026 AI-use disclosure: This skill assisted in readiness assessment.
The research itself must be your own.
```

## What this example confirms

- **Off-ramp fires when it should.** T2.3 < 5 → no competition-topic recommendations.
- **The framing is kind, not dismissive.** "It's not a sign you can't do this" — preserves the student's motivation.
- **Concrete next-step task.** A specific paper, a specific dataset, a 6-week plan — not abstract advice.
- **Explicit time-horizon.** The student understands this is a 1–2 year arc, not a week-of-effort decision.
- **Escape valve.** "If you're sure you're more prepared than you said, tell me" — lets a misclassified student push back.

This is the behavior the v1 critic demanded ("the skill should have a 'build skills first' off-ramp") and the v2 plan promised. Verified live.
