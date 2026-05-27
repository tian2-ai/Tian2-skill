# Category Judge Personas

For each ISEF category, this file describes the likely judge background, what they typically
weight in scoring, the most common interview questions, and the most common red flags they catch.

**Source basis:**
- Official ISEF Grand Award judge requirements (PhD+ / 6+ years; per societyforscience.org)
- ISEF 2026 category list (22 categories per playbook)
- Per-category judging preferences synthesized from `science-fair-judge/references/judge-preferences.md`
- PHYS-specific patterns from `ISEF-Scrape/output/PHYS-judging-guide-2026-05-13.md`

These personas are observed regularities, not deterministic predictions. Individual judges
vary.

---

## PHYS — Physics and Astronomy

**Likely judge mix:** Academic physicists (university faculty), national-lab researchers,
quantum/computational physics PhDs, research software industry (semiconductor, optics).
Astronomy projects often draw observatory and aerospace-industry judges.

**What they emphasize (per PHYS-judging-guide-2026-05-13.md):**
- **Conceptual creativity over data scale** — judges reward reframings
- Rigorous methodology defense (theory + experiment alignment)
- Mathematical / dimensional consistency
- Connection to broader physics framework

**Most common interview opener:** "Walk me through your hypothesis and why it's interesting from
a physics standpoint."

**Common red flags:**
- Treating physics as data-fitting rather than as physical reasoning
- Using ML/AI as a black box without physical interpretation
- Numerical answers without uncertainty quantification
- Hand-waving on dimensional analysis

**Must-have at booth:** Equations on your poster (judges look for them). A clear theoretical
framework section. Uncertainty bars on EVERY plot.

---

## MATH — Mathematics

**Likely judge mix:** Math department faculty, applied mathematicians, theoretical computer
scientists, statisticians from industry. Often more diverse career paths than PHYS.

**What they emphasize:**
- Rigor of the proof (for theoretical work) or the modeling (for applied)
- Novelty of the question or approach
- Clarity of presentation — math judges read carefully

**Most common interview opener:** "State your problem precisely. State your main result precisely."

**Common red flags:**
- Hand-wavy proofs ("this is obvious")
- Notation collisions / inconsistent variable usage
- Claiming a result more general than what was actually proven
- Code for simulations without statistical assessment

**Must-have at booth:** Clearly stated theorem (or, for applied: clearly stated problem + main
result). Proof sketch, not just statement. Acknowledge what you DIDN'T prove.

---

## BMED — Biomedical and Health Sciences

**Likely judge mix:** Physicians (MD/PhD), translational researchers, clinical statisticians,
pharmacology faculty. Many have hospital affiliations.

**What they emphasize:**
- Verifiable student ownership (BMED judges scrutinize this heavily — many projects are
  mentor-driven; ownership defense is critical)
- Compliance rigor (IRB approvals, informed consent process)
- Translational thinking — "what does this mean for patients?"
- Statistical appropriateness (especially sample size + power)

**Most common interview opener:** "Tell me your specific clinical question and how your project
addresses it."

**Common red flags:**
- Underpowered studies (n<10 per group) without acknowledgment
- IRB approval ambiguity
- Overstating clinical implications from a small study
- "My mentor's lab" framing that suggests low ownership

**Must-have at booth:** IRB approval letter visible. Clear inclusion/exclusion criteria. Sample
size justification. A clinical-significance section, not just statistical significance.

---

## CELL — Cellular and Molecular Biology

**Likely judge mix:** Cell biologists, molecular biologists, biochemists. Heavy academic
representation; some pharma/biotech industry.

**What they emphasize:**
- Reproducibility (biological replicates, not just technical replicates)
- Image-quality and quantification (when imaging is involved)
- Western blots / FACS / sequencing data presented with full context
- Controls — positive AND negative, and judges WILL ask

**Most common interview opener:** "Tell me about your controls."

**Common red flags:**
- Single-replicate "representative" images
- Missing negative controls
- ImageJ quantification without thresholding rationale
- Calling something "significant" without specifying the test

---

## ENBM — Biomedical Engineering

**Likely judge mix:** Biomedical engineers, medical-device industry, regulatory-affairs
professionals.

