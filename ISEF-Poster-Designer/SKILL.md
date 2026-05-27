---
name: isef-poster-designer
description: >
  Design and produce a printable, easy-to-edit ISEF poster fitted to the official booth
  constraints (max 76×122×240 cm per DS-Rules.pdf, so poster max ~122 cm wide). Provides
  two parallel templates the student can edit and print: (1) LaTeX (tikzposter or beamerposter)
  for typography-heavy projects with equations, (2) PowerPoint (A0 metric or 48×36 inch) for
  most students. Both templates are validated against the ISEF Display & Safety rules and
  produce print-ready 300dpi output. Wraps the user's /latex-posters skill for the LaTeX side
  and /pptx-posters for the PowerPoint side; this skill provides the ISEF-specific layer
  (booth dimensions, required-display content like the SRC-approved abstract, judges'
  6-minute-read constraint, accessibility/legibility checks). Use whenever the student says
  "design my ISEF poster", "make a science fair poster", "poster template", "海报模板",
  "学术海报", "printable poster", or has results and needs to produce the physical poster
  for booth display.
argument-hint: [--format latex|powerpoint|both] [--size A0|36x48|48x36|custom] [--lang en|zh|both]
allowed-tools: Read, Write, Bash, Skill, Grep, Glob
rubric_version: 2026.1
---

# ISEF Poster Designer

You produce a printable, editable ISEF poster fitted to the official booth constraints, with
explicit Display & Safety compliance and judge-readability optimization.

You provide two parallel deliverables the student picks between:
- **LaTeX** (tikzposter or beamerposter class): best for typography-heavy projects with
  equations, multi-column scientific layouts. Print-ready PDF.
- **PowerPoint** (A0 metric or 48×36 inch): best for most students; no LaTeX setup required;
  editable in PowerPoint, Keynote, or Google Slides.

You wrap the user's existing `/latex-posters` and `/pptx-posters` skills for the heavy
typesetting; this skill adds the **ISEF-specific layer**:
- Booth dimension constraints
- Display & Safety required content
- Judges' 6-minute-read layout (Z-pattern, banner, abstract first)
- Accessibility: 1m viewing distance → minimum font sizes
- A QR code linking to supplementary data (allowed)

## When to use

- "Design my ISEF poster", "make a science fair poster", "海报模板"
- Student has finalized content (abstract, methods, results, figures) and needs the physical artifact
- Pair with: `/isef-abstract-optimizer` (before, for the abstract), `/science-fair-judge` (after, for poster critique), `/isef-data-analysis-tutor` (for figures)

Don't use this for: writing the abstract (use `/isef-abstract-optimizer`), generating figures
(use `/scientific-visualization`), or designing the booth itself (this skill handles the poster
on the booth, not the booth structure).

## Hard constraints (from ISEF 2026 DS-Rules.pdf, verified in playbook)

| Constraint | Value | Source |
|---|---|---|
| Booth footprint | 76 cm deep × 122 cm wide × 240 cm tall | DS-Rules.pdf (verified in playbook compliance-quickref §6) |
| Poster max width | ~122 cm (must fit booth backplane) | derived from booth |
| Lighting | LED only | DS-Rules.pdf §3 |
| Lasers (if any on poster) | Class 1, 2, 3A, 3R only | DS-Rules.pdf §3 |
| Required vertical display | SRC-stamped Official Abstract & Certification | DS-Rules.pdf §3 |
| Conditional vertical display | Form 1C (if RRI work), Form 7 (if continuation) | DS-Rules.pdf §3 |
| Available at booth (not displayed) | Form 1, 1A, Research Plan, Form 1B, photo release | DS-Rules.pdf §3 |
| NOT at booth | Completed informed-consent forms (blank sample is OK in logbook) | DS-Rules.pdf §3 |

## Recommended sizes

| Size | Dimensions | When to use |
|---|---|---|
| A0 portrait | 841 × 1189 mm (33.1 × 46.8 in) | Default. International standard; fits 122cm-wide booth with margin |
| A0 landscape | 1189 × 841 mm | Engineering / multi-figure projects |
| 48 × 36 in landscape | 121.9 × 91.4 cm | US-conventional; fits booth with minimal margin |
| 36 × 48 in portrait | 91.4 × 121.9 cm | US-conventional portrait |
| 36 × 56 in portrait | 91.4 × 142.2 cm | TALLER than booth allows in landscape; only portrait, and check booth height clearance |

**Avoid:** anything wider than 122 cm. Anything taller than 240 cm minus the table height
(typically ~75 cm), so practical max height ~165 cm.

## Workflow

### Step 1 — Confirm format + size

Ask: "LaTeX, PowerPoint, or both? Default: PowerPoint A0 portrait (works for most students).
Choose LaTeX if you have equations / math typesetting needs."

If `--size custom`: ask for width × height; validate against booth limits.

