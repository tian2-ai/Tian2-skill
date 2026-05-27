# Design → Test Flowchart

```
START: What's the structure of your data?
│
├─ ONE GROUP — comparing to a known value
│    │
│    ├─ Data approximately normal? → ONE-SAMPLE t-TEST
│    └─ Not normal / small n / ordinal? → WILCOXON SIGNED-RANK
│
├─ TWO GROUPS — comparing two samples
│    │
│    ├─ Are observations PAIRED (same subjects, before/after, matched)?
│    │    │
│    │    ├─ Yes, paired
│    │    │    ├─ Differences normal? → PAIRED t-TEST
│    │    │    └─ Not normal? → WILCOXON SIGNED-RANK
│    │    │
│    │    └─ No, independent
│    │         ├─ Both groups normal, equal variance? → STUDENT'S t-TEST
│    │         ├─ Both groups normal, unequal variance? → WELCH'S t-TEST
│    │         └─ Not normal? → MANN-WHITNEY U
│    │
│    └─ Effect size: Cohen's d (for t-tests)
│
├─ THREE+ GROUPS — comparing multiple samples
│    │
│    ├─ Independent groups?
│    │    ├─ Normal + equal variance? → ONE-WAY ANOVA + TUKEY POST-HOC
│    │    ├─ Normal + unequal variance? → WELCH'S ANOVA + GAMES-HOWELL
│    │    └─ Not normal? → KRUSKAL-WALLIS + DUNN'S POST-HOC
│    │
│    ├─ Paired / repeated measures?
│    │    ├─ Normal? → REPEATED-MEASURES ANOVA (rm-ANOVA)
│    │    └─ Not normal? → FRIEDMAN TEST + DURBIN-CONOVER POST-HOC
│    │
│    └─ Effect size: η² (eta-squared) or ω² (omega-squared)
│
├─ TWO CONTINUOUS VARIABLES — relationship
│    │
│    ├─ Linear, both normal? → PEARSON CORRELATION + LINEAR REGRESSION
│    ├─ Monotonic but not linear? → SPEARMAN CORRELATION
│    └─ Both ranked / ordinal? → SPEARMAN or KENDALL'S TAU
│    │
│    └─ Effect size: r² (coefficient of determination)
│
├─ CATEGORICAL VS CATEGORICAL — frequencies
│    │
│    ├─ Both nominal, all cells ≥5 expected? → CHI-SQUARE TEST
│    ├─ Small expected cell counts? → FISHER'S EXACT TEST
│    └─ Two paired binary? → MCNEMAR'S TEST
│    │
│    └─ Effect size: Cramér's V (or odds ratio)
│
├─ TIME SERIES / LONGITUDINAL
│    │
│    ├─ Few subjects, many time points → MIXED-EFFECTS MODEL or rm-ANOVA
│    ├─ Forecasting → ARIMA, exponential smoothing, or seasonal decomposition
│    └─ Survival data → KAPLAN-MEIER + LOG-RANK
│
└─ ENGINEERING PERFORMANCE / MODEL COMPARISON
     │
     ├─ Model A vs B on same N tasks → PAIRED design, bootstrap CI
     ├─ Multiple models, multiple metrics → CRITICAL DIFFERENCE DIAGRAM
     └─ Always report: 95% CI on the key metric; not just point estimate
```

## When to use parametric vs non-parametric

**Parametric** (t-test, ANOVA, Pearson) require:
- Continuous data
- Approximately normal distribution (check with histogram + Shapiro-Wilk for n<50)
- Homogeneity of variance (Levene's test) for ANOVA

**Non-parametric** (Mann-Whitney, Kruskal-Wallis, Spearman) require:
- Just ordered data
- No distributional assumption
- Slightly less statistical power if data is genuinely normal

**Heuristic for ISEF projects:**
- n < 30 per group + can't verify normality → default to non-parametric
- n ≥ 30 per group + visual histogram looks normal-ish → parametric is fine
- Skewed data with n<100 → non-parametric

## Multiple comparisons

If running >5 tests across the same dataset:
- **Bonferroni**: divide α by number of tests (conservative; safe but loses power)
- **Benjamini-Hochberg (FDR)**: less conservative; controls expected false-discovery rate
- **Tukey HSD**: built-in for ANOVA post-hoc; most common in HS projects

Always **state the correction in the methods**. Judges check.

## Effect sizes (always report alongside p-values)

| Test family | Effect-size measure | Interpretation |
|---|---|---|
| t-test | Cohen's d | 0.2 = small, 0.5 = medium, 0.8 = large |
| ANOVA | η² (eta-squared) | 0.01 = small, 0.06 = medium, 0.14 = large |
| Correlation | r² | 0.01 = small, 0.09 = medium, 0.25 = large |
| Chi-square | Cramér's V | 0.1 = small, 0.3 = medium, 0.5 = large |
| Logistic regression | Odds ratio | (1 = no effect; >2 or <0.5 = notable) |
| Engineering performance | Δ accuracy + 95% CI on Δ | Domain-specific |

**Why effect sizes matter for ISEF interview**: a judge will ask "is that a big effect or a
small effect?" A p-value can't answer this. An effect size can.

## Common HS-student mistakes (and the fix)

| Mistake | Fix |
|---|---|
| Running 3 t-tests instead of one ANOVA | Use ANOVA; t-tests inflate Type I error |
| Reporting "p < 0.05" without specifying the test | Always name the test |
| Ignoring assumption checks | At minimum: visual histogram + Shapiro-Wilk (n<50) |
| Using SEM bars without saying so | Label what your error bars represent |
| Calling a regression "significant" without stating r² | r² tells you how much variance is explained; p alone tells you the slope ≠ 0 |
| Treating ordinal data as continuous (e.g., Likert 1-5 as if it were temperature) | Use non-parametric or ordinal-regression methods |
