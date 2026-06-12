---
tags: [rule, prescription]
rule_type: PRESCRIPTION
hand_tag: "PRESCRIPTION"
llm_tag: "PRESCRIPTION"
annotator_agreement: agree
source: "adamglang/sovereign-core .clinerules"
---
# ✅ Fix the root cause (escalation ladder)

> When encountering lint/type errors: 1. FIX THE ROOT CAUSE  2. RESTRUCTURE  3. CONFIGURE (config-file change with justification).

**Type:** PRESCRIPTION  ·  **Hand tag:** PRESCRIPTION  ·  **LLM tag:** PRESCRIPTION

## Judgment
A well-ordered escalation procedure. Hand interestingly tagged step 3 (CONFIGURE) as PERMISSION — defensible, since it licenses an otherwise-suspect action under conditions. The ladder gives R26 its positive counterpart.

## Relations
- **exception** → [[clinerules-tdd/Rules/R27 No suppression pragmas|R27 No suppression pragmas]]
- **support** → [[clinerules-tdd/Rules/R26 NEVER disable linting, compilation, or type errors|R26 NEVER disable linting, compilation, or type errors]]
