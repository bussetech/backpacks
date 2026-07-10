#!/usr/bin/env python3
"""Referential integrity for the backpacks dataset.

Schema validation proves each file is well-formed. This proves the files agree
with each other: every citation resolves, every id is stable, and no record
claims a signal or a maker that does not exist.

The rule this enforces above all: a published value traces to a signal, and a
signal traces to a page on a registered source's host. A dataset whose
provenance chain has a hole in it is worse than one with fewer entries.
"""
import pathlib
import sys
from urllib.parse import urlsplit

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
errors: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def load(path: pathlib.Path):
    return yaml.safe_load(path.read_text())


def host(url: str) -> str:
    return urlsplit(url).hostname or ""


def registrable(h: str) -> str:
    """Strip a leading www. so www.goruck.com and goruck.com are one host."""
    return h[4:] if h.startswith("www.") else h


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

source_hosts = {registrable(host(s["url"])) for s in sources.values()}

# --- signals -----------------------------------------------------------------
for sid, sig in signals.items():
    site_id = sig.get("site_id")
    if site_id and site_id not in sites:
        err(f"{sid}: site_id {site_id!r} is not a record in data/sites/")
    h = registrable(host(sig["source_url"]))
    if h not in source_hosts:
        err(f"{sid}: source_url host {h!r} belongs to no registered source. "
            f"Every claim must come from a source in data/sources.yml.")

# --- records -----------------------------------------------------------------
for rid, rec in sites.items():
    if rec["maker"] not in operators:
        err(f"{rid}: maker {rec['maker']!r} is not in data/operators.yml")
    for sig_id in rec.get("signals", []):
        if sig_id not in signals:
            err(f"{rid}: cites signal {sig_id!r}, which does not exist")
        elif signals[sig_id].get("site_id") != rid:
            err(f"{rid}: cites signal {sig_id!r}, whose site_id is {signals[sig_id].get('site_id')!r}")
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
# ADR-0046: this registry is entirely manual. If that ever changes it must
# change deliberately — an `active` source appearing by accident means a
# fetcher is about to hit someone's server.
for sid, s in sources.items():
    if s["status"] == "active":
        err(f"{sid}: status is 'active', but ADR-0046 records this registry as entirely manual. "
            f"Flipping a source to active is a decision, not an edit: amend the ADR in the same PR.")

# --- page stubs --------------------------------------------------------------
stub_dir = ROOT / "packs"
stubs = {p.stem for p in stub_dir.glob("*.md")} if stub_dir.is_dir() else set()
if set(sites) - stubs:
    err(f"page stubs missing for: {', '.join(sorted(set(sites) - stubs))} — run scripts/gen-pages.sh")
if stubs - set(sites):
    err(f"orphan page stubs: {', '.join(sorted(stubs - set(sites)))} — run scripts/gen-pages.sh")

# --- the derived index -------------------------------------------------------
# data/packs_index.yml is generated. If it drifts from data/sites/, the site
# renders numbers no record backs — the exact failure this dataset exists to
# prevent.
index_path = ROOT / "data" / "packs_index.yml"
if not index_path.is_file():
    err("data/packs_index.yml is missing — run scripts/gen-pages.sh")
else:
    index = load(index_path) or []
    if {row["id"] for row in index} != set(sites):
        err("data/packs_index.yml is out of sync with data/sites/ — run scripts/gen-pages.sh")
    else:
        for row in index:
            rec = sites[row["id"]]
            if row["name"] != rec["name"] or row["status"] != rec["status"]:
                err(f"{row['id']}: packs_index.yml disagrees with the record — run scripts/gen-pages.sh")
            if row.get("capacity_l") != rec.get("specs", {}).get("capacity_l"):
                err(f"{row['id']}: packs_index.yml capacity disagrees with the record — run scripts/gen-pages.sh")

# --- conflicts are real ------------------------------------------------------
# A conflict is two signals sharing (site_id, attribute) and disagreeing on
# value. Where one exists, the record must acknowledge it — a silently resolved
# conflict is the one thing this dataset promises never to do.
by_key: dict[tuple[str, str], set] = {}
for sig in signals.values():
    if sig.get("site_id"):
        by_key.setdefault((sig["site_id"], sig["attribute"]), set()).add(str(sig["value"]))
for (site_id, attribute), values in sorted(by_key.items()):
    if len(values) > 1:
        rec = sites.get(site_id, {})
        note_field = f"{attribute.replace('_l', '').replace('weight_g', 'weight')}_note"
        specs = rec.get("specs", {})
        acknowledged = any(k.endswith("_note") for k in specs) or rec.get("notes")
        if not acknowledged:
            err(f"{site_id}: signals disagree on {attribute} ({', '.join(sorted(values))}) but the record "
                f"acknowledges no conflict. Add a *_note or notes: — never pick silently.")

if errors:
    print(f"check-integrity: {len(errors)} problem(s)", file=sys.stderr)
    for e in errors:
        print(f"  - {e}", file=sys.stderr)
    sys.exit(1)

conflicts = sum(1 for v in by_key.values() if len(v) > 1)
print(f"check-integrity: OK — {len(sites)} packs, {len(signals)} signals, {len(operators)} entities, "
      f"{len(sources)} sources (all manual), {conflicts} unresolved conflict(s) acknowledged")
