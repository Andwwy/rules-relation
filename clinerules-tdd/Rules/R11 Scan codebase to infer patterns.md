---
tags: [rule, prescription]
rule_type: PRESCRIPTION
hand_tag: "PRESCRIPTION"
llm_tag: "PRESCRIPTION"
annotator_agreement: agree
source: "adamglang/sovereign-core .clinerules"
---
# ✅ Scan codebase to infer patterns

> Scan the codebase (components, hooks, services/api, utils, lib) and package.json to infer patterns.

**Type:** PRESCRIPTION  ·  **Hand tag:** PRESCRIPTION  ·  **LLM tag:** PRESCRIPTION

## Judgment
Concrete locations make this actionable. It is the evidence-gathering step that R07/R08 silently depend on.

## Relations
- **support** → [[clinerules-tdd/Rules/R07 Search repo before writing new patterns|R07 Search repo before writing new patterns]]
- **support** → [[clinerules-tdd/Rules/R08 Align with established approaches|R08 Align with established approaches]]
