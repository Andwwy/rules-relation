---
tags: [rule, preference]
rule_type: PREFERENCE
hand_tag: "PREFERENCE"
llm_tag: "PREFERENCE"
annotator_agreement: agree
source: "adamglang/sovereign-core .clinerules"
---
# 💡 Loose coupling and abstraction layers

> Avoid tight coupling. Use abstraction layers (interfaces, adapters) for external dependencies. Prefer dependency injection over direct imports. Keep business logic separate from framework code.

**Type:** PREFERENCE  ·  **Hand tag:** PREFERENCE  ·  **LLM tag:** PREFERENCE

## Judgment
Consolidates four pro-abstraction preferences. This cluster is the file's biggest internal tension: R30/R31 say fewest layers and R32 says distrust abstractions, while this says add interfaces, adapters and DI. No priority rule arbitrates this specific conflict — the genuine gap in the rule system.

## Relations
*(target only — incoming relations via backlinks)*
