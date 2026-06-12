---
tags: [rule, prohibition]
rule_type: PROHIBITION
hand_tag: "PROHIBITION"
llm_tag: "PROHIBITION"
annotator_agreement: agree
source: "adamglang/sovereign-core .clinerules"
---
# 🚫 Defaults stay on best-supported path

> Defaults must remain on the best-supported path. Never silently degrade behavior to "make it work."

**Type:** PROHIBITION  ·  **Hand tag:** PROHIBITION  ·  **LLM tag:** PROHIBITION

## Judgment
Restates R01 with a defaults focus — partially redundant. 'Best-supported path' is undefined; hand annotation split this into a prescription + prohibition while the LLM merged them, showing segmentation disagreement, not semantic disagreement.

## Relations
- **refinement** → [[clinerules-tdd/Rules/R01 No silent downgrades|R01 No silent downgrades]]
