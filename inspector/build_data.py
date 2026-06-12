#!/usr/bin/env python3
"""Parse the rules-relation Obsidian vault into JSON for the edge inspector.

For each project folder (one with Rules/ inside), emits data/<project>.json:
  { "project": ..., "nodes": {id: {...}}, "edges": [{...}] }

If data/rationales/<project>.json exists (edge_id -> rationale string),
rationales are merged into the edges.
"""
import json
import re
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent
OUT = Path(__file__).resolve().parent / "data"

REL_RE = re.compile(r"^- \*\*(?P<type>[^*]+)\*\*\s*(?:→|->)\s*\[\[(?P<target>[^\]|]+)(?:\|(?P<label>[^\]]+))?\]\]")
TITLE_RE = re.compile(r"^# (?P<emoji>\S+)?\s*(?P<title>.+)$")


def parse_frontmatter(text):
    fm = {}
    if not text.startswith("---"):
        return fm, text
    end = text.find("\n---", 3)
    if end == -1:
        return fm, text
    for line in text[3:end].strip().splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"')
    return fm, text[end + 4:]


def node_id_from_path(path_str):
    """'clinerules-tdd/Rules/R01 No silent downgrades' -> 'R01'"""
    name = path_str.split("/")[-1]
    m = re.match(r"^([RC]\d+)\b", name)
    return m.group(1) if m else name


def section(body, header):
    m = re.search(rf"^## {re.escape(header)}.*?$\n(.*?)(?=^## |\Z)", body, re.M | re.S)
    return m.group(1).strip() if m else ""


def parse_node(md_path, project):
    text = md_path.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)
    nid = node_id_from_path(md_path.stem)
    title, emoji = md_path.stem, ""
    quote_lines = []
    for line in body.splitlines():
        tm = TITLE_RE.match(line)
        if tm and not title_set(title, md_path.stem):
            pass
        if line.startswith("# "):
            m = TITLE_RE.match(line)
            raw = m.group("title").strip()
            parts = raw.split(" ", 1)
            if parts and not parts[0].isascii():
                emoji, title = parts[0], parts[1] if len(parts) > 1 else raw
            else:
                emoji, title = "", raw
        elif line.startswith("> "):
            quote_lines.append(line[2:].strip())

    node_type = fm.get("rule_type") or fm.get("node_type") or "UNKNOWN"
    node = {
        "id": nid,
        "file": str(md_path.relative_to(VAULT)),
        "kind": "context" if nid.startswith("C") else "rule",
        "title": title,
        "emoji": emoji,
        "type": node_type,
        "context_type": fm.get("context_type", ""),
        "hand_tag": fm.get("hand_tag", ""),
        "llm_tag": fm.get("llm_tag", ""),
        "agreement": fm.get("annotator_agreement", ""),
        "source": fm.get("source", ""),
        "text": " ".join(quote_lines),
        "judgment": section(body, "Judgment") or section(body, "Role"),
    }

    edges = []
    for line in body.splitlines():
        m = REL_RE.match(line.strip())
        if m:
            tgt = node_id_from_path(m.group("target"))
            rtype = m.group("type").strip()
            edges.append({
                "id": f"{nid}--{rtype.replace(' ', '_')}--{tgt}",
                "source": nid,
                "target": tgt,
                "type": rtype,
                "rationale": "",
            })
    return node, edges


def title_set(a, b):
    return a != b


def build_project(proj_dir):
    project = proj_dir.name
    nodes, edges = {}, []
    for sub in ("Rules", "Context"):
        d = proj_dir / sub
        if not d.is_dir():
            continue
        for md in sorted(d.glob("*.md")):
            node, e = parse_node(md, project)
            nodes[node["id"]] = node
            edges.extend(e)

    # merge LLM rationales if present
    rfile = OUT / "rationales" / f"{project}.json"
    if rfile.exists():
        rationales = json.loads(rfile.read_text())
        for e in edges:
            if e["id"] in rationales:
                e["rationale"] = rationales[e["id"]]

    # drop edges pointing at unknown nodes (safety)
    edges = [e for e in edges if e["source"] in nodes and e["target"] in nodes]
    return {"project": project, "nodes": nodes, "edges": edges}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "rationales").mkdir(exist_ok=True)
    projects = []
    for d in sorted(VAULT.iterdir()):
        if d.is_dir() and (d / "Rules").is_dir():
            data = build_project(d)
            (OUT / f"{d.name}.json").write_text(json.dumps(data, indent=1, ensure_ascii=False))
            n_rat = sum(1 for e in data["edges"] if e["rationale"])
            print(f"{d.name}: {len(data['nodes'])} nodes, {len(data['edges'])} edges ({n_rat} with rationale)")
            projects.append(d.name)
    (OUT / "projects.json").write_text(json.dumps(projects))


if __name__ == "__main__":
    sys.exit(main())
