#!/usr/bin/env python3
"""search_arxiv.py — direct HTTPS to export.arxiv.org/api/query.

Returns Atom XML; parses with xml.etree.ElementTree (stdlib).
Filters to papers from the last 6 months for M3 (preprint freshness).

Cache TTL: 14 days. No API key required.
"""
import argparse
import datetime as dt
import json
import sys
import urllib.parse
import xml.etree.ElementTree as ET
from _http_cache import http_get, read_cache, write_cache


TTL_SECONDS = 14 * 24 * 3600
ATOM_NS = "{http://www.w3.org/2005/Atom}"


def search(topic: str, max_results: int = 20) -> dict:
    cached = read_cache("arxiv", topic, TTL_SECONDS)
    if cached is not None:
        cached["status"] = "ok_cached"
        return cached

    # arXiv expects "all:tok1 AND all:tok2 AND ..." (space-separated; URL encoder turns to %20).
    # Drop short stopwords; cap tokens to keep query within URL length limits.
    tokens = [t for t in topic.split() if len(t) > 2][:6]
    if not tokens:
        return {"source": "arxiv", "status": "ok", "papers_last_6mo": [], "all_papers": [], "total_results_returned": 0}
    query = " AND ".join(f"all:{t}" for t in tokens)
    url = (
        f"https://export.arxiv.org/api/query?search_query={urllib.parse.quote(query)}"
        f"&start=0&max_results={max_results}&sortBy=submittedDate&sortOrder=descending"
    )
    code, body = http_get(url, accept="application/atom+xml")
    if code != 200:
        return {"source": "arxiv", "status": "unavailable", "reason": f"HTTP {code}"}

    try:
        root = ET.fromstring(body)
    except ET.ParseError as e:
        return {"source": "arxiv", "status": "unavailable", "reason": f"XML parse: {e}"}

    six_months_ago = (dt.datetime.utcnow() - dt.timedelta(days=180)).isoformat()
    all_papers = []
    recent = []
    for entry in root.findall(f"{ATOM_NS}entry"):
        title = (entry.findtext(f"{ATOM_NS}title") or "").strip()
        published = (entry.findtext(f"{ATOM_NS}published") or "").strip()
        idfield = (entry.findtext(f"{ATOM_NS}id") or "").strip()
        arxiv_id = idfield.split("/abs/")[-1] if "/abs/" in idfield else idfield
        year = None
        if published:
            try:
                year = int(published[:4])
            except ValueError:
                pass
        paper = {"title": title[:200], "year": year, "id": arxiv_id, "published": published}
        all_papers.append(paper)
        if published > six_months_ago:
            recent.append(paper)

    result = {
        "source": "arxiv",
        "status": "ok",
        "total_results_returned": len(all_papers),
        "papers_last_6mo": recent,
        "all_papers": all_papers[:max_results],
    }
    write_cache("arxiv", topic, result)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--topic", required=True)
    parser.add_argument("--max-results", type=int, default=20)
    args = parser.parse_args()
    result = search(args.topic, args.max_results)
    json.dump(result, sys.stdout, indent=2)
    return 0


if __name__ == "__main__":
    sys.exit(main())
