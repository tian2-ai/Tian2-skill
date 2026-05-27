# Contract tests

**Phase 4 deliverable.** Currently empty.

Each external dependency gets a fixture-based contract test that:
1. Stores a known-good API response in `fixtures/<source>.json`
2. Asserts that the parser in `scripts/search_<source>.py` correctly extracts the expected fields from the fixture
3. Optionally: replays the fixture against a live API call (skipped in CI; manual only) to detect schema drift

Files to create in Phase 4:
- `test_openalex_contract.py` (+ `fixtures/openalex.json`)
- `test_pubmed_contract.py` (+ `fixtures/pubmed.xml`)
- `test_biorxiv_contract.py` (+ `fixtures/biorxiv.json`)
- `test_arxiv_contract.py` (+ `fixtures/arxiv.xml`)
- `test_perplexity_contract.py` (+ `fixtures/perplexity.json`)

Each test must run in < 1s (no network). Run with:

```
python -m pytest scripts/contracts/
```

When a contract test fails, it signals that the upstream API's schema changed — the corresponding `search_<source>.py` parser needs updating before scoring is reliable again.
