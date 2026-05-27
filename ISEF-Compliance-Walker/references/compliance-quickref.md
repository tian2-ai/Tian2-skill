# ISEF Compliance Form Decision Tree

**Generated:** 2026-05-01 (slice 3)
**Source basis:** Verified extracts from official `societyforscience.org/isef/international-rules/*` HTML pages PLUS now-archived official PDFs in `03-archive-raw/` (SHA256 in `SHA256SUMS.txt`) normalized to text in `04-archive-normalized/`. PDFs parsed for this slice: `All-Forms.pdf`, `DS-Rules.pdf`, `Generative-AI-Use-Table.pdf`, `Field-Safety-Work-Plan.pdf`, `BSL1-Checklist.pdf`, `BSL2-Checklist.pdf`. Two PDFs archived but only spot-read this slice: `Book.pdf` (2026 Rules Book, ~2.8k extracted lines) and `Rules-Educator-Guide.pdf` (~2.8k extracted lines) — branches dependent on those bodies are explicitly flagged "archived, not yet parsed."

## 1. Always-required forms (every ISEF project)

Verified from `All-Forms.pdf` (Form 1, 1A, 1B) + `rules-for-all-projects/` HTML + `DS-Rules.pdf`:

- **Form 1 — Checklist for Adult Sponsor.** "Required for ALL projects." Completed by Adult Sponsor with student before research start.
- **Form 1A — Student Checklist.** "Required for ALL projects." Per student / team.
- **Research Plan / Project Summary.** "Required for ALL projects" and must accompany 1A. Written prior to experimentation.
- **Form 1B — Approval Form.** "A completed form is required for each student, including all team members."
- **Abstract & Certification (Official Abstract).** Official stamped/embossed copy required to be vertically displayed at the booth (`DS-Rules.pdf`).

## 2. Conditional forms — verified trigger matrix

All triggers below are quoted/paraphrased from the archived PDF bodies (`All-Forms.pdf`, `DS-Rules.pdf`, `Field-Safety-Work-Plan.pdf`).

| Form | Trigger | Pre-/Post-experiment | Pre-approval body | Source |
|---|---|---|---|---|
| **Form 1C** | Research conducted at a Regulated Research Institution / industrial setting / any work site other than home, school, or field. | Completed AFTER experimentation. | n/a (mentor signs) | All-Forms.pdf p.34; DS-Rules.pdf |
| **Form 2 — Qualified Scientist** | Used when human participants, vertebrate animals, potentially hazardous biological agents, or hazardous substances/devices are involved AND a QS is required by IRB/SRC, or for vertebrate-animal work at a regulated site, or for DEA-controlled substances. | Completed and signed BEFORE experimentation. | n/a | All-Forms.pdf p.35 |
| **Form 3 — Risk Assessment** | "Recommended for all projects." REQUIRED for projects involving Human Participants, Hazardous Chemicals/Materials/Devices, or Potentially Hazardous Biological Agents. Also the only required form for the exempt-microorganism categories listed below. | Before experimentation. | n/a | All-Forms.pdf p.36 |
| **Form 4 — Human Participants** | Required for all research involving human participants NOT at a Regulated Research Institution. (At an RRI, use institutional IRB documentation instead.) | IRB approval BEFORE recruitment / data collection. | IRB | All-Forms.pdf p.37 |
| **Human Informed Consent Form** (sample) | Whenever the IRB requires written informed consent / minor assent / parental permission. | Before participation. | IRB | All-Forms.pdf p.38 |
| **Form 5A — Vertebrate Animal** | Vertebrate-animal research at school / home / field site. | SRC pre-approval BEFORE experimentation. | local/affiliate SRC | All-Forms.pdf p.39 |
| **Form 5B — Vertebrate Animal** | Vertebrate-animal research at a Regulated Research Institution. | IACUC approval BEFORE experimentation; form completed/signed AFTER experimentation. | IACUC | All-Forms.pdf p.40 |
| **Form 6A — Potentially Hazardous Biological Agents** | Microorganisms, rDNA, fresh/frozen tissue (incl. primary cell lines, human/primate established cell lines, tissue cultures), blood, blood products, body fluids. Includes BSL-1 / BSL-2 / MDRO branches. | SRC / IACUC / IBC approval BEFORE experimentation. | SRC / IACUC / IBC | All-Forms.pdf p.41 |
| **Form 6B — Human and Vertebrate Animal Tissue** | Same tissue scope as 6A (fresh/frozen tissue, primary cell lines, blood/products, body fluids). MUST accompany Form 6A. | Before experimentation. | n/a (QS/DS attests) | All-Forms.pdf p.42 |
| **Form 7 — Continuation / Research Progression** | Project is a continuation/progression in the same field as a previous project. Must attach previous year's abstract + Research Plan. | n/a | n/a | All-Forms.pdf p.43; DS-Rules.pdf |
| **BSL-1 Checklist** | When experimentation occurs at a non-RRI BSL-1 lab (e.g. high-school microbiology, water-testing facility). Attach to Form 6A. | Lab self-assessment before experimentation. | reviewed by SRC | BSL1-Checklist.pdf |
| **BSL-2 Checklist** | When experimentation occurs at a non-RRI BSL-2 lab (high-school lab, medical office, diagnostic lab). Attach to Form 6A. Also required by Field Work Safety Plan when collecting unknown microorganisms in water. | Lab self-assessment before experimentation. | reviewed by SRC | BSL2-Checklist.pdf; Field-Safety-Work-Plan.pdf |
| **Field Work Safety Plan** | Field projects involving soil, water, air, device deployment, chemicals, microorganism collection, or plant collection. | Reviewed alongside Research Plan before experimentation. | n/a | Field-Safety-Work-Plan.pdf |
| **Project Set-up Approval Form** | Issued/signed on-site at ISEF; signed by finalist + Display & Safety Committee at inspection. | At competition. | D&S Committee | DS-Rules.pdf |

