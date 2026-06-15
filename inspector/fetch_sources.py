#!/usr/bin/env python3
"""Fetch each project's raw source rule file at the commit pinned in its CSV.

The CSV's source_url is a GitHub blob URL with a commit SHA, so the fetched file
lines up exactly with line_start/line_end in the CSV. Saved to sources/<project>.txt.

Run this once (and again only if a project's pinned commit changes):
    python3 fetch_sources.py
Then run build_data.py to embed the sources into data/*.json.

Uses curl (the system trust store) to avoid Python SSL-cert issues on some Macs.
"""
import csv
import subprocess
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent
SRC = Path(__file__).resolve().parent / "sources"


def raw_url(blob_url):
    return blob_url.replace("https://github.com/", "https://raw.githubusercontent.com/").replace("/blob/", "/")


def main():
    SRC.mkdir(exist_ok=True)
    for d in sorted(VAULT.iterdir()):
        if not (d.is_dir() and (d / "Rules").is_dir()):
            continue
        csvs = list(d.glob("rules_*.csv"))
        if not csvs:
            print(f"{d.name}: no CSV, skipped")
            continue
        with csvs[0].open(encoding="utf-8") as f:
            row = next(csv.DictReader(f), None)
        url = raw_url((row or {}).get("source_url", ""))
        if not url:
            print(f"{d.name}: no source_url, skipped")
            continue
        dest = SRC / f"{d.name}.txt"
        r = subprocess.run(["curl", "-sS", "-f", url, "-o", str(dest)], capture_output=True, text=True)
        if r.returncode == 0:
            print(f"{d.name}: {len(dest.read_text().splitlines())} lines  <- {url}")
        else:
            print(f"{d.name}: FAILED ({r.stderr.strip()})")


if __name__ == "__main__":
    sys.exit(main())
