---
tags: [rule, prohibition]
rule_type: PROHIBITION
hand_tag: "PROHIBITION"
llm_tag: "PROHIBITION"
annotator_agreement: agree
source: "adamglang/sovereign-core .clinerules"
---
# 🚫 No parallel patterns or dual sources of truth

> Do not introduce parallel patterns, dual sources of truth, or divergent frameworks without explicit instruction.

**Type:** PROHIBITION  ·  **Hand tag:** PROHIBITION  ·  **LLM tag:** PROHIBITION

## Judgment
Clear prohibition with an explicit-instruction escape hatch. 'Parallel pattern' is vague at the margin (annotator agrees), but R50/R52 make it concrete for the config domain. R10 provides the legal route around it.

## Relations
- **support** → [[clinerules-tdd/Rules/R08 Align with established approaches|R08 Align with established approaches]]
