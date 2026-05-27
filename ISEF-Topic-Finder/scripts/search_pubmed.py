#!/usr/bin/env python3
"""search_pubmed.py — direct HTTPS to NCBI E-utilities.

Two-step: esearch → efetch. Returns top N PMIDs with titles, abstracts (truncated), years.

NCBI rate limit: 3 req/sec without API key. We sleep between the two calls.
Cache TTL: 14 days.
"""
import argparse
import json
import sys
import time
import urllib.parse
import xml.etree.ElementTree as ET
from _http_cache import http_get, read_cache, write_cache


TTL_SECONDS = 14 * 24 * 3600
BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"


def search(topic: str, max_results: int = 10) -> dict:
    cached = read_cache("pubmed", topic, TTL_SECONDS)
    if cached is not None:
        cached["status"] = "ok_cached"
        return cached

    esearch_url = (
        f"{BASE}/esearch.fcgi?db=pubmed&retmode=json&retmax={max_results}"
        f"&term={urllib.parse.quote(topic)}&tool=isef-topic-finder"
    )
    code, body = http_get(esearch_url, accept="application/json")
    if code != 200:
        return {"source": "pubmed", "status": "unavailable", "reason": f"esearch HTTP {code}"}
    try:
        idlist = json.loads(body.decode("utf-8"))["esearchresult"]["idlist"]
    except (UnicodeDecodeError, json.JSONDecodeError, KeyError):
        return {"source": "pubmed", "status": "unavailable", "reason": "esearch parse failed"}

    if not idlist:
        result = {"source": "pubmed", "status": "ok", "papers": [], "total_hits": 0}
        write_cache("pubmed", topic, result)
        return result

    time.sleep(0.4)  # be polite to NCBI
    efetch_url = (
        f"{BASE}/efetch.fcgi?db=pubmed&id={','.join(idlist)}&retmode=xml&tool=isef-topic-finder"
    )
    code2, body2 = http_get(efetch_url, accept="application/xml")
    if code2 != 200:
        return {"source": "pubmed", "status": "unavailable", "reason": f"efetch HTTP {code2}"}

    papers = []
    try:
        root = ET.fromstring(body2)
        for art in root.findall(".//PubmedArticle"):
            pmid = (art.findtext(".//PMID") or "").strip()
            title = (art.findtext(".//ArticleTitle") or "").strip()[:200]
            year = (art.findtext(".//PubDate/Year") or "").strip()
            abstract = ""
            ab = art.find(".//Abstract")
            if ab is not None:
                abstract = " ".join((t.text or "") for t in ab.findall("AbstractText"))[:300]
            papers.append({
                "title": title,
                "year": int(year) if year.isdigit() else None,
                "id": pmid, "pmid": pmid,
                "abstract": abstract,
            })
    except ET.ParseError as e:
        return {"source": "pubmed", "status": "unavailable", "reason": f"efetch XML parse: {e}"}

    result = {"source": "pubmed", "status": "ok", "papers": papers, "total_hits": len(idlist)}
    write_cache("pubmed", topic, result)
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
