---
tags: [rule, permission]
rule_type: PERMISSION
hand_tag: "PERMISSION"
llm_tag: "PERMISSION"
annotator_agreement: agree
source: "adamglang/sovereign-core .clinerules"
---
# 🔓 Exception for generated and third-party code

> Only exception: generated code or third-party dependencies that cannot be modified. Even then, isolate with targeted config changes, not inline disables.

**Type:** PERMISSION  ·  **Hand tag:** PERMISSION  ·  **LLM tag:** PERMISSION

## Judgment
Well-bounded permission with a nested prescription (config-only isolation). Mirrors the R05 pattern: exception narrowly carved out of a hard prohibition.

## Relations
- **exception** → [[clinerules-tdd/Rules/R26 NEVER disable linting, compilation, or type errors|R26 NEVER disable linting, compilation, or type errors]]
- **exception** → [[clinerules-tdd/Rules/R27 No suppression pragmas|R27 No suppression pragmas]]
