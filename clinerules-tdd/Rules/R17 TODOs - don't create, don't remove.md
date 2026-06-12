---
tags: [rule, prohibition]
rule_type: PROHIBITION
hand_tag: "PREFERENCE"
llm_tag: "PROHIBITION"
annotator_agreement: disagree
source: "adamglang/sovereign-core .clinerules"
---
# 🚫 TODOs - don't create, don't remove

> TODO statements should not be created but also should not be removed without explicit instruction.

**Type:** PROHIBITION  ·  **Hand tag:** PREFERENCE  ·  **LLM tag:** PROHIBITION

## Judgment
Buried inside the whitelist bullet list but is actually a bidirectional prohibition (LLM got the tag right). Unusual and well-defined: both actions are objectively detectable in a diff.

## Relations
- **refinement** → [[clinerules-tdd/Rules/R14 Comment necessity threshold (score at least 8 of 10)|R14 Comment necessity threshold (score at least 8 of 10)]]
