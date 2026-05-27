# Question Categories — The 10-Part Structure

Detailed guidance, worked examples, and per-category traps.

---

## Part A — ISEF General / Common Questions

These are the questions almost every judge asks. The student should be word-perfect on these — they're the warm-up that determines first impression.

### Required questions (always include):
1. Why did you choose this topic? (genuine curiosity test)
2. Walk me through your project in 2 minutes. (the elevator pitch)
3. What would you do differently if starting over? **THE most important canonical question**
4. What are the limitations of your study? (maturity test)
5. Can you explain your project to someone with no background? (real understanding test)

### Recommended additional:
6. How long did this project take?
7. Did you have a mentor? What did they help with?
8. Has this work been published or presented elsewhere?
9. What did you learn from doing this project?
10. How does this connect to your future plans / studies?

### Failure mode to drill against
"Nothing — I wouldn't change anything." This is the single biggest red flag. The student must give 3 specific things they'd change.

---

## Part B — Background Understanding Check

Tests whether the student grasps the *domain concepts* behind their work. Generic questions like "what is your field?" don't work — pick the 8-12 *specific concepts* their project depends on and ask for explanations.

### Pattern
For each technical term that appears prominently on the poster, generate one question of the form:
- "What exactly is X?"
- "Explain the difference between X and Y."
- "Why is X relevant to your work?"

### Worked examples by field

**Physics/astronomy project on stellar activity:**
- What is the Maunder Minimum?
- Difference between umbra and penumbra?
- What is log R'HK and why is it a good activity indicator?
- What does pole-on mean and why does it matter?
- What is metallicity?

**Biology/biomedical project on protein structure:**
- What is the difference between primary and tertiary structure?
- Why does this protein need a chaperone?
- Explain the role of post-translational modification in your context.

**CS/ML project on classification:**
- What is the difference between precision and recall?
- Why did you use cross-entropy loss vs MSE?
- Explain what a transformer attention head does.

### Trap to avoid
Do not ask textbook definition questions in isolation. Frame them as "in *your* context" so the student must connect concept → project, not recite Wikipedia.

---

## Part C — Methodology Questions

Tests whether the student *made* the methodological choices vs *inherited* them. This is where mentor-driven projects fail.

### Required pattern
For each major method choice on the poster, ask:
1. **What did you choose?** (factual)
2. **Why did you choose it?** (reasoning)
3. **What would the alternative have been?** (awareness of options)
4. **What's the tradeoff?** (real understanding)

### Categories of methodology questions
- Sample selection: why this population, why this size, why these cuts?
- Data preprocessing: why these filters, why this normalization?
- Algorithm/method choice: why this algorithm, why this configuration?
- Validation: why these validation tests, why this number of folds?
- Tools: why this software, why this library?

### Worked example
> "Why did you choose to use quantile regression instead of linear regression for your boundary?"

A strong answer explains: linear regression minimizes squared deviations around the *mean*, but a boundary line should track an *upper limit* of low-activity stars, not an average. Quantile regression at the 90th percentile directly estimates "the line below which 90% of low-activity stars lie." A weak answer says "R² was too low" without explaining what quantile regression solves.

### Trap to avoid
"Standard practice in the field" is a non-answer that signals the student didn't think about it.

---

## Part D — Statistics & Error Analysis

Almost every science fair project has statistical claims. Drill these especially hard for physics, bio, and engineering projects.

### Required questions (when applicable)
- Walk me through your statistical test(s). Why this test?
- What are your confidence intervals?
- What is your effect size, not just your p-value?
- How did you handle multiple comparisons?
- How do uncertainties propagate from raw measurements to your final result?
- Are your results sensitive to threshold choices? Show me.
- What is your false positive rate? (or: how would you estimate it?)

### Field-specific extras
- **Physics:** error propagation in quadrature, units check, theory comparison
- **Bio/medical:** sample size justification (power analysis), exact p-values not "p<0.05", positive/negative controls
- **CS/ML:** baseline comparison, train/test split discipline, overfitting checks

### Worked example
> "Your p-value is 10⁻⁸². Isn't that suspicious?"

