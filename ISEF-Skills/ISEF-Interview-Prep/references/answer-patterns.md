# Answer Patterns — Strong vs Weak Templates

How a well-prepared student should structure responses, with bilingual (EN + 中文) phrasing and recovery scripts for moments when they don't know the answer.

---

## 1. The five answer archetypes

Most strong answers in science fair interviews fit one of five archetypes. Train the student to recognize which archetype the question calls for.

### 1a. The "Choice + Reason + Alternative + Tradeoff" archetype
Used for: methodology questions, design choices, statistical test choices.

> **Template (EN):** "I chose [X]. The reason is [Y]. The alternative would have been [Z], but I rejected it because [tradeoff]. The cost of choosing X is [acknowledged downside]."

> **Template (中文):** "我选择了 [X]。原因是 [Y]。备选方案是 [Z]，但我没采用，因为 [取舍]。选 X 的代价是 [承认的不足]。"

**Why this works:** It signals the student knew alternatives existed and made a deliberate decision. Judges almost always upgrade scientific maturity scores when they hear this pattern.

**Worked example:**
> Q: "Why did you use Mann-Whitney U instead of a t-test?"
> A (EN): "I chose Mann-Whitney U because it's non-parametric — it doesn't assume normal distributions, which mattered because my activity-index distribution is right-skewed. A t-test would have been simpler and given comparable p-values, but I rejected it because if the skewness violates normality, the t-test's p-value isn't trustworthy. The cost of Mann-Whitney is slightly lower power, but with N=3,339 my effect size is so large that power isn't a concern."
> A (中文): "我选择 Mann-Whitney U 是因为它是非参数检验，不假设正态分布，而我的 log R'HK 分布是右偏的。t-test 更简单且 p-value 接近，但我没用是因为如果偏度违反正态性，t-test 的 p-value 就不可信了。Mann-Whitney 的代价是 power 略低，但 N=3,339 的样本量加上极大效应量，power 完全不是瓶颈。"

---

### 1b. The "Three things, ranked" archetype
Used for: limitations, future work, "what would you do differently."

> **Template (EN):** "There are three [limitations / next steps / things I'd change]. The most [important / serious] is [A] because [reason]. Second, [B] which affects [scope]. Third, [C] which is bounded by [test/check]."

> **Template (中文):** "有三个 [局限 / 下一步 / 改进点]。最 [重要 / 严重] 的是 [A]，因为 [原因]。第二是 [B]，影响 [范围]。第三是 [C]，由 [验证] 来约束。"

**Why this works:** "Three" is enough to show depth without being overwhelming. Ranking signals critical thinking. Specifying scope/bound for each shows the student didn't just memorize a list.

**Worked example (limitations):**
> A (EN): "Three foundational limitations, ranked by severity. First, our 4-year baseline can detect only short MM-like quiet phases, not multi-decade ones — this is the strongest constraint and bounds my candidate definition. Second, photometric variability is an indirect activity proxy compared to spectroscopic log R'HK, but our spectroscopic subsample of 28 stars validates the photometric ranking. Third, contamination from pole-on stars: 19.1% of low-i stars could be active stars seen face-on, which I bounded by removing the i<36° subsample as a sensitivity check."

---

### 1c. The "Acknowledge + Reframe + Evidence" archetype
Used for: critical questions where the judge has flagged a real concern.

> **Template (EN):** "That's a fair point. The way I'd frame it is [reframe]. The evidence I'd point to is [specific data / test]."

> **Template (中文):** "这个问题很合理。我的理解是 [重新表述]。证据是 [具体数据 / 检验]。"

**Why this works:** Never argue with the judge. Concede the point, then redirect to evidence. This is the *signature* move of mature scientists.

**Worked example:**
> Q: "Your candidate count of 795 is 250× larger than the literature value of ~3 confirmed MM stars. Doesn't that look suspicious?"
> A (EN): "That's a fair point. The way I'd frame it is that 'candidate' and 'confirmed' are different definitions. Confirmed MM stars require multi-decade chromospheric monitoring; my candidates are 4-year photometrically quiet. The evidence I'd point to is that prior systematic searches like Saar & Testa (2011) used spectroscopic subsamples of ~hundreds of stars, while I systematically search 3,339. The 250× ratio reflects 250× more stars searched and a different criterion, not a 250× detection rate."

---

