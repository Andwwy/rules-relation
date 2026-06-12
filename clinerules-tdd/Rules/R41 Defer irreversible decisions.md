---
tags: [rule, preference]
rule_type: PREFERENCE
hand_tag: "PREFERENCE"
llm_tag: "PREFERENCE"
annotator_agreement: agree
source: "adamglang/sovereign-core .clinerules"
---
# 💡 Defer irreversible decisions

> Defer irreversible decisions: make decisions as late as possible when you have maximum information

**Type:** PREFERENCE  ·  **Hand tag:** PREFERENCE  ·  **LLM tag:** PREFERENCE

## Judgment
Annotator: vague, and 'maximum information' could be forever. Pairs with R44, which carves out when planning IS appropriate.

## Relations
- **support** → [[clinerules-tdd/Rules/R38 Never over-architect or plan too far ahead|R38 Never over-architect or plan too far ahead]]
- **conflict** → [[clinerules-tdd/Rules/R44 Exception: truly irreversible decisions|R44 Exception: truly irreversible decisions]]
