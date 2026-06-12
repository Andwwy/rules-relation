---
tags: [rule, permission]
rule_type: PERMISSION
hand_tag: "PERMISSION"
llm_tag: "—"
annotator_agreement: hand-only
source: "adamglang/sovereign-core .clinerules"
---
# 🔓 Provider-level defaults exception

> Internal implementation details (retry counts, backoff delays) not exposed in config.yaml can have provider-level defaults.

**Type:** PERMISSION  ·  **Hand tag:** PERMISSION  ·  **LLM tag:** —

## Judgment
Fourth instance of the gated-exception pattern (after R05, R29, R37). Boundary is clear: exposed-in-config.yaml vs internal.

## Relations
- **exception** → [[clinerules-tdd/Rules/R52 Exactly ONE default definition|R52 Exactly ONE default definition]]
