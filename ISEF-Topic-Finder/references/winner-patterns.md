# Winner Patterns Library

Patterns mined from `/Volumes/Mac-Mini/workspaces/tian2-edu/ISEF-Scrape/output/` (PHYS021 deep-dives + project inventories) and from `ISEF-Scrape/ISEF竞赛完全指南-完整版.md` ch. 4 (52k-project trends) and ch. 7 (2025 top-312 keyword analysis).

These are **patterns to instantiate**, not topics to copy. The topic-generation step (`flow-discover.md` §4) requires every candidate to instantiate ONE of these patterns. This prevents the rare-keyword-combo failure mode (Critic blocker §1).

**Important:** These patterns aren't formulas. Following the structure doesn't guarantee a win; violating them doesn't guarantee a loss. They are observed regularities in winning work, not necessary conditions.

## §1 — Tier-1 patterns (most reliably correlated with grand awards)

### P1 — "Reframe a mechanism as a statistical ensemble"
**Shape:** Take a configurational system (origami, linkages, granular media, polymers, cell-shape distributions) and recast its degrees of freedom as a statistical-mechanics ensemble. Apply MCMC sampling, partition functions, free-energy arguments.
**Why it wins:** Imports PHYS-MATH formalism into an unexpected substrate; visualizable; cross-disciplinary.
**Anchor:** PHYS021 (2026) "MCMC Sampling of Origami and Linkages."

### P2 — "Cross-category importation"
**Shape:** Take a winning structure from category X (e.g., PHYS) and apply it to a substrate in category Y (e.g., BMED). The methodological *form* is X's; the *material* is Y's.
**Why it wins:** Unlocks M4's positive arm; signals genuine cross-disciplinary reading.
**Examples to mine for variants:** stat-mech → tissue folding; graph theory → metabolic networks; signal processing → cell-imaging analysis.

### P3 — "Low-cost X for Y" (engineering / translational)
**Shape:** Build a sub-$200 device that performs a function normally requiring a $50k+ instrument, targeted at a specific underserved population/setting.
**Why it wins:** Concrete outcome + accessibility + social-impact narrative; visible prototype works in interview.
**Common substrates:** water-quality detector for a specific region; assistive device for a specific disability; field-deployable diagnostic.

### P4 — "Open-data + novel formal lens"
**Shape:** Take a publicly-available dataset (NASA, NOAA, NCBI, OpenAlex, gravitational-wave detector data) and apply a formal lens that no one has applied yet — usually from MATH or theoretical PHYS.
**Why it wins:** No equipment barrier; verifiable student ownership (the lens is the student's choice); cross-disciplinary.
**Anti-pattern (do NOT instantiate):** "Train a ResNet on the dataset" — this is application of a known method to a known domain. Low T1.1.

### P5 — "Validate against a known solution before extending"
**Shape:** Pick a problem where a known solution exists. Reproduce it first (sanity check). Then perturb it in one specific direction the student is interested in.
**Why it wins:** T1.2 ownership through the sanity check; T1.3 legibility because the baseline is well-known.

## §2 — Tier-2 patterns (work well but lower hit rate)

### P6 — "Build a tool, then use it"
**Shape:** Develop a measurement/analysis tool (software or hardware). Use it to answer one specific scientific question. The tool itself is part of the contribution.
**Why it works:** Two deliverables (tool + finding); modular milestones.

### P7 — "Local empirical question"
**Shape:** A specific empirical question about the student's own environment (their local lake, their school's HVAC, their community's pollution). Field data + simple analysis.
**Why it works:** Authentic motivation reads well in interview; T1.2 ownership extremely high.

### P8 — "Mathematical proof in graph/combinatorics/number theory"
**Shape:** A novel result in pure MATH, often by students with deep math-olympiad background. Written up as a research paper, not a poster artifact.
**Why it works:** When it works, it wins big (Regeneron STS finalists). But it requires unusual student preparation; not for typical HS.
**Note:** Per official rubric, MATH papers are judged differently — no physical exhibit; emphasis on the proof.

## §3 — Anti-patterns (penalize during generation)

If a topic generation candidate matches one of these, regenerate:

| Anti-pattern | Why it fails |
|--------------|--------------|
| "Train [neural net] to classify [public dataset]" | Saturated; M1 −5; T1.1 reframing low |
| "Survey [demographic] about [topic]" | IRB-heavy; T2.1 capped; T1.2 often mentor-driven |
| "Investigate the effect of [variable] on [outcome]" with no formal lens | Too generic; T1.1 reframing absent |
| "Use AI to [solve general problem]" | AI-use disclosure rules; T1.1 low unless AI is the *subject*, not just a tool |
| "Build a [popular gadget shape] for [audience]" without a specific user | T1.2 ownership ambiguous; no measurable outcome |
| "Recreate [recent paper] with my own data" | Derivative; T1.1 minimal |
| Same topic structure as ISEF top-3 winner in same category within last 3 years | M4 −5 (cargo-cult penalty) |

## §4 — Chinese-pathway notes (CASTIC + affiliated fairs)

For students entering ISEF via CASTIC + four China-affiliated fairs:

- **Translational medical and engineering categories** (BMED, ENBM, TMED, ROBO) historically over-represented in China-track projects. Cross-category importation INTO these from PHYS/MATH is an under-exploited niche.
- **CASTIC scoring weights novelty slightly higher than ISEF's official rubric** (per `ISEF-Scrape/ISEF竞赛完全指南-完整版.md` ch. 2). A topic that's borderline on T1.1 at ISEF might be stronger at CASTIC; flag this.
- **Mentor visibility** is a recurring T1.2 trap. Chinese-track projects often involve summer-school lab placements; the rubric must distinguish between mentor-supplied data (penalty) and mentor-supplied training (no penalty).

## §5 — Pattern mining backlog

Patterns to formalize in Phase 2 once back-testing data is available:
- "Origami" recurring keyword (per `ISEF-Scrape` six-year retrospective)
- "Microfluidics for [niche disease]"
- "Citizen science platform for [phenomenon]"
- "Climate-specific [mitigation/adaptation] in [region]"

These are documented but not yet stratified into Tier-1 vs Tier-2.
