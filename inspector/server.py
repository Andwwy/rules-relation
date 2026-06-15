#!/usr/bin/env python3
"""Local server for the rule-relation edge inspector.

Run:  python3 server.py   →  http://localhost:7077

No dependencies. Data is read from ./data/*.json (built by build_data.py).
Annotations (marks, comments, user-added edges) are persisted to
./annotations/<project>.json so they survive restarts and live next to the vault.
"""
import json
import os
import re
import threading
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
ANN = ROOT / "annotations"
ANN.mkdir(exist_ok=True)
PORT = int(os.environ.get("PORT", 7077))
HOST = os.environ.get("HOST", "127.0.0.1")  # set HOST=0.0.0.0 in Docker

_lock = threading.Lock()
SAFE = re.compile(r"^[\w.-]+$")


def load_ann(project):
    f = ANN / f"{project}.json"
    if f.exists():
        ann = json.loads(f.read_text(encoding="utf-8"))
    else:
        ann = {}
    ann.setdefault("edges", {})          # edge_id -> {mark, comment}
    ann.setdefault("added", [])          # user-added relations
    ann.setdefault("nodes", [])          # user-added rules/contexts (from text selection)
    ann.setdefault("cleared", False)     # if true, detected relations are hidden
    return ann


def save_ann(project, data):
    f = ANN / f"{project}.json"
    f.write_text(json.dumps(data, indent=1, ensure_ascii=False), encoding="utf-8")


def now():
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


class Handler(BaseHTTPRequestHandler):
    def _send(self, code, body, ctype="application/json; charset=utf-8"):
        data = body if isinstance(body, bytes) else json.dumps(body, ensure_ascii=False).encode()
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, fmt, *args):  # quieter logs
        pass

    def do_GET(self):
        path = self.path.split("?")[0]
        if path in ("/", "/index.html"):
            self._send(200, (ROOT / "index.html").read_bytes(), "text/html; charset=utf-8")
        elif path == "/api/projects":
            self._send(200, (DATA / "projects.json").read_bytes())
        elif path.startswith("/api/data/"):
            name = path.rsplit("/", 1)[1]
            f = DATA / f"{name}.json"
            if SAFE.match(name) and f.exists():
                self._send(200, f.read_bytes())
            else:
                self._send(404, {"error": "unknown project"})
        elif path.startswith("/api/annotations/"):
            name = path.rsplit("/", 1)[1]
            if SAFE.match(name):
                self._send(200, load_ann(name))
            else:
                self._send(404, {"error": "unknown project"})
        else:
            self._send(404, {"error": "not found"})

    def do_POST(self):
        path = self.path.split("?")[0]
        if not path.startswith("/api/annotations/"):
            return self._send(404, {"error": "not found"})
        name = path.rsplit("/", 1)[1]
        if not SAFE.match(name):
            return self._send(400, {"error": "bad project"})
        length = int(self.headers.get("Content-Length", 0))
        try:
            body = json.loads(self.rfile.read(length))
        except json.JSONDecodeError:
            return self._send(400, {"error": "bad json"})

        with _lock:
            ann = load_ann(name)
            action = body.get("action", "annotate")
            if action == "annotate":
                eid = body["edge_id"]
                cur = ann["edges"].get(eid, {})
                if "mark" in body:
                    cur["mark"] = body["mark"]  # 'agree' | 'unsure' | 'reject' | None
                if "comment" in body:
                    cur["comment"] = body["comment"]
                cur["updated_at"] = now()
                if not cur.get("mark") and not cur.get("comment"):
                    ann["edges"].pop(eid, None)
                else:
                    ann["edges"][eid] = cur
            elif action == "add_edge":
                e = body["edge"]
                eid = f"user--{e['source']}--{e['type'].replace(' ', '_')}--{e['target']}"
                if not any(a["id"] == eid for a in ann["added"]):
                    ann["added"].append({
                        "id": eid,
                        "source": e["source"],
                        "target": e["target"],
                        "type": e["type"],
                        "rationale": e.get("rationale", ""),
                        "user_added": True,
                        "created_at": now(),
                    })
            elif action == "remove_added":
                ann["added"] = [a for a in ann["added"] if a["id"] != body["edge_id"]]
                ann["edges"].pop(body["edge_id"], None)
            elif action == "add_node":
                n = body["node"]
                nid = "U%d" % (max([0] + [int(x["id"][1:]) for x in ann["nodes"] if x["id"][1:].isdigit()]) + 1)
                ann["nodes"].append({
                    "id": nid, "kind": n.get("kind", "rule"),
                    "type": (n.get("type") or "UNKNOWN").upper(),
                    "title": n.get("title", n.get("text", ""))[:90],
                    "text": n.get("text", ""),
                    "line_start": n.get("line_start"), "line_end": n.get("line_end"),
                    "char_start": n.get("char_start"), "char_end": n.get("char_end"),
                    "source_lines": n.get("source_lines", ""),
                    "user_added": True, "created_at": now(),
                })
            elif action == "remove_node":
                ann["nodes"] = [x for x in ann["nodes"] if x["id"] != body["node_id"]]
                ann["added"] = [a for a in ann["added"]
                               if a["source"] != body["node_id"] and a["target"] != body["node_id"]]
            elif action == "clear_relations":
                ann["edges"] = {}
                ann["added"] = []
                ann["cleared"] = True
            elif action == "restore_relations":
                ann["cleared"] = False
            else:
                return self._send(400, {"error": "unknown action"})
            save_ann(name, ann)
        self._send(200, ann)


if __name__ == "__main__":
    print(f"Edge inspector → http://localhost:{PORT}  (binding {HOST}:{PORT})")
    ThreadingHTTPServer((HOST, PORT), Handler).serve_forever()
