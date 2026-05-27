#!/usr/bin/env python3
"""
search_isef_archive.py — local TF-IDF over ISEF-Scrape JSON corpus.

Reads project inventories from $ISEF_SCRAPE_ROOT (with fallback chain). Each
inventory file has shape {"years": [...], "projects": [{title, year, category_code, ...}]}.
Builds a TF-IDF index over titles (no abstracts available in the inventories),
computes cosine similarity to the query topic, and returns the M4 modulator
arm decision per the rubric.

M4 arms (see references/rubric-topic-stage-extensions.md §3):
- cargo_cult_penalty:    same category, last 5 years, similarity > 0.6 → −5
- cross_category_bonus:  different category, similarity > 0.5 → +2
- no_signal:             everything else, or sparse coverage → 0
"""
import argparse
import hashlib
import json
import math
import os
import re
import sys
import time
from collections import Counter
from pathlib import Path
from typing import Optional


TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z0-9]{2,}")
STOPWORDS = {
    "the", "and", "for", "with", "from", "that", "this", "into", "their",
    "using", "based", "study", "effect", "effects", "investigation",
    "analysis", "novel", "new", "use", "uses", "via", "are", "was", "were",
    "its", "his", "her", "they", "them", "our", "your", "you", "have",
    "has", "had", "will", "would", "could", "should", "can", "may", "might",
}


def resolve_isef_scrape_root() -> Optional[str]:
    env = os.environ.get("ISEF_SCRAPE_ROOT")
    if env and os.path.isdir(env):
        return env
    for candidate in [
        os.path.expanduser("~/ISEF-Scrape/output"),
        "/Volumes/Mac-Mini/workspaces/tian2-edu/ISEF-Scrape/output",
    ]:
        if os.path.isdir(candidate):
            return candidate
    return None


def tokenize(text: str) -> list[str]:
    if not text:
        return []
    cleaned = re.sub(r"^[A-Z]{3,5}\d+\s*-\s*", "", text)  # strip "ANIM052 - "
    tokens = [t.lower() for t in TOKEN_RE.findall(cleaned)]
    return [t for t in tokens if t not in STOPWORDS and len(t) > 2]


def load_corpus(root: str) -> list[dict]:
    """Load all project records from the ISEF-Scrape outputs.

    Looks for `*/project-inventory.json` files under root. Skips the
    enbm080-* singleton files (different schema)."""
    records = []
    for inventory in Path(root).glob("*/project-inventory.json"):
        try:
            with open(inventory) as f:
                data = json.load(f)
        except (json.JSONDecodeError, OSError):
            continue
        for p in data.get("projects", []):
            title = p.get("title") or ""
            year = p.get("year")
            cat = p.get("category_code") or ""
            if title and cat:
                records.append({
                    "title": title,
                    "tokens": tokenize(title),
                    "year": year,
                    "category": cat,
                    "url": p.get("url", ""),
                    "slug": p.get("slug", ""),
                })
    return records


def build_idf(corpus: list[dict]) -> dict[str, float]:
    n = len(corpus)
    df = Counter()
    for rec in corpus:
        for tok in set(rec["tokens"]):
            df[tok] += 1
    return {tok: math.log((n + 1) / (df_count + 1)) + 1 for tok, df_count in df.items()}


def tfidf_vec(tokens: list[str], idf: dict[str, float]) -> dict[str, float]:
    if not tokens:
        return {}
    tf = Counter(tokens)
    norm = math.sqrt(sum((c / len(tokens)) ** 2 for c in tf.values()))
    if norm == 0:
        return {}
    return {tok: (count / len(tokens)) * idf.get(tok, 1.0) for tok, count in tf.items()}


def cosine(a: dict[str, float], b: dict[str, float]) -> float:
    if not a or not b:
        return 0.0
    common = set(a) & set(b)
    if not common:
        return 0.0
    dot = sum(a[k] * b[k] for k in common)
    na = math.sqrt(sum(v * v for v in a.values()))
    nb = math.sqrt(sum(v * v for v in b.values()))
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)


def search(topic: str, category: str, top_k: int = 5, exclude_slug: Optional[str] = None) -> dict:
    root = resolve_isef_scrape_root()
    if not root:
        return {
            "source": "isef_archive",
            "status": "unavailable",
            "reason": "ISEF_SCRAPE_ROOT not set and no fallback path exists",
            "m4_value": 0,
            "m4_arm": "no_signal",
        }
    t0 = time.time()
    corpus = load_corpus(root)
    if not corpus:
        return {
            "source": "isef_archive",
            "status": "empty",
            "reason": f"no project inventories found under {root}",
            "m4_value": 0,
            "m4_arm": "no_signal",
        }
    idf = build_idf(corpus)
    query_tokens = tokenize(topic)
    qv = tfidf_vec(query_tokens, idf)

    current_year = 2026
    recent_threshold = current_year - 5

    sims_in = []
    sims_out = []
    for rec in corpus:
        if exclude_slug and rec["slug"] == exclude_slug:
            continue
        sim = cosine(qv, tfidf_vec(rec["tokens"], idf))
        if sim < 0.2:
            continue
        item = {"title": rec["title"], "year": rec["year"], "category": rec["category"], "similarity": round(sim, 3), "slug": rec["slug"]}
        if rec["category"] == category and isinstance(rec["year"], int) and rec["year"] >= recent_threshold:
            sims_in.append(item)
        elif rec["category"] != category:
            sims_out.append(item)

    sims_in.sort(key=lambda r: r["similarity"], reverse=True)
    sims_out.sort(key=lambda r: r["similarity"], reverse=True)
    sims_in = sims_in[:top_k]
    sims_out = sims_out[:top_k]

    # M4 arm decision
    m4_value = 0
    m4_arm = "no_signal"
    if sims_in and sims_in[0]["similarity"] > 0.6:
        m4_value = -5
        m4_arm = "cargo_cult_penalty"
    elif sims_out and sims_out[0]["similarity"] > 0.5:
        m4_value = 2
        m4_arm = "cross_category_bonus"

    # Sparse-coverage check: if same-category-last-5y has < 50 records, suppress signal
    same_cat_recent = sum(
        1 for r in corpus
        if r["category"] == category and isinstance(r["year"], int) and r["year"] >= recent_threshold
    )
    if same_cat_recent < 50 and m4_arm == "cargo_cult_penalty":
        # Be conservative: not enough archive coverage to assert cargo-cult
        m4_value = 0
        m4_arm = "no_signal_sparse_coverage"

    return {
        "source": "isef_archive",
        "status": "ok",
        "root": root,
        "corpus_size": len(corpus),
        "same_category_recent_count": same_cat_recent,
        "matches_in_category": sims_in,
        "matches_cross_category": sims_out,
        "m4_value": m4_value,
        "m4_arm": m4_arm,
        "query_token_count": len(query_tokens),
        "search_time_seconds": round(time.time() - t0, 2),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--topic", required=True)
    parser.add_argument("--category", required=True)
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--exclude-slug", default=None, help="Skip this slug (used during back-testing to avoid self-matches)")
    args = parser.parse_args()
    result = search(args.topic, args.category, args.top_k, args.exclude_slug)
    json.dump(result, sys.stdout, indent=2)
    return 0


if __name__ == "__main__":
    sys.exit(main())
