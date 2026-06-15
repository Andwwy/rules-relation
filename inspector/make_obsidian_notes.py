#!/usr/bin/env python3
"""Generate Obsidian vault notes (Rules/*.md, Context/*.md) for CSV-native
projects, so they show up in Obsidian's graph view like GPTPortal/elastix_gemm.

Reads inspector/data/<project>.json (nodes + edges) and writes one note per
node, with outgoing relations as [[wikilinks]] (incoming come from backlinks).
The inspector itself still reads the CSV (these projects keep relations.json,
which build_data treats as the CSV-native marker) — the notes are only for the
Obsidian graph, generated from the same data so the two stay consistent.

Usage: python3 make_obsidian_notes.py [project ...]
Default: every project that has a relations.json (the CSV-native ones).
"""
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VAULT = ROOT.parent
DATA = ROOT / "data"

EMOJI = {"PROHIBITION": "🚫", "PRESCRIPTION": "✅", "PREFERENCE": "💡",
         "PERMISSION": "🔓", "CONTEXT": "🗒", "UNKNOWN": "•"}


def fname(nid, title):
    t = re.sub(r'[\\/:*?"<>|#\[\]^]', "-", title or "").strip()
    t = re.sub(r"\s+", " ", t)
    if len(t) > 80:
        t = t[:80]
    t = t.rstrip(" .")                          # avoid trailing-dot "..md"
    return f"{nid} {t}".strip()


def link(project, node, names):
    folder = "Context" if node["kind"] == "context" else "Rules"
    nm = names[node["id"]]
    return f"[[{project}/{folder}/{nm}|{nm}]]"


def write_project(project):
    data = json.loads((DATA / f"{project}.json").read_text(encoding="utf-8"))
    nodes, edges = data["nodes"], data["edges"]
    proj_dir = VAULT / project
    source_name = data.get("source_name", f"{project} source")

    names = {nid: fname(nid, n["title"]) for nid, n in nodes.items()}
    out = {}                                   # node id -> list of outgoing edges
    for e in edges:
        out.setdefault(e["source"], []).append(e)

    # fresh regeneration
    for sub in ("Rules", "Context"):
        d = proj_dir / sub
        if d.exists():
            shutil.rmtree(d)
        d.mkdir(parents=True)

    for nid, n in nodes.items():
        is_ctx = n["kind"] == "context"
        ntype = n["type"]
        rels = out.get(nid, [])
        rel_lines = "\n".join(
            f"- **{e['type']}** → {link(project, nodes[e['target']], names)}"
            for e in rels if e["target"] in nodes
        ) or "*(target only — incoming relations via backlinks)*"

        if is_ctx:
            fm = (f"---\ntags: [context]\nnode_type: CONTEXT\n"
                  f"grounds_count: {len(rels)}\nsource: \"{source_name}\"\n---\n")
            body = (f"{fm}# 🗒 {n['title']}\n\n> {n['text']}\n\n"
                    f"**Node type:** CONTEXT — no deontic force; participates only in support relations.\n\n"
                    f"## Role\n{n.get('judgment') or '—'}\n\n"
                    f"## Grounds ({len(rels)} rules)\n{rel_lines}\n")
        else:
            tag = ntype.lower()
            tagline = f"[rule, {tag}]" if ntype != "UNKNOWN" else "[rule]"
            emoji = EMOJI.get(ntype, "•")
            fm = (f"---\ntags: {tagline}\nrule_type: {ntype}\n"
                  f"source: \"{source_name}\"\nsource_lines: \"{n.get('source_lines','')}\"\n---\n")
            body = (f"{fm}# {emoji} {n['title']}\n\n> {n['text']}\n\n"
                    f"**Type:** {ntype}  ·  **Source line:** {n.get('source_lines','—')}\n\n"
                    f"## Judgment\n{n.get('judgment') or '—'}\n\n"
                    f"## Relations\n{rel_lines}\n")

        folder = "Context" if is_ctx else "Rules"
        (proj_dir / folder / f"{names[nid]}.md").write_text(body, encoding="utf-8")

    nR = sum(1 for n in nodes.values() if n["kind"] != "context")
    nC = len(nodes) - nR
    print(f"{project}: wrote {nR} Rules + {nC} Context notes ({len(edges)} relations as links)")


def main():
    targets = sys.argv[1:]
    if not targets:
        targets = [d.name for d in sorted(VAULT.iterdir())
                   if d.is_dir() and (d / "relations.json").exists()]
    for p in targets:
        write_project(p)


if __name__ == "__main__":
    sys.exit(main())
