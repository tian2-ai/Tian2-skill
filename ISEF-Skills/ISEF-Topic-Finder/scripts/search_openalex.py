#!/usr/bin/env python3
"""search_openalex.py — direct HTTPS to api.openalex.org.

Three queries:
- Q1: topic velocity (group_by=publication_year over last 5 years)
- Q2: top citation density (sort by cited_by_count)
- Q3 (skipped here; intersection mining requires pre-resolved concept IDs)

Output schema (consumed by score_topic.py):
  status, papers_per_year (dict year→count), trend_slope, top_papers,
  category_normalized_percentile (placeholder — see notes)

Cache TTL: 30 days. No API key required.
"""
import argparse
import json
import sys
import urllib.parse
from _http_cache import http_get, read_cache, write_cache


TTL_SECONDS = 30 * 24 * 3600
CATEGORY_PLACEHOLDER_PERCENTILES = {
    # Until data/category_distributions.json is built (Phase 3.5), use rough fallbacks.
    # Maps an absolute papers/year value to a percentile within the category.
    "MATH": [(2, 5), (10, 30), (30, 70), (80, 90)],
    "PHYS": [(3, 5), (10, 30), (60, 70), (200, 90)],
    "BMED": [(5, 5), (20, 30), (150, 70), (500, 90)],
    "CHEM": [(5, 5), (15, 30), (80, 70), (300, 90)],
    "SFTD": [(10, 5), (50, 30), (300, 70), (1000, 90)],
    "CBIO": [(10, 5), (50, 30), (300, 70), (1000, 90)],
    "ROBO": [(10, 5), (50, 30), (300, 70), (1000, 90)],
}
DEFAULT_PCT_TABLE = [(3, 5), (10, 30), (80, 70), (250, 90)]


def papers_per_year_to_percentile(ppy: int, category: str) -> int:
    table = CATEGORY_PLACEHOLDER_PERCENTILES.get(category, DEFAULT_PCT_TABLE)
    last_pct = 5
    for threshold, pct in table:
        if ppy < threshold:
            return last_pct + (pct - last_pct) // 2
        last_pct = pct
    return 95


def compute_trend_slope(by_year: dict) -> float:
    """Simple least-squares slope on (year, count). Returns 0 if insufficient data."""
    items = sorted((int(y), c) for y, c in by_year.items() if c is not None)
    if len(items) < 2:
        return 0.0
    n = len(items)
    sum_x = sum(x for x, _ in items)
    sum_y = sum(y for _, y in items)
    sum_xy = sum(x * y for x, y in items)
    sum_xx = sum(x * x for x, _ in items)
    denom = n * sum_xx - sum_x * sum_x
    if denom == 0:
        return 0.0
    return (n * sum_xy - sum_x * sum_y) / denom


def search(topic: str, category: str, max_papers: int = 10) -> dict:
    cached = read_cache("openalex", f"{category}::{topic}", TTL_SECONDS)
    if cached is not None:
        cached["status"] = "ok_cached"
        return cached

    # Q1: velocity
    q1 = f"https://api.openalex.org/works?search={urllib.parse.quote(topic)}&per-page=200&group_by=publication_year"
    code, body = http_get(q1, accept="application/json")
    if code != 200:
        return {"source": "openalex", "status": "unavailable", "reason": f"HTTP {code}"}
    try:
        velocity_data = json.loads(body.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        return {"source": "openalex", "status": "unavailable", "reason": "JSON parse failed on Q1"}
    by_year = {item["key"]: item["count"] for item in velocity_data.get("group_by", []) if item.get("key")}
    # Filter to last 5 years for trend
    recent = {y: c for y, c in by_year.items() if y.isdigit() and 2020 <= int(y) <= 2026}

    # Q2: top papers
    q2 = f"https://api.openalex.org/works?search={urllib.parse.quote(topic)}&per-page={max_papers}&sort=cited_by_count:desc"
    code2, body2 = http_get(q2)
    top_papers = []
    if code2 == 200:
        try:
            d = json.loads(body2.decode("utf-8"))
            for w in d.get("results", []):
                top_papers.append({
                    "title": (w.get("title") or "")[:200],
                    "year": w.get("publication_year"),
                    "id": w.get("id", "").split("/")[-1],
                    "cited_by_count": w.get("cited_by_count", 0),
                    "why_it_matters": "",  # filled by Claude downstream
                })
        except (UnicodeDecodeError, json.JSONDecodeError):
            pass

    # Percentile (placeholder until category_distributions.json exists)
    recent_total = sum(recent.values())
    recent_count_years = max(1, len(recent))
    ppy = recent_total // recent_count_years
    percentile = papers_per_year_to_percentile(ppy, category)

    result = {
        "source": "openalex",
        "status": "ok",
        "papers_per_year": recent,
        "papers_per_year_avg": ppy,
        "category_normalized_percentile": percentile,
        "trend_slope": round(compute_trend_slope(recent), 3),
        "top_papers": top_papers,
        "note": "percentile uses placeholder table; build data/category_distributions.json to refine",
    }
    write_cache("openalex", f"{category}::{topic}", result)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--topic", required=True)
    parser.add_argument("--category", required=True)
    parser.add_argument("--max-papers", type=int, default=10)
    args = parser.parse_args()
    result = search(args.topic, args.category, args.max_papers)
    json.dump(result, sys.stdout, indent=2)
    return 0


if __name__ == "__main__":
    sys.exit(main())
