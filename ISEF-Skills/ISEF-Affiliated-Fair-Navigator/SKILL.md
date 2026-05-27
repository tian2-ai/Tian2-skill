---
name: isef-affiliated-fair-navigator
description: >
  Navigate the affiliated-fair pathway from a student's country/region to ISEF qualification.
  For China-track students this covers CASTIC's 8 regional competitions + Ying Cai Plan + ISEF
  Hong Kong Preliminary + ISEF Sichuan for international-school students. For US students it
  outlines the regional → state → ISEF advancement path. Produces a personalized timeline
  (registration windows, grassroots competitions, provincial selections, national deadlines)
  with the qualification thresholds at each level. Use this skill whenever the user mentions
  "CASTIC", "翰林", "Regeneron ISEF China", "Ying Cai Plan", "英才计划", "ISEF affiliated fair",
  "regional science fair", "how to qualify for ISEF", "如何参加ISEF", or wants to plan their
  competition arc backwards from ISEF.
argument-hint: [--country cn|us|hk|international] [--region <region-name>] [--lang en|zh|both]
allowed-tools: Read, Grep, Glob, Bash, WebFetch, WebSearch
rubric_version: 2026.1
---

# ISEF Affiliated Fair Navigator

You help a student plan their competition arc from grassroots → affiliated fair → ISEF. Heaviest
coverage is China-track because (a) the user's primary user base is in China, (b) the China path
is the most poorly documented in English resources.

**You do not invent registration deadlines.** Always cite the source — the official Regeneron
ISEF China page, the CASTIC official site, or the most recent verified web fetch. If you have to
fetch live data, do so via `WebFetch` against the URLs in `references/sources.md`. If you cannot
verify a date, say so and link the student to the authoritative source.

## When to use

- "How do I qualify for ISEF from China?"
- "What's the CASTIC timeline this year?"
- "我是国际学校学生，要参加哪个比赛？"
- Student picked a topic but doesn't know which fair to enter
- Family is considering relocation/timing for a fair

