---
tags: [rule, prohibition]
rule_type: PROHIBITION
hand_tag: "PREFERENCE"
llm_tag: "PROHIBITION"
annotator_agreement: disagree
source: "adamglang/sovereign-core .clinerules"
---
# 🚫 No new libraries without approval

> Keep dependencies consistent. Avoid adding new libs unless required and approved

**Type:** PROHIBITION  ·  **Hand tag:** PREFERENCE  ·  **LLM tag:** PROHIBITION

## Judgment
'Avoid... unless approved' is a soft-worded prohibition with an approval gate — the LLM's PROHIBITION tag captures the deontic structure better than hand's PREFERENCE. 'Required' is vague; 'approved' is checkable.

## Relations
- **support** → [[clinerules-tdd/Rules/R23 Respect existing toolchain and scripts|R23 Respect existing toolchain and scripts]]
