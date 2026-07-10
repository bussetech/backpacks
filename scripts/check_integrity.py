#!/usr/bin/env python3
"""Referential integrity for the backpacks dataset.

Schema validation proves each file is well-formed. This proves the files
agree with each other: every citation resolves, every id is stable, and no
record claims a signal or a maker that does not exist.

The rule this enforces above all: a published value traces to a signal, and
a signal traces to a registered source. A dataset whose provenance chain has
a hole in it is worse than one with fewer entries.
"""
import pathlib
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
errors: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def load(path: pathlib.Path):
    return yaml.safe_load(path.read_text())


sources = {s["id"]: s for s in load(ROOT / "data" / "sources.yml")["sources"]}
operators = {o["id"]: o for o in load(ROOT / "data" / "operators.yml")}

signals = {}
for p in sorted((ROOT / "data" / "signals").glob("*.yml")):
    sig = load(p)
    if sig["id"] != p.stem:
        err(f"signal id {sig['id']!r} != filename stem {p.stem!r}")
    signals[sig["id"]] = sig

sites = {}
for p in sorted((ROOT / "data" / "sites").glob("*.yml")):
    rec = load(p)
    if rec["id"] != p.stem:
        err(f"record id {rec['id']!r} != filename stem {p.stem!r}")
    sites[rec["id"]] = rec

# --- signals -----------------------------------------------------------------
for sid, sig in signals.items():
    if sig["source"] not in sources:
        err(f"{sid}: source {sig['source']!r} is not in data/sources.yml")
    subject = sig.get("subject_id")
    if subject:
        if sig["subject_type"] == "pack" and subject not in sites:
            err(f"{sid}: subject_id {subject!r} is not a record in data/sites/")
        if sig["subject_type"] == "maker" and subject not in operators:
            err(f"{sid}: subject_id {subject!r} is not a maker in data/operators.yml")
    for other in sig.get("conflicts_with", []):
        if other not in signals:
            err(f"{sid}: conflicts_with {other!r} does not exist")
        elif sid not in signals[other].get("conflicts_with", []):
            err(f"{sid}: conflicts_with {other!r} is not reciprocated — a disagreement has two sides")

# --- records -----------------------------------------------------------------
for rid, rec in sites.items():
    if rec["maker"] not in operators:
        err(f"{rid}: maker {rec['maker']!r} is not in data/operators.yml")
    for sig_id in rec.get("signals", []):
        if sig_id not in signals:
            err(f"{rid}: cites signal {sig_id!r}, which does not exist")
        elif signals[sig_id].get("subject_id") != rid:
            err(f"{rid}: cites signal {sig_id!r}, whose subject is {signals[sig_id].get('subject_id')!r}")
    if not rec.get("signals"):
        err(f"{rid}: has no signals — every published value must trace to one")

# --- makers ------------------------------------------------------------------
for oid, op in operators.items():
    parent = op.get("parent")
    if parent and parent not in operators:
        err(f"{oid}: parent {parent!r} is not a registered entity")
    if op.get("status") == "acquired" and not parent:
        err(f"{oid}: status is 'acquired' but no parent is named")
    if op.get("acquired_date") and not parent:
        err(f"{oid}: has an acquired_date but no parent")

# --- the fetch allowlist -----------------------------------------------------
# ADR-0046: this registry is entirely manual. If that ever changes, it must
# change deliberately — an `active` source appearing by accident means a
# fetcher is about to hit someone's server.
for sid, s in sources.items():
    if s["status"] == "active":
        err(f"{sid}: status is 'active', but ADR-0046 records this registry as entirely manual. "
            f"Flipping a source to active is a decision, not an edit: amend the ADR in the same PR.")

# --- page stubs --------------------------------------------------------------
stub_dir = ROOT / "packs"
stubs = {p.stem for p in stub_dir.glob("*.md")} if stub_dir.is_dir() else set()
missing = set(sites) - stubs
extra = stubs - set(sites)
if missing:
    err(f"page stubs missing for: {', '.join(sorted(missing))} — run scripts/gen-pages.sh")
if extra:
    err(f"orphan page stubs: {', '.join(sorted(extra))} — run scripts/gen-pages.sh")

# --- the derived index -------------------------------------------------------
# data/packs_index.yml is generated. If it drifts from data/sites/, the site
# renders numbers that no record backs — the exact failure this dataset exists
# to prevent.
index_path = ROOT / "data" / "packs_index.yml"
if not index_path.is_file():
    err("data/packs_index.yml is missing — run scripts/gen-pages.sh")
else:
    index = load(index_path) or []
    indexed = {row["id"] for row in index}
    if indexed != set(sites):
        err("data/packs_index.yml is out of sync with data/sites/ — run scripts/gen-pages.sh")
    else:
        for row in index:
            rec = sites[row["id"]]
            if row["name"] != rec["name"] or row["status"] != rec["status"]:
                err(f"{row['id']}: packs_index.yml disagrees with the record — run scripts/gen-pages.sh")
            if row.get("capacity_l") != rec.get("specs", {}).get("capacity_l"):
                err(f"{row['id']}: packs_index.yml capacity disagrees with the record — run scripts/gen-pages.sh")

if errors:
    print(f"check-integrity: {len(errors)} problem(s)", file=sys.stderr)
    for e in errors:
        print(f"  - {e}", file=sys.stderr)
    sys.exit(1)

print(f"check-integrity: OK — {len(sites)} packs, {len(signals)} signals, "
      f"{len(operators)} entities, {len(sources)} sources (all manual)")
