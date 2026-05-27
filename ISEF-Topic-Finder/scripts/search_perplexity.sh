#!/usr/bin/env bash
# search_perplexity.sh — skill-wrap of the perplexity-search skill.
#
# Phase 3 deliverable. Currently a stub.
#
# Only source that's skill-wrapped (no public HTTP API alternative).
# This means cross_validate.py serializes the Perplexity call (others parallel).
#
# Query: "<topic>" high school OR undergraduate research
# Returns: accessibility signal for M2 (HS precedent / open-source kits / industry-only).
# Cache: data/cache/perplexity/<sha256(query)>.json with 7-day TTL.
#
# Usage: ./search_perplexity.sh "topic phrase"
set -euo pipefail

TOPIC="${1:?usage: $0 \"topic\"}"

# Phase 3 work: actually invoke perplexity-search skill via claude command or
# a bridge. For now emit a stub JSON.
cat <<EOF
{
  "source": "perplexity",
  "status": "stub",
  "topic": "$TOPIC",
  "accessibility_signal": null,
  "hs_precedent_found": false
}
EOF
