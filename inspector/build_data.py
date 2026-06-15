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


def locate_in_source(text, lines, hint=None):
    """Find the contiguous line range in the source file that best matches `text`.

    The CSV's LLM-extracted line_start/line_end are unreliable (off-by-one drift),
    so for confidently-matched nodes we re-derive the true line range from the
    actual source. `hint` (the CSV's 1-indexed range) is used only as a soft
    tie-breaker. Returns (start, end) 1-indexed, or None if nothing matches well.
    """
    tt = set(_norm(text).split())
    if not tt:
        return None
    n = len(lines)
    best, best_score = None, 0.0
    for i in range(n):
        joined = ""
        for w in range(min(15, n - i)):
            joined = (joined + " " + _norm(lines[i + w])).strip()
            jt = set(joined.split())
            inter = len(tt & jt)
            cov = inter / len(tt)                    # how much of the rule is covered
            jac = inter / len(tt | jt) if jt else 0  # penalize extra/noise lines
            score = 0.5 * cov + 0.5 * jac
            if hint:
                dist = min(abs((i + 1) - hint[0]), abs((i + 1) - hint[1]))
                score -= 0.008 * min(dist, 25)
            if score > best_score:
                best_score, best = score, (i + 1, i + w + 1)
    return best if best_score >= 0.5 else None


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

    # Source file (raw, fetched at the CSV's pinned commit). Read it up front so
    # we can re-derive correct line numbers from it (see below).
    src_file = SRC / f"{project}.txt"
    source_text = src_file.read_text(encoding="utf-8") if src_file.exists() else ""
    source_lines = source_text.split("\n") if source_text else []

    # Replace each node's display text with the exact span selected as the rule
    # in the source file (from the CSV). The vault note's quote is kept as
    # "paraphrase"; "source_lines" and "verbatim" let the UI show provenance.
    spans = load_csv_spans(proj_dir)
    matched = relocated = 0

    def set_lines(node, start, end):
        node["line_start"], node["line_end"] = start, end
        node["source_lines"] = f"{start}" if start == end else f"{start}–{end}"

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
            set_lines(node, key[0], key[1])
            # The CSV's (often LLM-estimated) line numbers drift; re-locate the
            # exact text in the real source so the line ref + highlight are right.
            if source_lines:
                loc = locate_in_source(exact, source_lines, hint=key)
                if loc and loc != (key[0], key[1]):
                    set_lines(node, loc[0], loc[1])
                    relocated += 1
            matched += 1
        else:
            node["verbatim"] = False
            node["source_lines"] = ""
            node["line_start"] = node["line_end"] = None
    build_project.last_match = (matched, len(nodes), relocated)

    # merge LLM rationales if present
    rfile = OUT / "rationales" / f"{project}.json"
    if rfile.exists():
        rationales = json.loads(rfile.read_text())
        for e in edges:
            if e["id"] in rationales:
                e["rationale"] = rationales[e["id"]]

    # drop edges pointing at unknown nodes (safety)
    edges = [e for e in edges if e["source"] in nodes and e["target"] in nodes]

    # Source descriptor (rule_file name) and pinned URL for the source header.
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


def clean_title(text):
    """A short human-readable label from a verbatim rule span."""
    t = text.split("\n")[0].strip()
    t = re.sub(r"^\s*\d+\.\s+", "", t)          # "1. "
    t = re.sub(r"^\s*[-*•]\s+", "", t)          # bullet
    t = t.replace("**", "").replace("`", "").replace("__", "")
    t = re.sub(r"\s+", " ", t).strip(" :-")
    if len(t) > 90:
        t = t[:88].rsplit(" ", 1)[0] + "…"
    return t


def _is_hand(row):
    return row.get("extracted_by") in ("hand", row.get("annotator"))


