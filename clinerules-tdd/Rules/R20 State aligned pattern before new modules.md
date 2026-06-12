---
tags: [rule, prescription]
rule_type: PRESCRIPTION
hand_tag: "(untagged)"
llm_tag: "PRESCRIPTION"
annotator_agreement: untagged
source: "adamglang/sovereign-core .clinerules"
---
# ✅ State aligned pattern before new modules

> Before writing a new module/component: show which existing pattern or module you will align with and where it lives.

**Type:** PRESCRIPTION  ·  **Hand tag:** (untagged)  ·  **LLM tag:** PRESCRIPTION

## Judgment
Hand left untagged with 'gives obligation but vague'. The 'where it lives' requirement actually makes it more checkable than R12, which it otherwise duplicates.

## Relations
- **refinement** → [[clinerules-tdd/Rules/R12 Summarize chosen pattern before coding|R12 Summarize chosen pattern before coding]]
- **checkpoint** → [[clinerules-tdd/Rules/R07 Search repo before writing new patterns|R07 Search repo before writing new patterns]]
