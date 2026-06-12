---
tags: [rule, prescription]
rule_type: PRESCRIPTION
hand_tag: "PRESCRIPTION"
llm_tag: "PRESCRIPTION"
annotator_agreement: agree
source: "adamglang/sovereign-core .clinerules"
---
# ✅ Stop on duplicate or conflicting patterns

> If a proposed change creates a duplicate or conflicting pattern, stop and propose consolidation or a refactor plan instead.

**Type:** PRESCRIPTION  ·  **Hand tag:** PRESCRIPTION  ·  **LLM tag:** PRESCRIPTION

## Judgment
Runtime tripwire enforcing R09. Same halt-and-propose shape as R35.

## Relations
- **checkpoint** → [[clinerules-tdd/Rules/R09 No parallel patterns or dual sources of truth|R09 No parallel patterns or dual sources of truth]]
