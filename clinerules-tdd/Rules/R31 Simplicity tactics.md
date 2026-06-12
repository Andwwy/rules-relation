---
tags: [rule, prescription]
rule_type: PRESCRIPTION
hand_tag: "PRESCRIPTION"
llm_tag: "PRESCRIPTION"
annotator_agreement: agree
source: "adamglang/sovereign-core .clinerules"
---
# ✅ Simplicity tactics

> Choose the solution with fewest moving parts. Eliminate redundant code, duplicate patterns, or parallel implementations. Refactor complex solutions into simpler ones when discovered.

**Type:** PRESCRIPTION  ·  **Hand tag:** PRESCRIPTION  ·  **LLM tag:** PRESCRIPTION

## Judgment
Three concrete tactics consolidated from separate annotations (with minor hand/LLM tag splits on individual bullets). 'When discovered' gives the refactor clause an event trigger, which is good rule design.

## Relations
- **support** → [[clinerules-tdd/Rules/R09 No parallel patterns or dual sources of truth|R09 No parallel patterns or dual sources of truth]]
- **support** → [[clinerules-tdd/Rules/R30 Prefer the simplest solution|R30 Prefer the simplest solution]]
