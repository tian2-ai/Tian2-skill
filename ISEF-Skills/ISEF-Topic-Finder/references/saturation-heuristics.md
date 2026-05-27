# Saturation Heuristics (OpenAlex query templates)

**Purpose:** Compute T1.1.c "anti-saturation" sub-score and M1 "trend velocity" modulator. Both depend on **category-normalized** OpenAlex percentiles (NOT absolute paper-count thresholds, which were the Critic's v1 MAJOR on M1 arbitrariness).

## §1 — Why category-normalized percentiles, not absolute thresholds

A v1 draft used "10–80 papers/year" as the sweet spot. This is wrong:
- MATH publishes far fewer papers/year than ML — what's "saturated" in MATH is "vapor" in ML
- Even within a category, sub-categories vary by 10×
- Trends shift year to year

Category-normalized percentile fixes this. Compute papers-per-year for the topic's concept cluster, then express as a percentile within the category's concept-cluster distribution.

## §2 — OpenAlex query templates

For each topic, run THREE queries in parallel:

### Q1 — Topic velocity (exact phrase)
```
GET https://api.openalex.org/works?
  search=<URL-encoded exact topic phrase>
  &filter=publication_year:>=2021,publication_year:<=2025
  &per-page=200
  &group_by=publication_year
```
Returns yearly counts. Compute slope of last 4 years (trend velocity).

### Q2 — Citation density
```
GET https://api.openalex.org/works?
  search=<URL-encoded topic phrase> NOT review
  &filter=publication_year:>=2022
  &per-page=10
  &sort=cited_by_count:desc
```
Returns top-10 substantive papers. Use for anchor citations + citation density signal.

### Q3 — Intersection mining (cross-disciplinary verification)
```
GET https://api.openalex.org/works?
  filter=concepts.id:<concept1_id>,concepts.id:<concept2_id>
  &per-page=50
```
Returns papers that bridge the two concepts. Used to verify the cross-disciplinary bridge is real and rare.

## §3 — Category-normalized percentile computation

Pseudocode for the percentile:

```python
def category_normalized_percentile(topic_papers_per_year, category):
    # Get distribution of papers-per-year for ALL concept clusters in this category
    # (precomputed and cached in data/category_distributions.json, refreshed monthly)
    distribution = load_category_distribution(category)
    percentile = stats.percentileofscore(distribution, topic_papers_per_year)
    return percentile
```

`data/category_distributions.json` is built by querying OpenAlex for each ISEF category's parent OpenAlex concepts and computing the distribution of papers-per-year across sub-concepts within each. Refreshed monthly. Until built, use these placeholder thresholds (rough — replace ASAP):

| Category | Vapor (< 5th pct) | Sweet (30–70 pct) | Saturated (> 90th pct) |
|----------|-------------------|---------------------|---------------------------|
| MATH | < 2 papers/year | 5–30 | > 80 |
| PHYS | < 3 | 10–60 | > 200 |
| BMED | < 5 | 20–150 | > 500 |
| CHEM | < 5 | 15–80 | > 300 |
| SFTD/CBIO/ROBO (ML-heavy) | < 10 | 50–300 | > 1000 |
| All others | < 3 | 10–80 | > 250 |

These are placeholders — replace with computed percentiles by Phase 3.

## §4 — Scoring mapping

```
T1.1.c (anti-saturation, max 10 pts):
  10–80 pct      → 10/10
  5–10 or 80–90  → 6/10
  < 5 or > 90    → 2/10

M1 (trend velocity, ±5):
  30–70 pct + rising slope         → +5
  30–70 pct + flat slope           → +3
  10–30 or 70–90 pct + rising      → +2
  < 5 pct OR > 90 pct              → −3 to −5
  < 5 pct AND no preprints in M3   → −5 (genuine vapor)
  > 90 pct AND high citation density → −5 (genuine saturation)
```

## §5 — Failure handling

If OpenAlex is unreachable, M1 is omitted, T1.1.c uses Claude inference fallback (rough category-knowledge prior), and the score is widened to the next confidence band per `rubric-topic-stage-extensions.md` §4.2.

Output marks the source as `OpenAlex: unavailable` in the scorecard's `missing_sources` array.

## §6 — Caching policy

- Q1 (topic velocity) cached 30 days
- Q2 (citation density) cached 30 days
- Q3 (intersection mining) cached 30 days
- Category distributions refreshed monthly

Cache key = sha256(query_url). Stored in `data/cache/openalex/<hash>.json`.
