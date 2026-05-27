#!/usr/bin/env python3
"""cross_validate.py — orchestrate parallel fan-out across 5 sources.

4 sources call HTTP APIs via curl (real parallelism via ThreadPoolExecutor).
1 source (perplexity) is intentionally serial — wrap of a Claude skill, not HTTP.
1 source (isef_archive) is local TF-IDF.

CLI:
    python cross_validate.py --topic "..." --category PHYS [--skip perplexity,pubmed]

Output: merged evidence pack matching the schema score_topic.py consumes.

Cache TTLs are per-source (set inside each search_*.py).

Determinism note (A6): the local-archive + HTTP responses are deterministic given
identical caches. Concurrent execution does not affect the merged JSON because
each source's output goes to a named key.
"""
import argparse
import importlib.util
import json
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


SCRIPT_DIR = Path(__file__).parent


def _import_search(module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, SCRIPT_DIR / f"{module_name}.py")
    if spec is None or spec.loader is None:
        return None
    mod = importlib.util.module_from_spec(spec)
    # add SCRIPT_DIR to sys.path so internal `from _http_cache import ...` works
    if str(SCRIPT_DIR) not in sys.path:
        sys.path.insert(0, str(SCRIPT_DIR))
    try:
        spec.loader.exec_module(mod)
    except Exception:  # noqa: BLE001
        return None
    return mod


def fan_out(topic: str, category: str, skip: set[str]) -> dict:
    """Run all sources concurrently and merge into evidence pack."""
    evidence = {}

    # Build the task table: (source_name, callable)
    tasks: list[tuple[str, callable]] = []

    # Capture each module via default-argument to avoid closure-over-loop pitfall.
    if "openalex" not in skip:
        m = _import_search("search_openalex")
        if m:
            tasks.append(("openalex", lambda mod=m: mod.search(topic, category)))

    if "arxiv" not in skip:
        m = _import_search("search_arxiv")
        if m:
            tasks.append(("arxiv", lambda mod=m: mod.search(topic)))

    if "pubmed" not in skip:
        m = _import_search("search_pubmed")
        if m and category in {"BMED", "CELL", "MCRO", "BCHM", "TMED", "BEHA", "ANIM", "PLNT", "ENBM"}:
            tasks.append(("pubmed", lambda mod=m: mod.search(topic)))

    if "biorxiv" not in skip:
        m = _import_search("search_biorxiv")
        if m and category in {"BMED", "CELL", "MCRO", "BCHM", "ANIM", "PLNT", "ENBM"}:
            tasks.append(("biorxiv", lambda mod=m: mod.search(topic)))

    if "isef_archive" not in skip:
        m = _import_search("search_isef_archive")
        if m:
            tasks.append(("isef_archive", lambda mod=m: mod.search(topic, category)))

    # Perplexity is skill-wrapped, not HTTP. Mark unavailable for now;
    # the calling flow (Claude) is responsible for invoking /perplexity-search
    # if M2 needs to be populated.
    if "perplexity" not in skip:
        evidence["perplexity"] = {
            "source": "perplexity",
            "status": "unavailable",
            "reason": "perplexity is skill-wrapped; calling flow must invoke /perplexity-search to populate",
        }

    # Fan out the HTTP/local tasks
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=min(8, max(1, len(tasks)))) as pool:
        future_to_name = {pool.submit(fn): name for name, fn in tasks}
        for fut in as_completed(future_to_name):
            name = future_to_name[fut]
            try:
                evidence[name] = fut.result()
            except Exception as e:  # noqa: BLE001
                evidence[name] = {"source": name, "status": "error", "reason": f"{type(e).__name__}: {e}"}

    evidence["_meta"] = {
        "topic": topic,
        "category": category,
        "fan_out_seconds": round(time.time() - t0, 2),
        "sources_attempted": list(future_to_name.values() if 'future_to_name' in dir() else [name for name, _ in tasks]),
    }
    return evidence


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--topic", required=True)
    parser.add_argument("--category", required=True)
    parser.add_argument("--skip", default="", help="Comma-separated source names to skip")
    args = parser.parse_args()
    skip = {s.strip() for s in args.skip.split(",") if s.strip()}
    evidence = fan_out(args.topic, args.category, skip)
    json.dump(evidence, sys.stdout, indent=2)
    return 0


if __name__ == "__main__":
    sys.exit(main())
