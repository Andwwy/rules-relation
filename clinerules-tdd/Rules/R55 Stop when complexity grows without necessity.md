---
tags: [rule, prescription]
rule_type: PRESCRIPTION
hand_tag: "PRESCRIPTION"
llm_tag: "PRESCRIPTION"
annotator_agreement: agree
source: "adamglang/sovereign-core .clinerules"
---
# ✅ Stop when complexity grows without necessity

> If complexity is increasing without clear necessity, stop and simplify.

**Type:** PRESCRIPTION  ·  **Hand tag:** PRESCRIPTION  ·  **LLM tag:** PRESCRIPTION

## Judgment
Runtime tripwire for R30/R38. 'Without clear necessity' is self-assessed — same weakness as every catch-yourself trigger in the file.

## Relations
- **checkpoint** → [[clinerules-tdd/Rules/R30 Prefer the simplest solution|R30 Prefer the simplest solution]]
- **checkpoint** → [[clinerules-tdd/Rules/R38 Never over-architect or plan too far ahead|R38 Never over-architect or plan too far ahead]]
