---
tags: [rule, prescription]
rule_type: PRESCRIPTION
hand_tag: "PRESCRIPTION"
llm_tag: "PRESCRIPTION"
annotator_agreement: agree
source: "adamglang/sovereign-core .clinerules"
---
# ✅ Use existing config patterns

> Scan for config.py, config.yaml, environment variables, or settings modules already in the repo. Align with what exists.

**Type:** PRESCRIPTION  ·  **Hand tag:** PRESCRIPTION  ·  **LLM tag:** PRESCRIPTION

## Judgment
Config-domain instance of R07/R08 — same search-then-align structure, fully concrete file targets.

## Relations
- **refinement** → [[clinerules-tdd/Rules/R07 Search repo before writing new patterns|R07 Search repo before writing new patterns]]
- **refinement** → [[clinerules-tdd/Rules/R08 Align with established approaches|R08 Align with established approaches]]
- **support** → [[clinerules-tdd/Rules/R45 Centralize behavioral primitives in config|R45 Centralize behavioral primitives in config]]
