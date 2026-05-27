#!/usr/bin/env python3
"""search_biorxiv.py — direct HTTPS to api.biorxiv.org.

bioRxiv has no built-in keyword search; we pull the last-180-days date range
and do local token matching. This is rough — appropriate for M3 freshness signal,
not for substantive citation discovery.

Cache TTL: 14 days. No API key required.
"""
import argparse
import datetime as dt
import json
import sys
import re
from _http_cache import http_get, read_cache, write_cache


TTL_SECONDS = 14 * 24 * 3600
STOPWORDS = {"the", "of", "and", "for", "with", "from", "to", "in", "on", "by"}


def search(topic: str, max_results: int = 10) -> dict:
    cached = read_cache("biorxiv", topic, TTL_SECONDS)
    if cached is not None:
        cached["status"] = "ok_cached"
        return cached

    end = dt.date.today()
    start = end - dt.timedelta(days=180)
    url = f"https://api.biorxiv.org/details/biorxiv/{start.isoformat()}/{end.isoformat()}/0"
    code, body = http_get(url, accept="application/json", timeout=30)
    if code != 200:
        return {"source": "biorxiv", "status": "unavailable", "reason": f"HTTP {code}"}
    try:
        data = json.loads(body.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        return {"source": "biorxiv", "status": "unavailable", "reason": "JSON parse failed"}

    tokens = {t.lower() for t in re.findall(r"\w+", topic) if len(t) > 2 and t.lower() not in STOPWORDS}
    if not tokens:
        return {"source": "biorxiv", "status": "ok", "preprints_last_6mo": []}

    matches = []
    for entry in data.get("collection", []):
        title = (entry.get("title") or "").lower()
        abstract = (entry.get("abstract") or "").lower()
        text_tokens = set(re.findall(r"\w+", title + " " + abstract))
        overlap = len(tokens & text_tokens)
        if overlap >= max(2, len(tokens) // 2):
            matches.append({
                "title": (entry.get("title") or "")[:200],
                "year": int((entry.get("date") or "0000")[:4]) if (entry.get("date") or "").startswith(("19", "20")) else None,
                "id": entry.get("doi", ""),
                "doi": entry.get("doi", ""),
                "match_strength": overlap / max(1, len(tokens)),
            })
        if len(matches) >= max_results:
            break

    matches.sort(key=lambda m: m["match_strength"], reverse=True)
    result = {
        "source": "biorxiv",
        "status": "ok",
        "preprints_last_6mo": matches[:max_results],
        "date_range": [start.isoformat(), end.isoformat()],
        "total_scanned": len(data.get("collection", [])),
    }
    write_cache("biorxiv", topic, result)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--topic", required=True)
    parser.add_argument("--max-results", type=int, default=10)
    args = parser.parse_args()
    result = search(args.topic, args.max_results)
    json.dump(result, sys.stdout, indent=2)
    return 0


if __name__ == "__main__":
    sys.exit(main())
