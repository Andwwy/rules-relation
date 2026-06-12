---
tags: [rule, prescription]
rule_type: PRESCRIPTION
hand_tag: "PREFERENCE"
llm_tag: "PRESCRIPTION"
annotator_agreement: disagree
source: "adamglang/sovereign-core .clinerules"
---
# ✅ Centralize behavioral primitives in config

> Primitive values that control UX or system behavior should live in a centralized configuration layer, not scattered as magic numbers.

**Type:** PRESCRIPTION  ·  **Hand tag:** PREFERENCE  ·  **LLM tag:** PRESCRIPTION

## Judgment
Tag split again on 'should'. The accompanying qualifies/does-not-qualify lists (annotator: 'context for the following rules') are what make it usable — without them 'behavioral primitive' would be hopelessly vague. Inherently in tension with R38/R30, which R46 explicitly resolves.

## Relations
- **conflict** → [[clinerules-tdd/Rules/R46 Rule hierarchy - Rule 6 wins|R46 Rule hierarchy - Rule 6 wins]]
