---
tags: [rule, prescription]
rule_type: PRESCRIPTION
hand_tag: "PRESCRIPTION"
llm_tag: "PRESCRIPTION"
annotator_agreement: agree
source: "adamglang/sovereign-core .clinerules"
---
# ✅ Clean up and verify before finishing

> Clean up after investigation completes. Enforcement: before completing a debug task, verify all temporary files are deleted or in tests/_temp_/.

**Type:** PRESCRIPTION  ·  **Hand tag:** PRESCRIPTION  ·  **LLM tag:** PRESCRIPTION

## Judgment
Rare case where the rule names its own enforcement step ('Enforcement: ... verify'). The annotator asked elsewhere for an enforcement axis — this rule shows the file's author occasionally provided one.

## Relations
- **refinement** → [[clinerules-tdd/Rules/R58 Keep the repo clean|R58 Keep the repo clean]]
- **checkpoint** → [[clinerules-tdd/Rules/R45 Centralize behavioral primitives in config|R45 Centralize behavioral primitives in config]]
- **checkpoint** → [[clinerules-tdd/Rules/R59 Debug artifacts go in tests _temp_ dir|R59 Debug artifacts go in tests _temp_ dir]]
