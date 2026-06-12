---
tags: [rule, prohibition]
rule_type: PROHIBITION
hand_tag: "PROHIBITION"
llm_tag: "PROHIBITION"
annotator_agreement: agree
source: "adamglang/sovereign-core .clinerules"
---
# 🚫 Never over-architect or plan too far ahead

> NEVER over-architect or plan too far ahead. Build incrementally, validate constantly, maintain the ability to pivot.

**Type:** PROHIBITION  ·  **Hand tag:** PROHIBITION  ·  **LLM tag:** PROHIBITION

## Judgment
Agreed prohibition, but 'over-architect' is self-referentially vague — the file later supplies red-flag examples (designing for hypothetical extensibility, premature config systems) that do the real definitional work. This is 'Rule 6', the one R46 declares the winner of all conflicts.

## Relations
- **conflict** → [[clinerules-tdd/Rules/R40 Loose coupling and abstraction layers|R40 Loose coupling and abstraction layers]]
- **conflict** → [[clinerules-tdd/Rules/R45 Centralize behavioral primitives in config|R45 Centralize behavioral primitives in config]]
