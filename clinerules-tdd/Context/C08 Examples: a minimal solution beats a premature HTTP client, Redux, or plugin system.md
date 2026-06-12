---
tags: [context, example]
node_type: CONTEXT
context_type: example
grounds_count: 3
source: "adamglang/sovereign-core .clinerules"
---
# 🗒 Examples: a minimal solution beats a premature HTTP client, Redux, or plugin system

> ✅ simple fetch wrapper ❌ complex HTTP client with retry/caching/queuing up front · ✅ hard-code API endpoint ❌ multi-env config for a single-env app · ✅ useState ❌ Redux "because we might need global state" · ✅ write the feature ❌ design a plugin system first.

**Node type:** CONTEXT — no deontic force, cannot be violated; participates only in support-flavored relations (defines / exemplifies / motivates), and is one-to-many by nature.

## Role
Paired ✅/❌ cases that operationalize Rule 6 — the cheapest form of checkability. The HTTP-client and plugin cases also illustrate the coupling/abstraction rule.

## Grounds (3 rules)
- **support (exemplifies)** → [[clinerules-tdd/Rules/R38 Never over-architect or plan too far ahead|R38 Never over-architect or plan too far ahead]]
- **support (exemplifies)** → [[clinerules-tdd/Rules/R40 Loose coupling and abstraction layers|R40 Loose coupling and abstraction layers]]
- **support (exemplifies)** → [[clinerules-tdd/Rules/R42 Plan one or two steps ahead, not ten|R42 Plan one or two steps ahead, not ten]]
