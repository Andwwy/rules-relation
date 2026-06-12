---
tags: [rule, prohibition]
rule_type: PROHIBITION
hand_tag: "PROHIBITION"
llm_tag: "PROHIBITION"
annotator_agreement: agree
source: "adamglang/sovereign-core .clinerules"
---
# 🚫 No duplicate or parallel config sources

> Don't create duplicates: if a value is already configurable somewhere, use that mechanism. Don't create parallel config sources.

**Type:** PROHIBITION  ·  **Hand tag:** PROHIBITION  ·  **LLM tag:** PROHIBITION

## Judgment
Config-domain instance of R09's dual-source-of-truth ban. Clear and checkable.

## Relations
- **refinement** → [[clinerules-tdd/Rules/R09 No parallel patterns or dual sources of truth|R09 No parallel patterns or dual sources of truth]]
