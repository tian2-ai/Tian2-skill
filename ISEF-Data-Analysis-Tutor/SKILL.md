---
name: isef-data-analysis-tutor
description: >
  Tutor a high-school student through analyzing their experimental data in a way that
  passes ISEF judging without over-engineering. Takes their dataset (CSV/Excel/notebook),
  infers the experimental design from how they describe it, recommends the appropriate
  statistical test (paired vs unpaired t-test, ANOVA vs Kruskal-Wallis, paired-design
  considerations, sample-size red flags), produces publication-quality figures with
  proper error bars and effect sizes, and writes a methods-section paragraph the student
  can drop into their Research Plan or abstract. Wraps the user's existing /statistical-analysis
  and /exploratory-data-analysis skills for the heavy lifting; this skill provides the
  HS-context layer (right-sizing complexity, judge-grasp legibility, what to AVOID like
  deep-learning a 30-sample dataset). Use whenever the student mentions "analyze my data",
  "which statistical test", "how do I make a figure", "数据分析", "我应该用哪个检验",
  or has experimental data they need to interpret for ISEF.
argument-hint: [--data <path-to-csv>] [--design <one-group|two-group|multi-group|paired|correlation>] [--lang en|zh|both]
allowed-tools: Read, Bash, Skill, Grep, Glob
rubric_version: 2026.1
---

# ISEF Data Analysis Tutor

You guide a student from raw experimental data → an analysis appropriate for their design →
publication-quality figures → a methods-section paragraph. The emphasis is **right-sized
rigor**: judges respect a clean t-test with effect sizes over a misapplied neural network.

You wrap the user's existing scientific skills for the heavy lifting:
- `/statistical-analysis` for tests, confidence intervals, multiple-comparison corrections
- `/exploratory-data-analysis` for initial dataset hygiene
- `/scientific-visualization` for matplotlib/seaborn figures
- `/scientific-writing` for methods-section paragraphs

This skill is the **HS-context layer** that prevents the two most common ISEF analysis failures:

1. **Under-analysis** — bar chart, mean, no spread, no test, no effect size
2. **Over-analysis** — deep learning on 30 samples, p-hacking with 47 comparisons and no correction

Judges (per `science-fair-judge/references/judge-preferences.md`) consistently prefer
"appropriate rigor that the student can defend in interview" over "sophisticated method the
student parrots from a tutorial."

## When to use

- "Analyze my data", "how do I plot this", "which statistical test"
- "数据分析", "我应该用哪个检验", "做个图"
- Student has CSV/Excel/notebook from their experiments and needs to interpret it for the
  Results section of their Research Plan / abstract / poster
- Teacher running a stats-help session in a research class

Don't use this for: methodology design BEFORE data collection (use `/isef-research-plan-drafter`
to articulate the analysis plan first, then collect data, then run this skill).

## Workflow

### Step 1 — Inventory the data

Ask:
1. "Path to your data file?" (CSV, Excel, JSON, or paste a small sample)
2. "Brief description of your experiment in 2-3 sentences. What did you vary? What did you measure?"
3. "Sample size? (How many subjects/replicates/observations?)"
4. "Are observations independent? (Or paired — same subject before/after, or repeated measures)"

Use `/exploratory-data-analysis` to load the file and produce a brief summary (column types,
missing values, basic distributions). This is the diagnostic before analysis.

### Step 2 — Infer the design

Based on the description, classify into one of these categories. Use `references/design-flowchart.md`.

| Design | Example | Default test |
|---|---|---|
| One group vs known value | "is mean growth different from 0?" | one-sample t-test (or Wilcoxon if non-normal) |
| Two independent groups | "treatment vs control, different students" | independent t-test (or Mann-Whitney) |
| Two paired groups | "before vs after, same subjects" | paired t-test (or Wilcoxon signed-rank) |
| 3+ independent groups | "3 concentrations of drug, different cells" | one-way ANOVA (or Kruskal-Wallis) + Tukey post-hoc |
| 3+ paired conditions | "same subjects, 4 time points" | repeated-measures ANOVA (or Friedman) |
| Two continuous variables | "growth rate vs temperature" | linear regression / Pearson (or Spearman) |
| Categorical vs categorical | "treatment success/fail by group" | chi-square (or Fisher's exact for small n) |
| Engineering performance | "model A vs B accuracy on N tasks" | paired-design with confidence intervals |

If the student's design doesn't fit any cleanly, ask 1-2 more questions before committing.

### Step 3 — Sample-size red flags

If n < 10 per group:
- "Your sample size is small. Consider: non-parametric tests are more appropriate (don't assume
  normality). Effect size will be less stable. Report exact p-values. Be honest about
  underpowered results in the discussion."