### 1d. The "Reasoned uncertainty" archetype
Used for: questions the student doesn't fully know.

> **Template (EN):** "I'm not certain, but based on [data point I do know], I would estimate [reasoned guess]. To be more confident I'd need to [specific test]."

> **Template (中文):** "我不太确定，但基于 [我知道的数据点]，我估计 [合理推测]。要更确信需要 [具体验证]。"

**Why this works:** Reasoning under uncertainty is a core scientific skill. Judges *gain* confidence in students who hedge well; they lose confidence in students who bluff.

**Worked example:**
> Q: "What's the false positive rate of your pipeline?"
> A (EN): "I'm not certain — I haven't computed a formal FPR via injection-recovery. But based on the 19.1% pole-on contamination I quantified, plus the additional inclination cut at 36°, I'd estimate the residual FPR is in the 5–15% range. To be more confident I'd need to inject synthetic active stars at random orientations and measure recovery."

---

### 1e. The "Concrete, specific, scoped" archetype
Used for: future work, broader impact, "what's next."

> **Template (EN):** "By [year/timeframe], we could [specific concrete thing]. Specifically, [details]. This would tell us [specific scientific outcome]."

> **Template (中文):** "到 [年份]，可以做 [具体的事情]。具体来说，[细节]。这会回答 [具体的科学问题]。"

**Why this works:** "More research" is the worst answer. Specificity signals the student has actually thought about extensions, not just listed buzzwords.

**Worked example:**
> Q: "What's the next step?"
> A (EN): "Three concrete next steps. By 2027, ground-based spectroscopic followup of the top 50 candidates with HARPS-N to measure their Ca II H&K emission directly. By 2028, cross-match with Gaia DR4 ages — if MM candidates are systematically older, that's a strong stellar-age dependence signal. By 2030, when ESPRESSO has accumulated longer baselines, we can detect cycle reversals on timescales of years."

---

## 2. The "I don't know" recovery scripts

When the student genuinely doesn't know, they need scripted responses ready. These are far better than awkward silence or made-up answers.

### Script 1 — Genuinely no idea
- **EN:** "I'm not certain — I haven't worked through that in detail. My best guess based on [related thing I do know] would be [reasoned hypothesis], but I'd want to [specific verification] before committing to that answer."
- **中文：** "我不太确定，这部分我没深入研究过。基于 [我了解的相关内容]，我的初步猜测是 [合理假设]，但要给出确定的答案需要 [具体验证]。"

### Script 2 — Partially know
- **EN:** "I understand [what I do know], but I haven't worked through [the specific gap] in depth. What I can say is [confident partial answer]."
- **中文：** "我理解 [我掌握的部分]，但 [具体盲区] 这块我还没有深入研究。我能确定的是 [有把握的部分]。"

### Script 3 — Forgot a number
- **EN:** "Let me think — I should remember this... [pause] ...I don't want to misquote, but the value is in the range of [order-of-magnitude estimate]. The exact number is on my poster — [point]."
- **中文：** "让我想想，这个数我应该记得… [停顿] …我不想说错，大概在 [数量级] 这个范围。准确数字在海报上 [指过去]。"

### Script 4 — Judge challenges a method
- **EN:** "That's a fair point — let me reconsider. The way I originally thought about it was [original reasoning]. Hearing your concern, I think the strongest counter is [new reasoning], but you might be right that [acknowledged risk]."
- **中文：** "您这个问题很有道理，让我重新考虑一下。我原本的思路是 [原推理]。听了您的意见，我觉得最强的反驳是 [新推理]，但您可能说得对，确实存在 [承认的风险]。"

### Script 5 — Out-of-scope question
- **EN:** "That's outside the scope of my project, but it's a great question. My understanding is [brief related knowledge if any], but I haven't studied [exact topic] formally."
- **中文：** "这个问题超出了我项目的范围，但是个好问题。我的理解大概是 [简短的相关知识]，但 [确切话题] 我没有系统学过。"

---

## 3. The bilingual style guide

When generating Chinese answers, do NOT translate literally from English. Each version should sound natural in its own language.

