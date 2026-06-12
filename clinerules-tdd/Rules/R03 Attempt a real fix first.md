---
tags: [rule, prescription]
rule_type: PRESCRIPTION
hand_tag: "PRESCRIPTION"
llm_tag: "—"
annotator_agreement: hand-only
source: "adamglang/sovereign-core .clinerules"
---
# ✅ Attempt a real fix first

> Attempt a real fix - correct package, version, PATH, provider, config

**Type:** PRESCRIPTION  ·  **Hand tag:** PRESCRIPTION  ·  **LLM tag:** —

## Judgment
Gives direction but is vague ('real fix' is defined only by contrast with R01's banned workarounds). Functions as step 1 of the error-handling procedure that R04 continues.

## Relations
- **support** → [[clinerules-tdd/Rules/R01 No silent downgrades|R01 No silent downgrades]]
