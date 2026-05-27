# ISEF Compliance Quick-Reference

**Source:** `/Volumes/Mac-Mini/workspaces/tian2-edu/Competitions/isef-research-playbook/05-analysis/compliance-form-decision-tree-2026-05-01.md` (verified extract from 2026 Rules Book + All-Forms.pdf + DS-Rules.pdf + Generative-AI-Use-Table.pdf).

Used by the rubric's **compliance bias rule (A7)**: if a topic mentions humans, animals, tissue, pathogens, or hazardous chemicals — even in passing — T2.1 ≤ 7/10 and we surface the IRB/SRC/IACUC/IBC pathway.

## §1 — Substrate clusters (for triage)

When parsing a topic, classify it into one of six substrate clusters. The cluster determines the forms required and the time/risk profile.

| Cluster | What's in it | Forms profile | Time impact |
|---------|--------------|---------------|-------------|
| **A** | Vertebrate animals (school/home/field) | 5A + 1B + 3 + maybe 2 | SRC pre-approval gates everything; +2–4 weeks |
| **B** | Human participants (non-RRI) | 4 + Informed Consent + 1B + (3 if more than minimal risk) | IRB pre-approval; +3–6 weeks; non-trivial |
| **C** | PHBA / tissue / blood / body fluids / rDNA | 6A + (6B if tissue) + (BSL-1 or BSL-2 checklist) + SRC/IACUC/IBC | Heavy pre-approval; +4–8 weeks |
| **D** | Field work (soil/water/air/microorganism collection/device deployment/plant collection) | Field Work Safety Plan + (BSL-2 if unknown water microorganisms) + (3 if hazardous) | Modest; +1–2 weeks |
| **E** | Hazardous chemicals / activities / devices (incl. DEA-controlled) | 3 + (2 if DEA or otherwise applicable) | Low–moderate; school lab supervision |
| **F** | Low-substrate: math, pure CS, paper-and-pencil physics, theoretical chemistry | Forms 1, 1A, 1B, Research Plan, Abstract only | Minimal; fastest pathway to competition |

**Triage rule:** Cluster F has the fewest blockers. If you can frame a topic in cluster F without sacrificing T1.1 creativity, you eliminate the largest source of pre-experimentation delay.

## §2 — Always-required forms (every project)

Every ISEF project, regardless of cluster:
- **Form 1** — Adult Sponsor Checklist
- **Form 1A** — Student Checklist (per student)
- **Research Plan / Project Summary** (must accompany 1A)
- **Form 1B** — Approval Form (per student)
- **Abstract & Certification** (stamped/embossed; vertically displayed at booth)

## §3 — Conditional forms — trigger matrix

Verbatim from the playbook compliance tree. The rubric surfaces these as `compliance_flags` in the scorecard JSON.

| Form | Trigger | When | Pre-approval body |
|------|---------|------|-------------------|
| **1C** | Worked at RRI / industrial / non-home-school-field site | AFTER experimentation | n/a (mentor signs) |
| **2** | QS required by IRB/SRC; vertebrate at RRI; DEA-controlled substances | BEFORE experimentation | n/a |
| **3** | Human participants OR hazardous chemicals/materials/devices OR PHBA. Recommended for ALL. | BEFORE experimentation | n/a |
| **4** | Human participants at non-RRI | IRB BEFORE recruitment | IRB |
| **Informed Consent** | When IRB requires written consent / minor assent / parental permission | Before participation | IRB |
| **5A** | Vertebrate animal at school/home/field | SRC BEFORE experimentation | local/affiliate SRC |
| **5B** | Vertebrate animal at RRI | IACUC BEFORE experimentation | IACUC |
| **6A** | PHBA: microorganisms, rDNA, tissue, blood/products, body fluids | SRC/IACUC/IBC BEFORE experimentation | SRC / IACUC / IBC |
| **6B** | Human and vertebrate animal tissue (accompanies 6A) | Before experimentation | n/a (QS/DS attests) |
| **7** | Continuation project (annual re-review) | n/a | IRB/SRC as applicable |
| **BSL-1 Checklist** | Non-RRI BSL-1 lab work | Self-assessment before experimentation | reviewed by SRC |
| **BSL-2 Checklist** | Non-RRI BSL-2 lab; unknown microorganisms in water | Self-assessment before experimentation | reviewed by SRC |
| **Field Work Safety Plan** | Field projects (any of soil/water/air/device/chemical/microorganism/plant) | With Research Plan | n/a |
| **Project Set-up Approval Form** | On-site at ISEF | At competition | D&S Committee |

## §4 — Pre-approval-exempt biology (Form 3 only)

Some categories of biological work are exempt from pre-review and only require Form 3:

- Projects involving protists, archaea, and similar microorganisms
- Manure for composting, fuel production, or other non-culturing experiments
- Color-change coliform water test kits
- Microbial fuel cells
- Decomposing vertebrate organisms

These let students do biology without the 4–8 week pre-approval window.

## §5 — Generative AI use matrix (2026 official)

ISEF 2026 introduced a 14-row AI-use matrix. The skill must surface relevant rows whenever a topic plausibly involves AI assistance, and every output emits an AI-use disclosure line in the epilogue.

| AI use case | Permitted? | Disclosure required? |
|-------------|------------|----------------------|
| Brainstorming research questions / lit review | Permitted | Yes — disclose in Research Plan |
| Code generation (model training, analysis pipelines) | Permitted | Yes — disclose specific tools and what they generated |
| Image / figure generation for scientific results | **Prohibited** if used to fabricate data/results | n/a |
| Image / figure generation for poster decoration | Permitted | Yes — disclose tool |
| Paper-writing assistance (drafting, polishing prose) | Permitted | Yes — disclose extent |
| AI as analytical instrument (the AI itself is the experimental subject) | Permitted | Yes — declare AI as a tool/method/subject |
| AI to write the abstract verbatim | **Prohibited** | n/a |

Full 14-row table lives in the playbook source. Surface the relevant subset based on topic context.

## §6 — Display & Safety hard limits (when topic implies a physical exhibit)

For topics that will result in a physical exhibit, surface these in `--depth heavy` mode:

- **Booth footprint:** 76 × 122 × 240 cm (max)
- **Lighting:** LED only
- **Lasers:** Class 1 / 2 / 3A / 3R only (no Class 3B or 4)
- **No live organisms, hazardous chemicals, glass, sharps at the booth**
- See `DS-Rules.pdf` for full list

Topics that produce no physical artifact (pure computation / math) skip these.
