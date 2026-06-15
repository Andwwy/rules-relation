# Rules Relation

An Obsidian vault studying **rule files for AI coding agents**, plus a local web app for
inspecting the *relations between rules* one edge at a time.

Each project folder (`clinerules-tdd/`, `elastix_gemm/`, `GPTPortal/`) holds the rules and
context items extracted from one real-world agent rule file, with the relations between them
(refinement, exception, support, checkpoint, conflict, duplication) recorded as
`- **<type>** → [[target]]` links inside each note.

## Edge Inspector

`inspector/` is a zero-dependency app for reviewing every relation edge: it shows the two
nodes and the arrow between them, an LLM-generated rationale for *why* the relation holds,
and lets you mark each edge (agree / unsure / reject), comment on it, or add new relations.

### Launch with Docker (recommended)

Keeps the app running in the background and surviving reboots/idle.

```bash
docker compose up -d --build
```

Then open **http://localhost:7077**.

- **Stays up:** `restart: unless-stopped` — the container comes back after a crash, a
  Docker/host restart, or waking from idle. It only stays down if you stop it yourself.
- **Your inputs are stored locally:** marks, comments, and added edges are written to
  `inspector/annotations/` on your machine (bind-mounted into the container), so they
  persist across restarts, rebuilds, and `docker compose down`.
- Stop it with `docker compose stop` (keeps data) or `docker compose down` (removes the
  container; your annotations stay on disk).
- After editing the vault, rebuild so the data refreshes: `docker compose up -d --build`.

### Launch without Docker

Requires only **Python 3** (standard library — no `pip install`).

```bash
cd inspector
python3 build_data.py     # parse the vault → data/*.json (re-run after editing relations)
python3 server.py         # serve the app
```

Then open **http://localhost:7077**.

Set a different port with `PORT=8080 python3 server.py`. The server binds to `127.0.0.1`
by default; set `HOST=0.0.0.0` to expose it on your network (Docker does this automatically).

### What you can do

- **Switch projects** with the tabs in the header — rules, edges and annotations all swap together.
- **Read the source** in the left pane: the original rule file, with the current edge's rule span(s) highlighted in light yellow.
- **Inspect an edge** in the center: source node → relation → target node (exact source text), plus the LLM rationale.
- **Review** each edge: `✓ agree` / `? unsure` / `✗ reject` and a free-text comment (auto-saves).
- **Filter** the relation list (right/left panel) by relation type or review status.
- **Add relations** the LLM missed via **＋ Add relation** (pick source, type, target, write your own rationale).
- Keyboard: `←/→` navigate · `1` agree · `2` unsure · `3` reject.

### How it's wired

| File | Role |
|------|------|
| `inspector/fetch_sources.py` | Downloads each project's raw source rule file at the commit pinned in its CSV into `sources/<project>.txt` (so line numbers match). Run once. |
| `inspector/build_data.py` | Builds `data/<project>.json` — from vault notes, or (for CSV-native projects with a `relations.json`) straight from the CSV. Maps each node to its exact source span and embeds the source file. |
| `inspector/make_obsidian_notes.py` | Generates Obsidian vault notes (Rules/Context `.md` with relation `[[wikilinks]]`) for CSV-native projects, so they appear in Obsidian's graph view. |
| `inspector/data/rationales/*.json` | Per-edge LLM rationales, merged into the data at build time. |
| `inspector/server.py` | Python stdlib HTTP server (port 7077). Serves the UI and persists annotations. |
| `inspector/index.html` | Single-file UI (vanilla JS). |
| `inspector/annotations/<project>.json` | Your saved marks, comments, and user-added edges (one file per project). |

Annotations are plain JSON next to the vault, so they are easy to diff, export, or back up.
Re-run `build_data.py` whenever you edit relations in the vault to refresh the app's data.