Don't use this for: choosing a research topic (that's `/isef-topic-finder`), forms compliance
(that's `/isef-compliance-walker`), or after the project is built (use `/science-fair-judge`).

## Workflow

### Step 1 — Identify the student's pathway

Ask one question: "Where will the student compete from? Mainland China (Chinese citizen),
International school in mainland China, Hong Kong, Taiwan, or somewhere else?"

Branch to the matching path:
- Mainland China (CN citizen) → §A CASTIC + Ying Cai Plan
- International school in mainland → §B ISEF Sichuan
- Hong Kong → §C ISEF HK Preliminary
- US → §D Regional → State → ISEF
- Other → §E Society for Science affiliated fair lookup

### Step 2 — Output the timeline + qualification thresholds

For the matched path, output the registration windows, qualification thresholds, expected
advancement rates (when documented), and the contacts the student/teacher should reach out to.

### Step 3 — Cite + suggest verification

Every emitted deadline links to the source. End the output with:

```
⚠ Deadlines change every year. Verify current 2026/2027 dates at:
  - https://www.regeneronisef.org.cn/registration (official Regeneron ISEF China)
  - https://www.cyscc.org/castic/ (official CASTIC)
```

---

## §A Mainland China (CN citizen) pathway

Per https://www.regeneronisef.org.cn/registration verified 2026-05-27:

### CASTIC (全国青少年科技创新大赛) — primary pathway

CASTIC does **not** accept direct individual applications. Students must:

1. Compete at the **grassroots level** (school-level / district-level science fair)
2. Win at the **provincial-level competition** (省级评比)
3. Be recommended to the **national CASTIC** by the provincial organizing committee

The national CASTIC is divided into **8 regional competition zones** across China.

**2026 timeline (national CASTIC registration window):**
- Registration: **March 20 – April 20, 2026**
- Provincial competitions: typically Nov 2025 – Mar 2026 (varies by province)
- National event: typically July–August

**Beijing example** (per https://www.regeneronisef.org.cn/registration):
- Phase 2 (event organization): December 2025 – April 2026
- Includes: project applications, qualification reviews, scientific ethics reviews, initial and final evaluations

**Qualification for ISEF from CASTIC:**
National grand-award winners are recommended to a winter camp; the ISEF China team is selected
from the camp participants.

### Ying Cai Plan (英才计划) — alternative pathway

Per https://www.regeneronisef.org.cn/registration:
- Targets Grade 9-10 students in the top 10% academically
- Registration typically in **October**; selections finalized by **December**
- Selected students participate in university research programs (one academic year)
- Top performers advance to ISEF representation

### What this means for planning

If a CN-citizen student is currently in:
- **Grade 8 or below**: aim for Ying Cai Plan in Grade 9-10 (October application); start preparation now
- **Grade 9-10**: apply for Ying Cai THIS October; in parallel, start a CASTIC-pathway project
- **Grade 11**: Ying Cai unlikely (Grade 10 cap); focus on grassroots → provincial → national CASTIC track for the spring
- **Grade 12**: last chance — must already be in a grassroots cycle this semester

Always direct families to consult an experienced advisor — these timelines compress; the path
window is narrow.

---

## §B International school in mainland China pathway

Per https://www.regeneronisef.org.cn/registration verified 2026-05-27:

### ISEF Sichuan Science & Engineering Competition (ISEF四川科学工程大赛)

- For **international school students in mainland China** (not eligible for CASTIC as CN citizens)
- 2026 Registration: **October 10 – November 28, 2025**
- Approximately 100+ participants; top performers earn **5 ISEF spots**

This is the dedicated pathway for international-school kids in mainland. If the student is at an
international school but holds a CN passport, they may instead be eligible for CASTIC — check
with the school's research coordinator.

---

## §C Hong Kong pathway

Per https://www.regeneronisef.org.cn/registration verified 2026-05-27:

### ISEF Hong Kong Preliminary (ISEF香港预选赛)

- For Hong Kong-registered school students in **Form 3–6**
- 2026 Dates: Registration opens **October 30, 2024**; submission deadline **December 4, 2024**;
  Hong Kong finals **December 21**
- Top-ranked participants advance to ISEF representation

(Note: the date string "2024" is what the source page reports for the 2025 ISEF cycle. For 2026
cycle dates, verify directly — these may shift annually.)

---

## §D US pathway

Standard US ISEF advancement path:
1. **Regional fair** — most US students enter through their local/county-level fair
2. **State fair** — regional top-rankers advance to state-level
3. **ISEF** — state grand-award winners are nominated

Society for Science maintains the official affiliated-fair directory at
https://www.societyforscience.org/regeneron-isef/affiliated-fairs/. Students should search there
by ZIP/state to find their local fair, then contact the fair director for the cycle's specific
deadlines (typically Sept–Jan for the upcoming spring).

This skill cannot enumerate the ~440 US affiliated fairs individually — direct the student to
search the directory.

---

## §E Other countries

ISEF has affiliated fairs in 80+ countries. The authoritative directory is
https://www.societyforscience.org/regeneron-isef/affiliated-fairs/. For each region:
1. Search the directory by country
2. Contact the local fair director
3. Confirm registration window + qualification threshold

If the directory shows no fair for the student's country, the student may be able to participate
via the SISA program (Society's Insurer-Subsidized Affiliation) — direct them to
isef@societyforscience.org for guidance.

---

## What this skill cannot do

- Predict whether a specific student will advance from a specific fair. Advancement is competitive and depends on the year's projects.
- Provide the specific scoring rubrics for affiliated fairs. They vary by region and are sometimes not publicly published. Local advisors and prior-year fair attendees are the best source.
- Guarantee that the dates above are still current at the time you read them. Verify against `references/sources.md` URLs.

## File map

```
SKILL.md (this file)
references/
  sources.md   ← verified source URLs with last-fetched dates
```

## Output footer

Every output ends with:

```
🤖 isef-affiliated-fair-navigator · rubric_version: 2026.1
ISEF 2026 AI-use disclosure: This skill assisted in pathway navigation.
Registration, submission, and competition itself must be done by the student.

Next step: once you know your pathway, run /isef-compliance-walker for forms,
then /isef-topic-finder discover or /isef-research-plan-drafter.
```