### Step 2 — Collect content

Ask for paths to:
1. Final abstract (or paste — should be the SRC-approved version)
2. 3-6 figures (or paths to a directory)
3. Tables (optional; many posters work better with figures only)
4. Bibliography (≥5 references)

If any of these aren't ready: stop and direct to the upstream skill (`/isef-abstract-optimizer`,
`/scientific-visualization`).

### Step 3 — Generate the poster

For **PowerPoint:** invoke `templates/build_pptx.py` (in this skill) which produces a
print-ready .pptx from a content YAML. Templates: `Default-A0` (clean), `Magazine-A0`
(editorial), `Engineering-48x36` (landscape for prototypes).

For **LaTeX:** invoke `/latex-posters` skill with the user's content, then post-process via
`templates/isef-poster.sty` (the ISEF-specific style hook in this skill).

For **both:** generate both in parallel; user picks which to print.

### Step 4 — Validate

Run `scripts/check_legibility.py` against the produced file:
- Body font ≥ 28pt at print size (so it's readable at 1m viewing distance)
- Heading font ≥ 60pt
- Title font ≥ 100pt
- Margin ≥ 2cm on all sides (printers eat margin)
- Color contrast: any text on background must pass WCAG AA (4.5:1 for body, 3:1 for headings)
- Image DPI ≥ 200 (300 ideal for print)

If validation fails, output a specific fix list — don't silently produce a bad poster.

### Step 5 — Export print-ready

PowerPoint: export to PDF at 300dpi via `python-pptx` + a print-friendly preset (no
transparency artifacts, fonts embedded). Output: `<project>-poster-print.pdf`.

LaTeX: compile via `xelatex` (better Unicode support for Chinese) or `pdflatex`. Output:
`<project>-poster.pdf`.

### Step 6 — Booth checklist

Output a printable booth-prep checklist (`<project>-booth-checklist.md`):

```
PRINT THIS
==========
☐ Final poster PDF (page count: 1)
☐ SRC-stamped Official Abstract (separate page, must be vertically displayed)
☐ [If RRI] Form 1C
☐ [If continuation] Form 7 + prior year's abstract + prior Research Plan

BRING TO BOOTH (not displayed but available)
============================================
☐ Form 1 (Adult Sponsor Checklist) — printed
☐ Form 1A (Student Checklist) — printed
☐ Research Plan / Project Summary — printed, signed
☐ Form 1B (Approval Form) — completed
☐ Lab notebook / logbook, dated and signed
☐ Bibliography (full, not just abstract version)
☐ Photo/video release form
☐ Any prototype or physical artifact

DO NOT BRING TO BOOTH
=====================
☐ Completed informed-consent forms (blank sample only, in logbook)
☐ Live organisms
☐ Hazardous chemicals
☐ Glass / sharps
☐ Class 3B or Class 4 lasers
☐ Lighting other than LED

DAY-OF
======
☐ Arrive early; sign Project Set-up Approval Form with D&S Committee
☐ QR code on poster works (if used) — test it on your phone
☐ Pens, sticky notes, business cards (for adult judges)
☐ Snacks + water (you'll be standing for 4+ hours)
```

## File map

```
SKILL.md (this file)
references/
  display-rules.md       ← booth + display rules from DS-Rules.pdf via playbook
  legibility-standards.md ← font/contrast/dpi minimums with rationale
templates/
  build_pptx.py           ← Python builder for the PPTX template (python-pptx based)
  default-a0-content.yaml ← example content schema for the builder
  isef-poster.sty         ← LaTeX style file (ISEF colors, fonts, layout hints)
  isef-poster-template.tex ← starter LaTeX file (uses isef-poster.sty)
scripts/
  check_legibility.py     ← validator for produced PDF/PPTX
```

## Source provenance

Booth dimensions, lighting, laser limits, required display items: ISEF 2026 DS-Rules.pdf via
`/Volumes/Mac-Mini/workspaces/tian2-edu/Competitions/isef-research-playbook/05-analysis/compliance-form-decision-tree-2026-05-01.md` §6.

Poster size conventions: https://www.posterpresentations.com/free-poster-templates.html (verified 2026-05-27 — A0 = 841×1189mm; 36×48, 48×72 inch standards).

Font/contrast standards: WCAG 2.1 AA (W3C); 1m-viewing-distance heuristic from academic
poster-design literature (Colin Purrington, Better Posters).

## Output footer

```
🤖 isef-poster-designer · rubric_version: 2026.1
ISEF 2026 AI-use disclosure: This skill provided the poster template and
validated print-readiness. Your content, figures, and final layout choices
are your own.

Next: print at a poster-print service (your school may have one; otherwise
https://www.posterpresentations.com/intel-isef-poster-printing-service.html
specializes in ISEF). After printing, run /science-fair-judge on the final
poster to catch issues before judging day.
```
