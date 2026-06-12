---
tags: [rule, prohibition]
rule_type: PROHIBITION
hand_tag: "PROHIBITION"
llm_tag: "PROHIBITION"
annotator_agreement: agree
source: "adamglang/sovereign-core .clinerules"
---
# 🚫 Exactly ONE default definition

> Configuration values must have exactly ONE default definition. Never duplicate defaults across config models, factories, or provider constructors. (✅ Pydantic Field(default=...) as single source ❌ config.get('model', 'gpt-4o-mini') fallbacks)

**Type:** PROHIBITION  ·  **Hand tag:** PROHIBITION  ·  **LLM tag:** PROHIBITION

## Judgment
Exceptionally well-specified: the correct-pattern/violation examples make it mechanically checkable. The strongest concrete instance of the anti-duplication theme.

## Relations
- **refinement** → [[clinerules-tdd/Rules/R09 No parallel patterns or dual sources of truth|R09 No parallel patterns or dual sources of truth]]
- **refinement** → [[clinerules-tdd/Rules/R50 No duplicate or parallel config sources|R50 No duplicate or parallel config sources]]