def build_project_from_csv(proj_dir):
    """Build a project straight from its rules_*.csv (no vault notes).

    Nodes = the human annotator's spans (authoritative) plus any LLM span that
    doesn't overlap a hand span. Relations come from <proj>/relations.json
    (produced by the LLM relation-detection pass), if present.
    """
    project = proj_dir.name
    rows = list(csv.DictReader((list(proj_dir.glob("rules_*.csv"))[0]).open(encoding="utf-8")))

    def span(r):
        return (int(r["line_start"]), int(r["line_end"]))

    hand = {}
    for r in rows:
        if _is_hand(r):
            hand.setdefault(span(r), r)
    hand_keys = list(hand)

    def overlaps(s):
        return any(not (s[1] < h[0] or s[0] > h[1]) for h in hand_keys)

    canonical = dict(hand)
    for r in rows:                       # add LLM-only spans (e.g. contexts the human didn't tag)
        if not _is_hand(r) and span(r) not in canonical and not overlaps(span(r)):
            canonical[span(r)] = r
    # an LLM row per span, for its rationale (stored as judgment; unused in UI)
    llm_by_span = {}
    for r in rows:
        if not _is_hand(r):
            llm_by_span.setdefault(span(r), r)

    source_text = (SRC / f"{project}.txt").read_text(encoding="utf-8") if (SRC / f"{project}.txt").exists() else ""
    source_lines = source_text.split("\n") if source_text else []

    items = sorted(canonical.items())     # by (line_start, line_end)
    rc = cc = 0
    nodes, by_key = {}, {}
    for key, row in items:
        is_ctx = (row.get("kind") == "context")
        if is_ctx:
            cc += 1; nid = f"C{cc:02d}"; ntype = "CONTEXT"
        else:
            rc += 1; nid = f"R{rc:02d}"; ntype = (row.get("tag") or "UNKNOWN").upper()
        text = row["rule_text"].strip()
        node = {
            "id": nid, "kind": "context" if is_ctx else "rule",
            "title": clean_title(text), "emoji": "", "type": ntype,
            "text": text, "paraphrase": text,
            "judgment": (llm_by_span.get(key, {}) or {}).get("llm_rationale", ""),
            "source": row.get("source_url", ""),
            "verbatim": True, "source_lines": "", "line_start": None, "line_end": None,
        }
        loc = locate_in_source(text, source_lines, hint=key) if source_lines else None
        s, e = loc if loc else key
        node["line_start"], node["line_end"] = s, e
        node["source_lines"] = f"{s}" if s == e else f"{s}–{e}"
        nodes[nid] = node
        by_key[key] = nid

    # relations (from the LLM detection pass)
    edges = []
    rel_file = proj_dir / "relations.json"
    if rel_file.exists():
        for r in json.loads(rel_file.read_text(encoding="utf-8")):
            s, t, ty = r.get("source"), r.get("target"), r.get("type")
            if s in nodes and t in nodes and s != t:
                edges.append({
                    "id": f"{s}--{ty.replace(' ', '_')}--{t}",
                    "source": s, "target": t, "type": ty,
                    "rationale": r.get("rationale", ""),
                })

    src_meta = parse_frontmatter((proj_dir / "_SOURCE.md").read_text(encoding="utf-8"))[0] \
        if (proj_dir / "_SOURCE.md").exists() else {}
    return {
        "project": project, "nodes": nodes, "edges": edges,
        "source_text": source_text,
        "source_name": src_meta.get("rule_file", f"{project} source"),
        "source_url": (rows[0].get("source_url", "") if rows else ""),
    }


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "rationales").mkdir(exist_ok=True)
    projects = []
    for d in sorted(VAULT.iterdir()):
        if not d.is_dir():
            continue
        if (d / "Rules").is_dir():                       # vault-note project
            data = build_project(d)
        elif list(d.glob("rules_*.csv")):                # CSV-native project
            data = build_project_from_csv(d)
        else:
            continue
        (OUT / f"{d.name}.json").write_text(json.dumps(data, indent=1, ensure_ascii=False))
        mv = sum(1 for n in data["nodes"].values() if n.get("verbatim"))
        print(f"{d.name}: {len(data['nodes'])} nodes, {len(data['edges'])} edges ({mv} verbatim)")
        projects.append(d.name)
    (OUT / "projects.json").write_text(json.dumps(projects))


if __name__ == "__main__":
    sys.exit(main())
