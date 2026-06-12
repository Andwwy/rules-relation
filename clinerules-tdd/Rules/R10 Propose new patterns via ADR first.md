---
tags: [rule, prescription]
rule_type: PRESCRIPTION
hand_tag: "PREFERENCE"
llm_tag: "PRESCRIPTION"
annotator_agreement: disagree
source: "adamglang/sovereign-core .clinerules"
---
# ✅ Propose new patterns via ADR first

> If a new pattern seems necessary, propose it first with a short ADR draft in docs/adr (context, options, decision, consequences).

**Type:** PRESCRIPTION  ·  **Hand tag:** PREFERENCE  ·  **LLM tag:** PRESCRIPTION

## Judgment
Another hand/LLM tag split. The ADR content list makes it concretely checkable, which pushes it toward PRESCRIPTION. Acts as the sanctioned escape route from R09.

## Relations
- **exception** → [[clinerules-tdd/Rules/R09 No parallel patterns or dual sources of truth|R09 No parallel patterns or dual sources of truth]]
- **support** → [[clinerules-tdd/Rules/R43 Over-planning recovery protocol|R43 Over-planning recovery protocol]]
