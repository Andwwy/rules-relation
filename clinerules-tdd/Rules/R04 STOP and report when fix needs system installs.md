---
tags: [rule, prescription]
rule_type: PRESCRIPTION
hand_tag: "PRESCRIPTION"
llm_tag: "PRESCRIPTION"
annotator_agreement: agree
source: "adamglang/sovereign-core .clinerules"
---
# ✅ STOP and report when fix needs system installs

> If the fix requires system installs or user action, STOP and report: what is missing, why, how to install/verify, commands to diagnose.

**Type:** PRESCRIPTION  ·  **Hand tag:** PRESCRIPTION  ·  **LLM tag:** PRESCRIPTION

## Judgment
One of the best-formed rules in the file: concrete trigger (system installs / user action), explicit halt, and a 4-item report checklist. Fully checkable. Member of the recurring STOP-and-ask family.

## Relations
- **support** → [[clinerules-tdd/Rules/R01 No silent downgrades|R01 No silent downgrades]]
