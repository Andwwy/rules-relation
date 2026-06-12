---
tags: [rule, permission]
rule_type: PERMISSION
hand_tag: "PERMISSION"
llm_tag: "PERMISSION"
annotator_agreement: agree
source: "adamglang/sovereign-core .clinerules"
---
# 🔓 Fallbacks only if requested or opt-in

> Fallbacks (CPU, reduced mode, mocks) are allowed ONLY if explicitly requested by the user, OR already defined as an opt-in mode.

**Type:** PERMISSION  ·  **Hand tag:** PERMISSION  ·  **LLM tag:** PERMISSION

## Judgment
Textbook permission-as-exception: it carves a precise, gated escape hatch out of R01/R02. The two conditions are objectively checkable. Annotator correctly noted it is 'a permission inside a prohibition'.

## Relations
- **exception** → [[clinerules-tdd/Rules/R01 No silent downgrades|R01 No silent downgrades]]
- **exception** → [[clinerules-tdd/Rules/R02 Never disable core features to fix errors|R02 Never disable core features to fix errors]]
