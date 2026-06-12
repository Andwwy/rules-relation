---
tags: [context, example]
node_type: CONTEXT
context_type: example
grounds_count: 3
source: "adamglang/sovereign-core .clinerules"
---
# 🗒 Examples: one Pydantic default beats defaults duplicated across factories

> ✅ Pydantic Field(default=value) as the single source · ✅ factories use config["key"] with no fallbacks · ❌ config.get("model", "gpt-4o-mini") in a factory · ❌ def __init__(self, temperature=0.7) in a provider.

**Node type:** CONTEXT — no deontic force, cannot be violated; participates only in support-flavored relations (defines / exemplifies / motivates), and is one-to-many by nature.

## Role
Also hand-tagged PREFERENCE; same misclassification as C10. These ✅/❌ cases are what make the single-default rule mechanically checkable, and they reinforce the no-parallel-config-sources rule.

## Grounds (3 rules)
- **support (exemplifies)** → [[clinerules-tdd/Rules/R49 Descriptive keys with sensible defaults|R49 Descriptive keys with sensible defaults]]
- **support (exemplifies)** → [[clinerules-tdd/Rules/R50 No duplicate or parallel config sources|R50 No duplicate or parallel config sources]]
- **support (exemplifies)** → [[clinerules-tdd/Rules/R52 Exactly ONE default definition|R52 Exactly ONE default definition]]
