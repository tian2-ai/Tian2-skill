# Readiness Off-Ramp

**Trigger:** T2.3 (learning-curve gradient) < 5/10. The student is not ready for an ISEF-grade project right now. Serving them a competition-grade topic produces failure, not winners.

The off-ramp is **kind and constructive**, not dismissive. Many of the best ISEF projects come from students who took a preparatory year first.

## §1 — How to phrase the off-ramp

Open with the honest framing, then pivot to actionable preparatory tiers. Suggested template:

```
A NOTE ON READINESS
====================
I'm pausing the competition-topic recommendations because, based on what
you told me, your current week-1 task would be "read papers and figure out
where to start." That's not a sign you can't do this — it's a sign that
serving you a PHYS021-level topic right now would set you up to spin your
wheels for 6 weeks before you have anything to show.

Students who win ISEF often spend a preparatory year building the specific
skills their topic needs. Here are three preparatory project tiers, sized
to your current skill level, that will compound into a competition-grade
project next year.
```

Then emit the three tiers below, customized to the student's profile.

## §2 — Tier 0: skill-builder (3–6 weeks)

A bounded project that teaches ONE skill the student will need for ISEF work. Output is a working artifact + a write-up. Not for competition.

Examples by interest area:

| Interest | Skill-builder project (3–6 weeks) |
|----------|------------------------------------|
| Biology | Replicate one published cell-imaging experiment using ImageJ; document protocol and one finding |
| Chemistry | Build a calibration curve for one analytical technique your school owns; write up titration uncertainty analysis |
| Physics | Reproduce one classical experiment with student-made apparatus (e.g., measure g, do a Millikan-oil-drop variant) |
| Math | Pick one Project Euler-style problem; solve it; write a 2-page proof writeup |
| CS/AI | Reproduce one classic paper's smallest result (e.g., MNIST baseline) on a laptop in under 2 hours; document |
| Engineering | Build one device from a tutorial (Arduino weather station, 3D-printed prosthetic finger); document assembly |
| Field/environment | Take 30 days of data on ONE local variable; produce a time-series plot with proper error bars |

**T2.3 lift after Tier 0:** typically 5 → 7. Now ready for Tier 1.

## §3 — Tier 1: literature-survey project (6–10 weeks)

The student reads 15–25 papers in one niche and writes a survey paper (5–8 pages). Often submittable to local fairs as a "review project," not ISEF-competitive but useful preparation.

Outputs:
- A survey paper with proper citations
- A list of 3 open questions the student could pursue next year
- A working bibliography in Zotero or similar

**T2.3 lift after Tier 1:** typically 6 → 8. Now ready for Tier 2.

## §4 — Tier 2: pilot study (10–14 weeks)

A bounded research project — too narrow for ISEF on its own — that produces one concrete finding. The student treats this as a pilot that informs next year's ISEF project.

Example shapes:
- Reproduce one published result on a smaller dataset; report what differs and what doesn't
- Build a measurement tool; use it once; report what the data showed
- Run one local empirical study (per `winner-patterns.md` P7)

**T2.3 lift after Tier 2:** typically 7 → 9. Now ready for next year's ISEF cycle with strong T1.2 (verifiable ownership through the pilot) and T2.3 (clear week-1 task).

## §5 — When to suggest `discover` instead

If T2.3 was capped because the topic the student proposed was too ambitious, not because the student is unprepared, suggest re-running `discover` from their underlying interest:

```
Alternatively: if you're capable but the specific topic you proposed is
too ambitious for the time you have, try `/isef-topic-finder discover`.
I'll find topics sized to your actual constraints.
```

## §6 — When NOT to suggest the off-ramp

Don't trigger the off-ramp if:
- T2.3 < 5 but T1.1 ≥ 25 and T1.2 ≥ 12: this is a *prepared* student with a *too-ambitious* topic. Suggest pivot suggestions instead (per `flow-score.md` §6).
- The student explicitly says they have 18+ weeks: re-evaluate T2.3 with the longer timeline.
- The student is being supervised by a mentor with a documented track record of producing ISEF finalists from novices: T2.3 < 5 may be acceptable in that specific environment.

## §7 — Pedagogical justification

This off-ramp exists because:
- Serving competition-grade topics to under-prepared students produces drop-outs, not winners
- The most reliable path to ISEF success is a preparatory year of skill-building
- The official ISEF rubric heavily weights "degree of independence" (Interview, 25 pts) — a student who couldn't do their own week-1 task will fail this in interview
- Better to have a successful 8-week skill-builder than a failed 14-week ISEF attempt
