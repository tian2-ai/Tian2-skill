---
name: Tian-any2pdf
description: Tian's personal fork of any2pdf — converts Markdown to professionally typeset PDF with reportlab. Adds H4/H5/H6 heading support (the upstream any2pdf only handles H1-H3, which causes infinite-loop hangs on deeper headings). Battle-tested for long Chinese books with deep heading hierarchies. Use this skill when the user wants to turn a .md file into a styled PDF, generate a report PDF from markdown, or create a print-ready document from markdown content — especially Chinese technical books / playbooks with deeply nested sections. Also trigger when the user mentions "Tian-any2pdf", "md2pdf", "md转pdf 用我的", or asks for a "typeset PDF" from markdown source that contains H4 or H5 headings.
---

# Tian-any2pdf — Markdown to PDF (with H4–H6 support)

This skill is Tian's personal fork of the upstream `any2pdf`. It fixes a real bug in the
upstream parser and adds first-class rendering for `####` (H4), `#####` (H5), and
`######` (H6) headings.

## Why this fork exists

The upstream `any2pdf` (at `~/.claude/skills/any2pdf/`) only handles H1/H2/H3.
When a markdown document contains an H4 or deeper heading, the paragraph parser
breaks on the `#` prefix but never advances the line index — the script hangs
indefinitely, never emits any output past "Parsing markdown...", and produces no PDF.

This fork:

- Adds explicit branches for H4 (`####`), H5 (`#####`), H6 (`######`) before the
  paragraph parser, so deep headings advance the line index and render as bold
  section/sub-section text.
- Keeps every other behavior of upstream `any2pdf` identical, so the same CLI
  arguments work without changes.

## Quick Start

```bash
python3 ~/.claude/skills/Tian-any2pdf/scripts/md2pdf.py \
  --input report.md \
  --output report.pdf \
  --title "My Report" \
  --author "Author" \
  --theme warm-academic
```

All flags from upstream `any2pdf` work here unchanged. The full list:

| Flag | Default | Purpose |
| --- | --- | --- |
| `--input` | (required) | Path to markdown file |
| `--output` | `output.pdf` | Output PDF path |
| `--title` | First H1 | Cover title |
| `--subtitle` | "" | Cover subtitle |
| `--author` | "" | Author name |
| `--date` | today | Date string |
| `--theme` | `warm-academic` | One of: warm-academic, nord-frost, github-light, solarized-light, paper-classic, ocean-breeze |
| `--cover` | true | Include cover page |
| `--toc` | true | Include clickable TOC |
| `--page-size` | A4 | A4 or Letter |
| `--watermark` | "" | Watermark text (empty = none) |
| `--header-title` | "" | Running header text |
| `--footer-left` | author | Footer left text |
| `--edition-line` | "" | Cover edition line |
| `--frontispiece` | "" | Full-page image after cover |
| `--banner` | "" | Back cover banner image |
| `--disclaimer` | "" | Back cover disclaimer |
| `--copyright` | "" | Back cover copyright |
| `--code-max-lines` | 30 | Max lines per code block |

## Pre-Conversion Options (recommended)

When invoked interactively, ask the user (single `AskUserQuestion` call) which theme,
whether to add a watermark, and whether to include a frontispiece or back-cover material.

Theme presets (same as upstream `any2pdf`):

| Choice | `--theme` value | Feel |
| --- | --- | --- |
| 暖学术 | `warm-academic` | Cream paper, terracotta accents — editorial |
| 极简 | `github-light` | Black on white, print-friendly |
| 冷色 | `nord-frost` | Slate / blue, modern tech-doc |
| 文献 | `solarized-light` | Solarized-inspired |
| 古典 | `paper-classic` | Off-white, serif-heavy |
| 清新 | `ocean-breeze` | Teal accents |

## How H4–H6 render

| Level | Markdown | Render |
| --- | --- | --- |
| H1 | `# Part` | Full divider page with decoration |
| H2 | `## Chapter` | Chapter page break + chapter title + accent rule |
| H3 | `### Section` | Section heading style (`ST['h3']`) |
| **H4** | `#### Sub-section` | **Bold inline section heading** (uses `ST['h3']` size, wrapped in `<b>`) |
| **H5** | `##### Sub-sub-section` | **Bold body paragraph** (uses `ST['body']` size, wrapped in `<b>`) |
| **H6** | `###### Tiny heading` | Bold body paragraph |

## Hard-Won Lessons (carried over from upstream)

- `_font_wrap()` is mandatory for any text containing CJK characters, because reportlab
  doesn't fall back across fonts in `Paragraph`.
- `wordWrap='CJK'` on body/bullet styles is required to break long CJK runs cleanly.
- Code blocks need `esc_code()` to preserve indentation and `\n` (reportlab treats `\n`
  as whitespace by default).
- Canvas-drawn text (cover, headers, footers) needs `_draw_mixed()` to support CJK.

## Dependencies

```bash
pip install reportlab --break-system-packages
```

## Source attribution

Forked from `~/.claude/skills/any2pdf/scripts/md2pdf.py`. The only material change is
the addition of the H4/H5/H6 heading branches in `parse_md()`. See the upstream skill
for the original lessons file and broader theme documentation.
