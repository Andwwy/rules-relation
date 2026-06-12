---
tags: [rule, prescription]
rule_type: PRESCRIPTION
hand_tag: "PRESCRIPTION"
llm_tag: "PRESCRIPTION"
annotator_agreement: agree
source: "adamglang/sovereign-core .clinerules"
---
# ✅ Verify with the repo's existing toolchain

> After implementing: ensure formatting, linting, and tests run with the repo's existing toolchain. Use the existing package manager (detect via lockfile).

**Type:** PRESCRIPTION  ·  **Hand tag:** PRESCRIPTION  ·  **LLM tag:** PRESCRIPTION

## Judgment
Concrete and checkable; 'detect via lockfile' even supplies the detection method. Bridges the task protocol to S5's toolchain rules.

## Relations
- **support** → [[clinerules-tdd/Rules/R23 Respect existing toolchain and scripts|R23 Respect existing toolchain and scripts]]
- **support** → [[clinerules-tdd/Rules/R26 NEVER disable linting, compilation, or type errors|R26 NEVER disable linting, compilation, or type errors]]
- **duplication** → [[clinerules-tdd/Rules/R23 Respect existing toolchain and scripts|R23 Respect existing toolchain and scripts]]
