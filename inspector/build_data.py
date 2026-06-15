#!/usr/bin/env python3
"""Parse the rules-relation Obsidian vault into JSON for the edge inspector.

For each project folder (one with Rules/ inside), emits data/<project>.json:
  { "project": ..., "nodes": {id: {...}}, "edges": [{...}] }

If data/rationales/<project>.json exists (edge_id -> rationale string),
rationales are merged into the edges.
"""
import csv
import difflib
import json
import re
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent
OUT = Path(__file__).resolve().parent / "data"
SRC = Path(__file__).resolve().parent / "sources"  # raw source files (fetch_sources.py)

REL_RE = re.compile(r"^- \*\*(?P<type>[^*]+)\*\*\s*(?:→|->)\s*\[\[(?P<target>[^\]|]+)(?:\|(?P<label>[^\]]+))?\]\]")
TITLE_RE = re.compile(r"^# (?P<emoji>\S+)?\s*(?P<title>.+)$")

# A node is mapped to a CSV row (the source span the labeler/LLM selected as the
# rule) only when the best text similarity clears this bar. Below it we keep the
# vault's paraphrase and flag verbatim=False — almost always synthesized context
# nodes that summarize several source spans and have no single literal text.
MATCH_THRESHOLD = 0.5
DEONTIC_TAGS = {"PROHIBITION", "PRESCRIPTION", "PREFERENCE", "PERMISSION"}


def _norm(s):
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", (s or "").lower())).strip()


def _similarity(a, b):
    """Blend sequence ratio with token-set overlap so reordered paraphrases score well."""
    na, nb = _norm(a), _norm(b)
    seq = difflib.SequenceMatcher(None, na, nb).ratio()
    ta, tb = set(na.split()), set(nb.split())
    jac = len(ta & tb) / max(1, len(ta | tb))
    return max(seq, jac)


def load_csv_spans(proj_dir):
    """Group every CSV row by its (line_start, line_end) source span."""
    csvs = list(proj_dir.glob("rules_*.csv"))
    if not csvs:
        return {}
    spans = {}
    with csvs[0].open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            try:
                key = (int(r["line_start"]), int(r["line_end"]))
            except (ValueError, KeyError):
                continue
            spans.setdefault(key, []).append(r)
    return spans


def match_node_to_source(node, spans):
    """Find the source span whose selected text best matches the node's paraphrase.

    Returns (exact_text, (line_start, line_end), score). Prefers the hand-selected
    row's text (a literal source span) over the LLM's reworded extraction. A soft
    penalty discourages matching a rule to a row of a different deontic tag.
    """
    paraphrase = node.get("text", "")
    rtype = (node.get("type") or "").upper()
    best, best_score, best_key = None, -1.0, None
    for key, rows in spans.items():
        for r in rows:
            sc = _similarity(paraphrase, r.get("rule_text", ""))
            tag = (r.get("tag") or "").upper()
            if rtype in DEONTIC_TAGS and tag and tag != rtype:
                sc *= 0.85
            if sc > best_score:
                best_score, best, best_key = sc, (key, rows, r), key
    if best is None:
        return None, None, 0.0
    _, rows, row = best
    hand = [x for x in rows if x.get("extracted_by") == "hand"]
    exact = (hand[0] if hand else row).get("rule_text", "").strip()
    return exact, best_key, best_score


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

    # Replace each node's display text with the exact span selected as the rule
    # in the source file (from the CSV). The vault note's quote is kept as
    # "paraphrase"; "source_lines" and "verbatim" let the UI show provenance.
    spans = load_csv_spans(proj_dir)
    matched = 0
    for node in nodes.values():
        node["paraphrase"] = node["text"]
        if not spans:
            node["verbatim"] = False
            node["source_lines"] = ""
            node["line_start"] = node["line_end"] = None
            continue
        exact, key, score = match_node_to_source(node, spans)
        if exact and score >= MATCH_THRESHOLD:
            node["text"] = exact
            node["verbatim"] = True
            node["source_lines"] = f"{key[0]}" if key[0] == key[1] else f"{key[0]}–{key[1]}"
            node["line_start"], node["line_end"] = key[0], key[1]
            matched += 1
        else:
            node["verbatim"] = False
            node["source_lines"] = ""
            node["line_start"] = node["line_end"] = None
    build_project.last_match = (matched, len(nodes))

    # merge LLM rationales if present
    rfile = OUT / "rationales" / f"{project}.json"
    if rfile.exists():
        rationales = json.loads(rfile.read_text())
        for e in edges:
            if e["id"] in rationales:
                e["rationale"] = rationales[e["id"]]

    # drop edges pointing at unknown nodes (safety)
    edges = [e for e in edges if e["source"] in nodes and e["target"] in nodes]

    # Embed the raw source file (fetched at the CSV's pinned commit, so its line
    # numbers match line_start/line_end) so the UI can show it and highlight the
    # current rule's span.
    src_file = SRC / f"{project}.txt"
    source_text = src_file.read_text(encoding="utf-8") if src_file.exists() else ""
    src_meta = parse_frontmatter((proj_dir / "_SOURCE.md").read_text(encoding="utf-8"))[0] \
        if (proj_dir / "_SOURCE.md").exists() else {}
    src_rows = load_csv_first_row(proj_dir)

    return {
        "project": project,
        "nodes": nodes,
        "edges": edges,
        "source_text": source_text,
        "source_name": src_meta.get("rule_file", f"{project} source"),
        "source_url": src_rows.get("source_url", ""),
    }


def load_csv_first_row(proj_dir):
    csvs = list(proj_dir.glob("rules_*.csv"))
    if not csvs:
        return {}
    with csvs[0].open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            return r
    return {}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "rationales").mkdir(exist_ok=True)
    projects = []
    for d in sorted(VAULT.iterdir()):
        if d.is_dir() and (d / "Rules").is_dir():
            data = build_project(d)
            (OUT / f"{d.name}.json").write_text(json.dumps(data, indent=1, ensure_ascii=False))
            n_rat = sum(1 for e in data["edges"] if e["rationale"])
            mv = sum(1 for n in data["nodes"].values() if n.get("verbatim"))
            print(f"{d.name}: {len(data['nodes'])} nodes, {len(data['edges'])} edges "
                  f"({n_rat} with rationale, {mv}/{len(data['nodes'])} verbatim from source)")
            projects.append(d.name)
    (OUT / "projects.json").write_text(json.dumps(projects))


if __name__ == "__main__":
    sys.exit(main())