Strong answer: addresses three sources separately — (1) effect size (Cohen's d separately reported), (2) sample-size artifact (log-transform robustness check), (3) assumption violations (non-parametric Mann-Whitney check). All three converge → p value is real.

Weak answer: "the software said so" or "yes that proves my hypothesis."

### Trap to avoid
Don't ask "is p<0.05" as a binary — judges hate that framing. Always ask about effect size and CI alongside.

---

## Part E — Results & Interpretation

Tests whether numbers are connected to physical/biological meaning, not just printed.

### Required questions
- What does your headline number actually mean?
- How does this compare to prior literature values?
- What does your result *not* tell us?
- If your results were the opposite, what would that mean?

### Worked example
> "Your candidate count is 250× larger than the literature value of ~3. Why?"

Strong answer: distinguishes *candidate* vs *confirmed*, explains methodological scale (3,339 stars systematic vs ~hundreds manual), addresses definition (4-year baseline vs decades). Weak answer: "my method is better."

---

## Part F — Limitations & Critical Analysis ⭐ MOST IMPORTANT

This is where Grand Award winners separate from qualifiers. The student who *names their own weaknesses* sounds like a real scientist.

### Required core question
**"What is the single biggest weakness of your study?"** — student must have a real answer, not a fluff one.

### High-value question patterns
- "Reconcile your conclusion that X with your Limitations stating Y." (the conclusion-vs-limitations tension)
- "Could your candidates be [alternative explanation]?" (rule out competing hypotheses)
- "How do you know your noise model is correct?" (foundation-shaking question)
- "If a future paper proves all your candidates are [contamination], how does your work survive?" (worst-case framing)
- "If your method works, why hasn't anyone else done this?" (technical/historical context)

### Critical principle for generation
Read the prior judge review's "weaknesses" section. **Every weakness flagged becomes a Part F question.** The student's answer should be the verbal version of how they'd address it.

### Top 3 callout
At end of Part F, identify the **3 questions the student MUST be 100% fluent on**. These are typically:
1. The conclusion-vs-limitations tension
2. The most field-specific methodology challenge
3. The "what would you do differently" canonical question (yes, repeat from Part A — it's that important)

---

## Part G — Impact & Future Work

Tests bigger-picture thinking. STS values this most; ISEF values it modestly.

### Required questions
- What's the broader impact of your work?
- Who is the audience for these results — solar physicists? exoplanet hunters? climatologists?
- What's next for this project? (concrete plan, not "more research")
- What would you do with infinite resources?

### Trap to avoid
"It will help solve X big problem" is too vague. Force specificity: who exactly will use this and how?

---

## Part H — Hypothetical "What If" Questions

Tests real understanding vs memorization. Judges use these to probe whether the student can reason from first principles.

### Pattern
Each hypothetical should connect to a *real choice* the student made, then perturb it:
- "What if you doubled your noise threshold to 100 ppm?" → tests understanding of the threshold tradeoff
- "What if half your validation data turned out wrong?" → tests robustness reasoning
- "What if you had only 100 samples instead of 3,000?" → tests how project scope changes with sample size
- "What if your method detected 0 candidates?" → tests how to interpret null results
- "What if a future paper proves [worst case]?" → tests resilience of conclusions

### Generation tip
Hypotheticals should test, not stump. They should probe a real choice; if the student understands the choice, they can reason through the answer.

---

## Part I — Answer Patterns to AVOID (table format)

Always use a 3-column table:

| ❌ Fatal answer | ✅ Replacement | Why this matters |
|---|---|---|
| "Nothing — I wouldn't change anything." | "Three specific things..." | "Nothing" is THE strongest red flag for scientific immaturity |
| "I have no limitations." | "Four main limitations..." | Every study has limitations; not naming them = ignorance or dishonesty |
| "My results perfectly confirmed the hypothesis." | "Results are consistent with the hypothesis but constrained by [X]" | "Perfectly" suggests p-hacking or shallow analysis |
| "It's too complicated to explain simply." | "Imagine [analogy]..." | Can't simplify = doesn't understand |
| "My mentor did most of the analysis." | "My mentor advised on X; I did Y, Z, W" | Triggers concerns about authorship |
| "I trust the result because the p-value is so small." | "Three convergent tests + huge effect size support the result" | Small p alone is not evidence |
| "I don't know" (with no follow-up) | "I'm not certain, but based on [data], I think..." | Empty "don't know" loses points; reasoned uncertainty gains them |
| "It's standard practice." | "I chose this because [specific reason]" | "Standard" hides absence of reasoning |
| "More data would solve it." | "[Specific data extension] would resolve [specific issue]" | Generic "more data" is lazy |
| Defensive / argumentative | "That's a fair point. Here's how I think about it..." | Judges want collaboration, not combat |

### Generation tip
Tailor the table to the student's project. If the project has shown a tendency in prior reviews to overclaim, include "MM is common" → "24% is upper bound" as a project-specific entry.

---

## Part J — Interview Day Tactics

Multiple sub-sections, action-oriented:

### J1. Time management (12-14 min/judge)
- 0-2 min: student-driven elevator pitch
- 2-10 min: judge Q&A
- 10-12 min: deep dive on whatever interests the judge
- 12-14 min: wrap-up, "any other questions?"

### J2. Body language
- Eye contact: ~50% speaking, ~70% listening
- Don't block the poster
- Point at figures, but don't gesticulate constantly
- Pauses are fine — "Let me think for a moment" beats a confused rush

### J3. "I don't know" recovery scripts
Provide 4 scripted phrases for different scenarios:
- Genuinely don't know: "I'm not certain, but based on [X], I would guess..."
- Partially know: "I understand [A]; I haven't worked through [B] in depth..."
- Forgot a number: "Let me think — I should remember this..."
- Judge challenges: "That's a fair point — let me reconsider..."

### J4. Key numbers to memorize
List ALL the project's key numbers with their CIs. The student should be able to recite these without hesitation. Examples:
- Sample size and final count (with CI)
- Headline percentage (with CI)
- Statistical effect sizes
- Boundary equations
- Threshold values

### J5. Poster pointing practice
A list of "indicate this section when answering this question" guidance. The student should rehearse pointing.

### J6. Mindset
- Judges aren't enemies. Hard questions = good signal.
- Acknowledging unknowns is a strength.
- Each judge resets — bad first interview doesn't doom the second.
- End with "Thank you for the great questions" — never wrong.
