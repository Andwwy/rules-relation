---
tags: [rule, prescription]
rule_type: PRESCRIPTION
hand_tag: "PRESCRIPTION"
llm_tag: "PRESCRIPTION"
annotator_agreement: agree
source: "adamglang/sovereign-core .clinerules"
---
# ✅ Confirm rules and list patterns at task start

> At task start: confirm you will follow these rules. Explicitly list detected patterns relevant to the task.

**Type:** PRESCRIPTION  ·  **Hand tag:** PRESCRIPTION  ·  **LLM tag:** PRESCRIPTION

## Judgment
Pure compliance ritual. Annotator's 'What rules??' flags a real referential ambiguity — 'these rules' assumes the whole file is in context. The pattern-listing half operationalizes R11.

## Relations
- **checkpoint** → [[clinerules-tdd/Rules/R11 Scan codebase to infer patterns|R11 Scan codebase to infer patterns]]
