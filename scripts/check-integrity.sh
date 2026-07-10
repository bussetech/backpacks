#!/usr/bin/env bash
# Referential integrity across data/. Needs python3 + pyyaml.
set -euo pipefail
cd "$(dirname "$0")/.."
exec python3 scripts/check_integrity.py "$@"