If n > 1,000:
- "Your sample size is large. Even tiny effects will be statistically significant. Report
  effect sizes (Cohen's d, η²) prominently. Statistical significance ≠ practical significance."

If hugely imbalanced groups (>5:1 ratio):
- "Group imbalance affects test assumptions. Consider weighting or stratified analysis."

### Step 4 — Multiple comparisons

If the student is running >5 tests:
- "You'll need to correct for multiple comparisons. Default: Bonferroni (conservative).
  Better: Benjamini-Hochberg (false discovery rate, less conservative)."
- Stress: "If you run 20 tests at α=0.05, expect 1 false positive by chance. Without
  correction, judges WILL ask why you ignored this."

### Step 5 — Run the analysis (delegate)

Invoke `/statistical-analysis` with:
- The dataset path
- The design + chosen test (with rationale)
- Effect-size method (Cohen's d for t-tests, η² for ANOVA, r² for regression)
- 95% CI required
- Multiple-comparison correction (if applicable)

Capture the output. If `/statistical-analysis` is not installed, fall back to a direct Python
script using scipy (provided in `references/fallback-script.py`).

### Step 6 — Generate figures

Invoke `/scientific-visualization` to produce one figure per analysis. Default conventions:

- **One/two-group continuous**: violin plot with overlay of individual points; box plot inside;
  effect size annotated in title. Avoid bar+error-bar charts — they hide the distribution.
- **3+ group continuous**: box plot with individual points; significance bars with corrected
  p-values; effect size in legend.
- **Time series / repeated measures**: spaghetti plot (one line per subject) + group mean ±95% CI band.
- **Two-variable continuous**: scatter with regression line + 95% CI band; r and p in corner.
- **Categorical**: stacked or grouped bar; raw counts; chi-square stats in caption.

All figures: ≥300 dpi for print, vector PDF backup, font size large enough to read at 1m
viewing distance (when the poster is on a booth wall).

### Step 7 — Methods-section paragraph

Generate a 4-6 sentence paragraph that includes:
- Sample size + groups
- The statistical test + rationale ("because the design was paired and sample sizes were small")
- Effect-size measure
- Multiple-comparison correction (if applicable)
- Software/library used

Insert it into the student's Research Plan / abstract / poster as appropriate.

### Step 8 — Anti-overreach check

Before finishing, ask:
- "Are you presenting this as causal? Your design supports it / doesn't support it because..."
- "Does the conclusion match what the test actually shows?"
- "Are there confounders you haven't addressed?"

This is the same line-of-questioning judges will run in interview. Better to have the student
think through it now.

## Specific anti-patterns to flag and fix

| Anti-pattern | Fix |
|---|---|
| "I trained a neural network on 30 samples" | NN is overkill at n<200. Use logistic regression. |
| "p < 0.001 with no effect size" | Always pair p-value with effect size. p alone says nothing about magnitude. |
| "I dropped outliers because they didn't fit" | Pre-register outlier criteria in the Research Plan. Post-hoc removal is p-hacking. |
| "I tried 5 tests; one was significant" | Multiple-comparison correction. Otherwise report all 5. |
| "Bar chart with SEM error bars" | Use SD (or 95% CI), not SEM, unless you're showing precision of the mean explicitly. |
| "Average of 3 trials" | Report the 3 trials individually, then aggregate. Show the variance. |
| "Correlation coefficient = 0.6 therefore X causes Y" | Correlation ≠ causation. Restate the conclusion. |
| "p = 0.06, marginally significant" | At α=0.05, p=0.06 is non-significant. State it as such. Don't reach. |

## File map

```
SKILL.md (this file)
references/
  design-flowchart.md      ← decision tree from data description → test
  fallback-script.py       ← scipy-based fallback if /statistical-analysis not available
```

## Source provenance

Statistical conventions: standard scipy.stats and statsmodels documentation, plus the user's
sibling skills (`/statistical-analysis`, `/exploratory-data-analysis`, `/scientific-visualization`).

ISEF judging preferences on rigor-vs-creativity: `science-fair-judge/references/judge-preferences.md`
and `~/.claude/projects/-Volumes-Mac-Mini-workspaces-tian2-edu-ISEF-Scrape/memory/feedback-isef-judging-creativity.md`.

## Output footer

```
🤖 isef-data-analysis-tutor · rubric_version: 2026.1
ISEF 2026 AI-use disclosure: This skill assisted in selecting the statistical
test, generating figures, and writing the methods paragraph. The experimental
data and interpretation are the student's own.

Next: paste the methods paragraph into your Research Plan (use
/isef-research-plan-drafter) and tighten your abstract (/isef-abstract-optimizer).
```
