---
tags: [rule, permission]
rule_type: PERMISSION
hand_tag: "PRESCRIPTION"
llm_tag: "—"
annotator_agreement: hand-only
source: "adamglang/sovereign-core .clinerules"
---
# 🔓 Exception: truly irreversible decisions

> If a decision is truly irreversible (database choice, foundational architecture), invest appropriate planning time. But these are rarer than they seem.

**Type:** PERMISSION  ·  **Hand tag:** PRESCRIPTION  ·  **LLM tag:** —

## Judgment
Hand tagged PRESCRIPTION but the logical role is a PERMISSION carved out of R38 (it licenses otherwise-banned up-front planning). Annotator rightly flags both 'truly irreversible' and 'appropriate planning time' as vague.

## Relations
- **exception** → [[clinerules-tdd/Rules/R38 Never over-architect or plan too far ahead|R38 Never over-architect or plan too far ahead]]
- **exception** → [[clinerules-tdd/Rules/R39 Build iteratively, validate early|R39 Build iteratively, validate early]]
