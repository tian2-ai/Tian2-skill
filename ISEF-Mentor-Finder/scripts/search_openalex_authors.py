#!/usr/bin/env python3
"""Search OpenAlex for researchers matching a topic phrase, with reachability filters.

Uses the same curl-based HTTP layer as isef-topic-finder (Python 3.14 urllib has SSL
EOF issues with OpenAlex on some macOS Python builds; curl is reliable).

Usage:
    python3 search_openalex_authors.py \\
        --topic "MCMC sampling origami" \\
        --max-results 15 \\
        --recent-papers-only

Output: JSON to stdout. Each candidate has:
    - id (OpenAlex author ID)
    - display_name
    - last_known_institution (name + country)
    - works_count
    - cited_by_count
    - recent_papers_3y_count
    - topic_score (0-1, how well their concept profile matches the query)
    - public_orcid (if available)
    - signal flags (junior-friendly, recently active, etc.)

The student must verify email from each researcher's institutional webpage —
the script does NOT return emails (OpenAlex doesn't store them, and that's
appropriate).
"""
import argparse
import json
import shutil
import subprocess
import sys
import urllib.parse
from pathlib import Path


CURL = shutil.which("curl") or "/usr/bin/curl"
USER_AGENT = "isef-mentor-finder/0.1 (mailto:noreply@example.com)"


def http_get_json(url):
    try:
        proc = subprocess.run(
            [CURL, "-sSL", "--max-time", "25", "-A", USER_AGENT, "-H", "Accept: application/json", url],
            capture_output=True, timeout=30,
        )
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return None
    if proc.returncode != 0:
        return None
    try:
        return json.loads(proc.stdout.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        return None


def search_authors(topic, max_results=15, recent_papers_only=True):
    # Strategy: search OpenAlex /works for the topic, collect distinct author IDs from the
    # top works, then enrich via /authors.
    works_url = (
        f"https://api.openalex.org/works?"
        f"search={urllib.parse.quote(topic)}"
        f"&per-page=50&sort=cited_by_count:desc"
    )
    works_data = http_get_json(works_url)
    if not works_data:
        return {"status": "error", "reason": "OpenAlex unreachable", "authors": []}

    # Collect author IDs with counts (more papers on topic → stronger signal)
    author_counts = {}
    author_first_seen = {}
    for w in works_data.get("results", []):
        for au in w.get("authorships", []):
            aid = au.get("author", {}).get("id")
            if not aid:
                continue
            author_counts[aid] = author_counts.get(aid, 0) + 1
            if aid not in author_first_seen:
                author_first_seen[aid] = {
                    "id": aid.split("/")[-1],
                    "display_name": au["author"].get("display_name", ""),
                    "topic_paper_count": 0,
                }
            author_first_seen[aid]["topic_paper_count"] = author_counts[aid]

    # Sort by topic_paper_count
    ranked = sorted(author_first_seen.values(), key=lambda x: -x["topic_paper_count"])[:max_results]

    # Enrich each author with /authors endpoint
    enriched = []
    for r in ranked:
        adata = http_get_json(f"https://api.openalex.org/authors/{r['id']}")
        if not adata:
            continue
        inst = adata.get("last_known_institution") or {}
        recent_count = sum(
            yr.get("works_count", 0)
            for yr in adata.get("counts_by_year", [])
            if yr.get("year", 0) >= 2023
        )
        if recent_papers_only and recent_count == 0:
            continue
        enriched.append({
            "id": r["id"],
            "display_name": r["display_name"],
            "topic_paper_count_in_top50": r["topic_paper_count"],
            "last_known_institution": {
                "display_name": inst.get("display_name"),
                "country_code": inst.get("country_code"),
                "ror": inst.get("ror"),
                "type": inst.get("type"),
            } if inst else None,
            "total_works_count": adata.get("works_count"),
            "total_cited_by_count": adata.get("cited_by_count"),
            "recent_papers_3y_count": recent_count,
            "h_index": (adata.get("summary_stats") or {}).get("h_index"),
            "orcid": adata.get("orcid"),
            "openalex_url": adata.get("id"),
            "signals": _compute_signals(adata, recent_count),
            "next_step_hint": (
                f"Search Google for: '{r['display_name']}' "
                f"{(inst.get('display_name') if inst else '')} email"
                " — find their institutional webpage and use the email listed there."
            ),
        })

    return {
        "status": "ok",
        "topic": topic,
        "candidates_returned": len(enriched),
        "authors": enriched,
        "note": (
            "OpenAlex does not store email addresses, by design. To contact a candidate, "
            "search Google for their institutional faculty page and use the email listed "
            "there. Respect any stated availability notices."
        ),
    }


def _compute_signals(adata, recent_count):
    """Soft flags surfaced to the student."""
    signals = []
    if recent_count >= 3:
        signals.append("recently_active")
    elif recent_count == 0:
        signals.append("inactive_3y")
    if (adata.get("works_count") or 0) > 20 and recent_count >= 5:
        signals.append("established_and_active")
    if adata.get("orcid"):
        signals.append("has_orcid")
    inst = adata.get("last_known_institution") or {}
    if inst.get("type") == "education":
        signals.append("university_affiliated")
    elif inst.get("type") == "company":
        signals.append("industry_affiliated")
    return signals


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--topic", required=True)
    p.add_argument("--max-results", type=int, default=15)
    p.add_argument("--recent-papers-only", action="store_true", default=True)
    p.add_argument("--include-inactive", action="store_true", help="Include authors with no papers in last 3y")
    args = p.parse_args()
    result = search_authors(
        args.topic,
        max_results=args.max_results,
        recent_papers_only=not args.include_inactive,
    )
    print(json.dumps(result, indent=2))
    return 0 if result.get("status") == "ok" else 1


if __name__ == "__main__":
    sys.exit(main())
