# Privacy & Data-Flow Policy

This skill is used by minors (high-school students). Privacy is enforced by code design, not policy alone.

## §1 — What stays local

The following data never leaves the user's machine:

- **Student profile inputs**: interests narrative, background (coursework, hobbies), resources (school name, lab access), time budget, language preference, math/code comfort
- **Hypothesis text** entered at the A15 gate
- **All cache files** under `data/cache/`
- **All evidence packs** under `data/cache/evidence/`
- **Scorecards** rendered to the user

## §2 — What leaves the machine

Only the following crosses the network boundary, and only when the skill is actively running discover or score:

- **Sanitized topic phrases** sent to external APIs:
  - OpenAlex: topic search strings, concept IDs
  - PubMed E-utilities: topic search strings
  - bioRxiv API: topic search strings
  - arXiv API: topic search strings
  - Perplexity (via skill-wrap): topic search strings + accessibility query prefix
- **No school name, no student name, no age, no hypothesis text, no profile data** is ever sent to any external API.

## §3 — Sanitization rules

Before any external call, `cross_validate.py` runs the topic phrase through a sanitizer that strips:

- Proper nouns identified as person names (heuristic: TitleCase tokens not in a domain whitelist)
- Place names below city granularity (e.g., specific addresses, school names)
- Date ranges that could identify a cohort
- Numbers that look like ID numbers (SSN, school ID, etc.)

Sanitization is conservative: when in doubt, redact. If the sanitizer redacts a token that the topic legitimately needs (e.g., a place name central to a field study), it flags the redaction to the calling flow and asks the user whether to proceed.

## §4 — Cache structure

Caches are **topic-keyed, never student-keyed**:

```
data/cache/
├── openalex/<sha256(query_url)>.json
├── pubmed/<sha256(query_url)>.json
├── biorxiv/<sha256(query_url)>.json
├── arxiv/<sha256(query_url)>.json
├── perplexity/<sha256(query_url)>.json
└── isef_archive/<sha256(topic_phrase)>.json
```

This means:
- Two students researching the same topic share cache hits (efficient, no leakage)
- A student running discover multiple times on the same profile gets deterministic results (A6)
- Deleting cache deletes all student-traceable data (none of it is student-traceable to begin with)

## §5 — Multi-student / teacher mode

When a teacher runs the skill for a class:
- Each student's discover/score is a separate invocation (no batching that mixes profiles)
- Cache is shared across students (as in §4)
- Outputs are written to per-student directories the teacher controls; no centralized log

Future v2.1: teacher mode will add a `--cohort-id` flag for organized per-class outputs. Until then, manually invoke per student.

## §6 — Logging

The skill itself does NOT log invocations. The `data/cache/` files are the only persistent artifacts. If the user wants determinism guarantees (A6), they can clear the cache between runs and observe re-derivation.

If the user is on a system that logs Claude Code tool calls (e.g., enterprise audit logging), those logs may capture topic phrases. Document this in the skill's user-facing output footer if the system fingerprint suggests enterprise mode.

## §7 — Third-party data retention

- **OpenAlex** publishes its data publicly; queries are logged per their privacy policy (no IP/identity correlation by default for unauthenticated use)
- **Perplexity** logs queries per its privacy policy; consider this when the topic phrase is sensitive
- **PubMed / bioRxiv / arXiv** log queries per NIH / Cold Spring Harbor / Cornell policies respectively (all academic, low-risk)

The skill does not transmit student identity to any of these.

## §8 — Disclosure to the student

The first time the skill runs for a user, emit this disclosure in the prologue:

```
PRIVACY NOTICE
================
This skill sends topic phrases (not your name, school, or hypothesis) to
public research databases (OpenAlex, PubMed, bioRxiv, arXiv) and one
commercial API (Perplexity) to verify topic novelty. All your profile
inputs and your hypothesis stay on this machine. Caches are topic-keyed,
not student-keyed. To clear cached data, delete `data/cache/`.
```

Cache the disclosure-shown flag in `data/.disclosure_shown`; do not re-show in subsequent invocations from the same shell.

## §9 — Compliance with ISEF AI-use rules

This skill is itself an AI tool. Students using it must disclose its use in their Research Plan per the ISEF 2026 Generative-AI-Use Matrix (see `references/compliance-quickref.md` §5). The skill's epilogue restates this every time.

The student should disclose:
- That `isef-topic-finder` assisted in topic exploration and proxy scoring
- That the student's hypothesis and research are their own work
- That no part of the abstract or research plan was AI-generated verbatim