### 2a. Pre-approval-exempt biological projects (Form 3 only)

Verified from Form 1 narrative (All-Forms.pdf p.30): exempt from prior review but require Risk Assessment Form 3:

- Projects involving protists, archaea, and similar microorganisms.
- Manure for composting, fuel production, or other non-culturing experiments.
- Color-change coliform water test kits.
- Microbial fuel cells.
- Decomposing vertebrate organisms.

## 3. Grounded decision flow

```
START
  ├─ ALL projects → Form 1, Form 1A, Research Plan/Project Summary,
  │                  Form 1B (per student), Official Abstract & Certification
  │
  ├─ Continuation in same field as a prior project? ──► Form 7 + attach prior abstract & RP
  │
  ├─ Worked at regulated research institution / industrial / non-home-school-field site? ──► Form 1C (after experimentation; vertically displayed at booth)
  │
  ├─ Human participants?
  │     ├─ at non-RRI? ──► Form 4 (IRB-approved BEFORE recruitment) + Human Informed Consent (if IRB requires)
  │     │                  + Form 3 if "more than minimal risk" + Form 2 if IRB requires QS
  │     └─ at RRI?     ──► institutional IRB documentation in place of Form 4
  │
  ├─ Vertebrate animals?
  │     ├─ school / home / field ──► Form 5A (SRC pre-approval) + Form 2 if QS required
  │     └─ RRI                     ──► Form 5B (IACUC pre-approval; signed post-experimentation) + Form 2 (required for vertebrate work at RRI per Form 1)
  │
  ├─ Potentially Hazardous Biological Agents (microorganisms, rDNA, tissues, blood, body fluids)?
  │     ├─ Exempt category (protists/archaea/MFC/etc.) ──► Form 3 only, no pre-approval
  │     ├─ Else ──► Form 6A (SRC/IACUC/IBC pre-approval)
  │     │           ├─ Tissue / cell lines / blood ──► add Form 6B
  │     │           ├─ Non-RRI BSL-1 lab ──► attach BSL-1 Checklist
  │     │           ├─ Non-RRI BSL-2 lab ──► attach BSL-2 Checklist
  │     │           └─ MDRO at RRI BSL-2+ ──► IBC pre-approval (date attached on Form 6A)
  │
  ├─ Hazardous Chemicals / Activities / Devices?
  │     └─ Form 3 (no SRC pre-approval) + Form 2 if DEA-controlled or otherwise applicable
  │
  ├─ Field work (soil / water / air / device / chemical / microorganism / plant)?
  │     ├─ Always ──► Field Work Safety Plan reviewed with Research Plan
  │     ├─ Unknown microorganisms in water ──► BSL-2 protocols
  │     └─ HAB period ──► sampling prohibited; documentation of no-bloom required
  │
  └─ At competition ──► Project Set-up Approval Form (signed on-site by finalist + D&S Committee)
                         and comply with Display & Safety hard limits (§4)
```

## 4. Display & Safety hard limits (verified from `DS-Rules.pdf` + display-safety HTML)