### 3a. Technical vocabulary
| English | 中文 (preferred) | Notes |
|---|---|---|
| autocorrelation function | 自相关函数 (ACF) | Standard. Keep ACF. |
| quantile regression | 分位数回归 | Standard. |
| chromospheric activity | 色球活动 | Standard. |
| log R'HK | log R'HK | Keep English; this is a field-standard symbol. |
| CDPP | CDPP | Keep; no Chinese equivalent. |
| RMS | RMS / 均方根 | Either; RMS more common in physics labs. |
| effect size | 效应量 | Standard in statistical 中文. |
| confidence interval | 置信区间 (CI) | Standard. |
| Mann-Whitney U test | Mann-Whitney U 检验 | Keep English name. |
| pole-on / equator-on | 极向 / 赤道向 (or 正面 / 侧面) | Both work; the latter is more colloquial. |
| Maunder Minimum | 蒙德极小期 | Standard. |
| inclination | 倾角 | Standard. |
| selection effect | 选择效应 | Standard. |
| systematic error | 系统误差 | Standard. |
| photometric variability | 光度变率 | Standard. |

### 3b. Sentence-level patterns

| EN pattern | Bad literal 中文 | Natural 中文 |
|---|---|---|
| "I would estimate..." | "我会估计..." | "我估计..." |
| "That's a fair point" | "那是一个公平的观点" | "您这个问题很有道理" / "这个问题很合理" |
| "Based on my data" | "基于我的数据" | "根据我的数据" |
| "The reason is..." | "理由是..." | "原因是..." |
| "Let me think" | "让我思考" | "让我想想" |
| "I'm not certain" | "我不肯定" | "我不太确定" |
| "Specifically" | "具体地" | "具体来说" |
| "In other words" | "用其他的话说" | "换句话说" / "也就是说" |

### 3c. Register
Chinese science fair answers should be **直接、清晰、有信心 (direct, clear, confident)**, but not overly formal. Avoid:
- Excessively literary phrases ("吾人" "诚然" "不啻为")
- Bureaucratic register ("本研究指出" if the student isn't writing a paper — say "我发现" or "我的研究显示")
- Self-deprecating filler ("我也不是很懂" "可能不太对")

Good register: a sharp 11th/12th-grader who has practiced explaining their work to a Chinese-speaking professor or family member. Confident, technical, but accessible.

---

## 4. Length calibration

| Question type | Target answer length |
|---|---|
| Elevator pitch (Q1 / A1) | 90–120 seconds (~250 words EN / ~300 中文) |
| Quick concept check (Part B) | 20–30 seconds (~50 words) |
| Methodology question (Part C) | 45–60 seconds (~120 words) |
| Statistics walk-through (Part D) | 60–90 seconds (~180 words) |
| Limitations (Part F) | 60–90 seconds (~200 words) |
| Future work (Part G) | 30–45 seconds (~100 words) |
| Hypothetical (Part H) | 30–45 seconds (~100 words) |

When generating model answers, write to these lengths. **Do not write 500-word answers** — students cannot deliver those naturally and judges will lose attention.

---

## 5. The "fluency tells"

Things that signal a strong answer to judges (use in model answers when possible):

- **Hedging at the right moments:** "I think...", "based on what I observed...", "to the best of my knowledge..."
- **Naming the limit before being asked:** "...although this only works when X, and X may not hold if Y..."
- **Pointing at the poster:** "...as shown in this figure..." (write into model answers as `[point at Figure 3]`).
- **Naming a paper:** "...this is what Saar & Testa 2011 also found..."
- **Quantifying the uncertainty:** "...about 5–15%..." rather than "...some..."
- **Acknowledging the alternative interpretation:** "...this is also consistent with [other hypothesis], so I can't rule that out yet..."

Things that signal a weak answer (avoid in model answers):

- **Filler:** "uh," "um," "like," "you know"
- **Overclaim:** "definitely," "obviously," "always," "perfectly"
- **Vagueness:** "kind of," "sort of," "I guess," "or whatever"
- **Authority appeal without reasoning:** "my mentor said," "the textbook says," "it's standard"

---

## 6. How to use this file when generating

When writing model answers in the bilingual Q&A document:

1. Pick the matching **archetype** from §1 — every answer should fit one cleanly.
2. Write the **English version first** at the target length from §4, using the §5 fluency tells.
3. Write the **Chinese version** as a parallel — *not literal* — translation, using the vocabulary from §3a and the natural phrasings from §3b.
4. For Part J's "I don't know" coverage, copy the four scripts from §2 verbatim into the document.
5. For "avoid this answer" sections, draw from §5's weak-signal list to construct specific bad-sentence examples.
