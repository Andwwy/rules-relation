---
tags: [rule, prescription]
rule_type: PRESCRIPTION
hand_tag: "PREFERENCE"
llm_tag: "PRESCRIPTION"
annotator_agreement: disagree
source: "adamglang/sovereign-core .clinerules"
---
# ✅ Prefer the simplest solution

> ALWAYS prefer the simplest solution that meets the specification. Actively reduce complexity rather than add it. Lower complexity is a primary goal, second only to meeting the spec.

**Type:** PRESCRIPTION  ·  **Hand tag:** PREFERENCE  ·  **LLM tag:** PRESCRIPTION

## Judgment
'ALWAYS prefer' is an oxymoronic construction — preference verb, prescription quantifier — which explains the hand/LLM tag split. Crucially, this sentence states an explicit priority ordering (spec > simplicity > everything else), one of only two places the file ranks its own rules.

## Relations
- **conflict** → [[clinerules-tdd/Rules/R40 Loose coupling and abstraction layers|R40 Loose coupling and abstraction layers]]
- **conflict** → [[clinerules-tdd/Rules/R45 Centralize behavioral primitives in config|R45 Centralize behavioral primitives in config]]