Required to be vertically displayed at the booth:
1. Official Abstract & Certification (stamped/embossed by SRC).
2. ISEF Project Set-up Approval Form (received on-site).
3. Conditional: Form 1C (if any RRI/industrial/other-site work); Form 7 (if continuation).

Required at the booth but NOT vertically displayed (must be available in case requested):
- Form 1 (Adult Sponsor), Form 1A (Student Checklist), Research Plan, Form 1B (Approval), photograph/video release form.

NOT to be at the project display booth or in the exhibit hall:
- Completed informed consent/assent forms for human-participant studies. A blank sample may live in the logbook.

Hard physical limits (verified earlier from display-safety HTML, re-confirmed in DS-Rules.pdf):
- Max display footprint 76 cm depth × 122 cm width × 240 cm height.
- LED lighting only; incandescent / fluorescent prohibited.
- Lasers Class 1, 2, 3A, or 3R only; handheld lasers prohibited.
- Power 120 / 220 V AC only.
- Prohibited at booth: living organisms, hazardous chemicals, weapons, glass, sharps, personal items / packaging stored under table.

## 5. AI use matrix (verified verbatim from `Generative-AI-Use-Table.pdf`)

| Task | Acceptable? | Conditions |
|---|---|---|
| Ask AI to identify/summarize key points in an article before reading it (literature-review starting point). | Yes | Acceptable without explicit citation. |
| Ask AI to summarize a book/article and reproduce that summary in your literature review without reading the source. | No | Never acceptable; no engagement with the source. |
| Use an AI chatbot as a writing tool to generate/develop ideas. | Yes | May require explicit citation depending on circumstances. Maintain a logbook of prompts as part of research notebook. |
| Use generative AI to initially write the research plan, abstract, paper, or poster. | No | Must be the independent work of the student. Refinement after the initial document is complete is allowed with explicit citation and a log. |
| Ask AI to write an abstract or section of your research paper and submit as your own. | No | Never acceptable. |
| You write an abstract; AI sharpens language without modifying / adding to / replacing main points. | Yes | Acceptable without explicit citation only if changes are limited to grammar and syntax. |
| Use AI to write initial code for your project. | Yes | Acceptable only with explicit citation stating which portions are AI-generated, plus a log of the prompts. |
| Ask AI to produce a flowchart, graphic, or image for paper/presentation. | Yes | Image must be clearly marked AI-generated with explicit citation describing how it was created. |
| Ask AI to add additional points to your research paper after you wrote it. | No | Never acceptable. |
| Use AI to produce conclusions, future steps, etc. | No | Never acceptable. |
| Use AI to help identify appropriate statistical tests or software tools (interpretation must be by the student). | Yes | Requires a log of prompts as part of research notebook. |
| Use AI to collect data and write research plan; use AI to provide citations backing your claims. | No | Never acceptable. |
| Ask AI to produce a starter bibliography. | No | Never acceptable. |
| Ask AI to fix the structure or formatting of your bibliography. | Yes | Acceptable without explicit citation; you must review and verify all citations as valid. |

Source: `Generative-AI-Use-Table.pdf` (Society for Science, Oct 2025; SHA256 `38ca04bbf1a6b5e650cd28bb6caa7af0e04adafd6de5a900d9f7c4334163be19`). Affiliated fairs may impose stricter policies.

## 6. Open / unverified branches (still explicitly NOT claimed verified)

- Form 6A MDRO branch: pre-approval workflow is captured but full IBC submission timing not yet cross-checked against `Book.pdf` body.
- Educator-side review timing and pre-registration calendar — `Rules-Educator-Guide.pdf` archived but not yet parsed in this slice.
- Affiliated-fair vs. ISEF-only deviations — not extracted; `Book.pdf` not yet parsed.
- Rules Wizard interactive logic (`ruleswizard.societyforscience.org/`) — not exercised this slice.
- ISEF Rules FAQ corrections / clarifications — not extracted.

## 7. Next analytical pass

1. Parse `Book.pdf` (2026 Rules Book) end-to-end to confirm form-trigger logic and cross-link rule sections, and to close §6 gaps.
2. Parse `Rules-Educator-Guide.pdf` for advisor-side deadlines and pre-registration steps.
3. Cross-validate this matrix against the Rules Wizard outputs for representative project archetypes.
4. Promote this decision tree from "grounded form-trigger matrix (slice 3)" to "fully cross-validated compliance map" once §6 branches close.