**What they emphasize:**
- Working prototype (or clear demonstration of function)
- Design-criteria-to-result traceability
- Iteration history (what was version 1? what changed?)
- Real-world deployment considerations (cost, manufacturability, sterilization)

**Most common interview opener:** "Show me how it works."

**Common red flags:**
- Renderings or CAD-only with no built prototype
- "It will be sterilizable" without testing
- Cost claims without bill-of-materials

---

## ROBO — Robotics and Intelligent Machines

**Likely judge mix:** Robotics PhDs, autonomous-systems industry, ML researchers, mechanical
engineering faculty.

**What they emphasize:**
- Working demonstration on the booth
- Failure-mode characterization (what makes it stop working?)
- ML model explanation (judges resist black-box claims)
- Power, latency, real-time constraints

**Most common interview opener:** "Run a demonstration for me."

**Common red flags:**
- Pre-recorded video instead of live demo
- "I trained a CNN" without explaining the data, the loss, the validation split
- Claiming autonomy without demonstrating recovery from perturbation

---

## SFTD — Software Design

**Likely judge mix:** Software engineers, computer science faculty, security professionals,
ML/data-science industry.

**What they emphasize:**
- Code quality (judges may ask to see GitHub)
- Test coverage / validation
- Distinction between novel work and library/framework use
- Clear "what's hard" articulation

**Most common interview opener:** "What's the technical challenge that was hardest?"

**Common red flags:**
- Wrapping an off-the-shelf library and calling it new
- Saturated topic (e.g., yet another chat app, yet another image classifier)
- No code repo / no test suite

---

## EAEV — Earth and Environmental Sciences

**Likely judge mix:** Environmental scientists, atmospheric researchers, geologists, climate
scientists.

**What they emphasize:**
- Field-data rigor (sampling design, replication, control sites)
- Connection to local context (judges love locally-grounded work)
- Awareness of regulatory / policy implications

**Most common interview opener:** "Describe your sampling protocol."

---

## ENEV — Environmental Engineering

**Likely judge mix:** Environmental engineers, civil engineers, sustainability industry.

**What they emphasize:**
- Quantified environmental benefit (mass, energy, cost saved)
- Real-world feasibility (scale, regulatory acceptance)
- Comparison to existing solutions

**Most common interview opener:** "What's your improvement over current state-of-the-art?"

---

## EGSD — Energy: Sustainable Materials and Design

**Likely judge mix:** Materials scientists, energy researchers, sustainability industry.

**What they emphasize:**
- Energy quantification (joules, efficiency, payback period)
- Materials sourcing (life-cycle considerations)
- Comparison to existing technologies on cost AND performance

---

## CHEM — Chemistry

**Likely judge mix:** Chemists across organic, inorganic, analytical, physical sub-fields.

**What they emphasize:**
- Synthesis or analytical-method rigor (yield, purity, characterization)
- Mechanism / pathway proposals
- Spectra interpretation

**Most common red flag:** Single-step claims without characterization data (NMR, MS, IR).

---

## CBIO — Computational Biology and Bioinformatics

**Likely judge mix:** Bioinformaticians, computational biologists, genomics industry.

**What they emphasize:**
- Code reproducibility (GitHub repo, pinned dependencies)
- Statistical multiple-testing correction
- Biological interpretation of computational results

---

## Other categories (briefer)

| Category | Judge emphasis |
|---|---|
| ANIM | Animal behavior rigor; ethics; replication |
| BCHM | Synthesis + characterization; pathway evidence |
| BEHA | Sample size; IRB; behavioral measurement validity |
| EBED | Working circuit; signal integrity; embedded constraints |
| ETSD | Working prototype; load testing; failure modes |
| MATS | Characterization rigor; comparison to known materials |
| MCRO | Sterile technique; biosafety; species ID rigor |
| PLNT | Replication across plants/plots; controls; phenotype quantification |
| TECA | Functional demo; user-experience considerations |
| TMED | Translational pathway; clinical relevance; ethical considerations |

For categories not detailed above, the universal principles apply: **defensible methodology +
appropriate rigor + clear ownership + cross-disciplinary legibility**.
