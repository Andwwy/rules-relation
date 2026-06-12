---
tags: [rule, prescription]
rule_type: PRESCRIPTION
hand_tag: "PRESCRIPTION"
llm_tag: "PRESCRIPTION"
annotator_agreement: agree
source: "adamglang/sovereign-core .clinerules"
---
# ✅ Descriptive keys with sensible defaults

> Config keys should be self-documenting (max_retry_attempts, llm_response_timeout_seconds). Always include sensible defaults so the system works out-of-the-box.

**Type:** PRESCRIPTION  ·  **Hand tag:** PRESCRIPTION  ·  **LLM tag:** PRESCRIPTION

## Judgment
Two merged micro-rules (naming + defaults). Good examples; 'sensible' is the only soft spot. The defaults clause feeds directly into R52's single-definition constraint.

## Relations
- **support** → [[clinerules-tdd/Rules/R45 Centralize behavioral primitives in config|R45 Centralize behavioral primitives in config]]
