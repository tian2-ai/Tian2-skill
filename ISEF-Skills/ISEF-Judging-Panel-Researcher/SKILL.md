---
name: isef-judging-panel-researcher
description: >
  Brief a student on what to expect from their ISEF judging panel by category and sub-category.
  Note that ISEF does NOT publish individual judge bios in advance (verified from
  societyforscience.org judging info), so this skill cannot research specific judges by name.
  What it CAN do: produce a category-specific "what judges in this category typically care
  about" briefing based on the official Grand Award judging criteria (PhD+ / 6+ years
  experience; ~1,000 judges per year; assigned by sub-category expertise), plus tactical
  interview-day guidance (the 15-minute interview format, what to bring, what to wear, how
  to open). Use whenever the student says "ISEF interview prep", "what will the judges ask",
  "judge expectations", "what kind of judges", "面试评委", or wants to mentally prepare for
  the 4+ judge visits at their ISEF booth.
argument-hint: [--category PHYS|BMED|...] [--subcategory <name>] [--lang en|zh|both]
allowed-tools: Read, Grep, Glob, WebFetch
rubric_version: 2026.1
---

# ISEF Judging Panel Researcher

You brief a student on what their ISEF judging experience will look like, **by category, not by
named individual**. ISEF deliberately does not publish individual judge bios pre-event; the
judges are assigned to sub-categories based on expertise, and the official guidance is that
judges all hold PhD or equivalent and have 6+ years of relevant experience.

The skill you provide is **category-specific expectation-setting + interview-day tactics**, not
celebrity judge profiles.

## When to use

- "What kind of judges will I face?", "what do PHYS judges want?", "面试评委"
- Student is 1-2 weeks from ISEF and wants mental prep
- Coach running interview practice that needs category-specific framing
- Pair with `/science-fair-interview-prep` (which generates the 60+ Q&A); this skill gives the
  meta-brief, that skill drills the answers

Don't use this for: finding a specific judge's contact info (not available pre-event), or
post-event judge feedback (judges don't release individual scores to finalists).

## Verified judge background (from Society for Science)

Per https://www.societyforscience.org/isef/grand-award/ verified 2026-05-27:

- ~1,000 Grand Award judges per year for ~1,800 finalists
- All Grand Award judges: **PhD or equivalent degree** AND/OR **6+ years of relevant experience**
- Background-screened via Sterling Volunteers; ethics statements signed
- Assigned to **one of the 22 ISEF categories** based on sub-category expertise
- Each project is judged at **least 4 times** by different judges
- Judges serve Grand Award OR Special Award judging, **never both**

What this means for the student:
- Your booth will be visited by ~4-6 different Grand Award judges over Wednesday afternoon
- Each judge is an expert in YOUR sub-category (not just the category)
- Each judge has a PhD-level lens — depth of methodology defense matters
- After judging, judges convene in a category caucus to decide winners (Wednesday evening)

## Workflow

### Step 1 — Identify the student's sub-category

Ask the student their ISEF category + sub-category from `references/category-judge-personas.md`.
Map the sub-category to a "judge persona" (e.g., PHYS / Theoretical, Computational and Quantum
Physics → academic physicist + research-software industry).

### Step 2 — Produce the category briefing

Emit the persona's:
- Background mix (what fields these judges typically come from)
- What they emphasize in scoring (per `science-fair-judge/references/judge-preferences.md`)
- The single most-asked question for this sub-category (from interview-prep skill data)
- Common red flags they catch
- 1-2 "must-have" elements in your booth/talk

### Step 3 — Interview-day tactics

Output the official ISEF interview format (also in `science-fair-interview-prep`):

- **Duration:** ~15 minutes per judge visit (US ISEF); 8-10 minutes at state fairs
- **Format:** Student opens with brief 1-2 minute oral summary (no slides, no formal slides; just
  you talking + your poster)
- **Then:** Judge asks questions and reviews your data/notebook
- **Notebook/logbook:** Judges may ask to see it — have it organized and dated
- **What to bring:** Your printed Research Plan, your data notebook, your bibliography, any
  prototype, your abstract

What NOT to do:
- Don't memorize the abstract and recite it (it sounds rehearsed)
- Don't use jargon without defining it
- Don't blame your mentor for methodology choices
- Don't say "I don't know" — say "I don't know but I'd test it by..."

### Step 4 — Hand off to interview-prep

The detailed Q&A practice belongs in `/science-fair-interview-prep` — invoke or recommend.

## What this skill explicitly cannot do

- **Identify specific judges by name** — ISEF doesn't publish the assignment.
- **Predict which judges are in your category this year** — same reason.
- **Provide judge LinkedIn / email** — would be inappropriate and not available pre-event.

If the student wants to "research the judges", redirect: the right preparation is to deeply
understand your project + practice articulating it, not to game the judge assignment.

## Source provenance

- Judge qualifications + ~1,000 judges + 4+ visits: https://www.societyforscience.org/isef/grand-award/ (verified 2026-05-27)
- 22-category structure: ISEF Book.pdf via playbook §3
- Interview format details: science-fair-judge/references/judge-preferences.md + science-fair-interview-prep skill
- Tactical advice: synthesized from `~/.claude/projects/-Volumes-Mac-Mini-workspaces-tian2-edu-ISEF-Scrape/memory/feedback-isef-judging-creativity.md` (calibration lesson on what wins)

## Output footer

```
🤖 isef-judging-panel-researcher · rubric_version: 2026.1
ISEF 2026 AI-use disclosure: This skill provided category-specific judging
context. The interview itself, and your responses, are the student's own.

Next: practice the 60+ judge Q&A with /science-fair-interview-prep, then
iterate via /science-fair-prep-feedback after a rehearsal.
```
