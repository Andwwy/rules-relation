---
tags: [rule, prescription]
rule_type: PRESCRIPTION
hand_tag: "PREFERENCE"
llm_tag: "PRESCRIPTION"
annotator_agreement: disagree
source: "adamglang/sovereign-core .clinerules"
---
# ✅ Centralize incrementally

> Move a primitive to config only when you're actively working with it or it clearly affects user-facing behavior.

**Type:** PRESCRIPTION  ·  **Hand tag:** PREFERENCE  ·  **LLM tag:** PRESCRIPTION

## Judgment
The 'only when' gate gives this a clear conditional structure. It is R45 throttled by R38's incrementalism.

## Relations
- **support** → [[clinerules-tdd/Rules/R45 Centralize behavioral primitives in config|R45 Centralize behavioral primitives in config]]
- **support** → [[clinerules-tdd/Rules/R46 Rule hierarchy - Rule 6 wins|R46 Rule hierarchy - Rule 6 wins]]
