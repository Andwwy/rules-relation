---
tags: [context, rationale]
node_type: CONTEXT
context_type: rationale
grounds_count: 4
source: "adamglang/sovereign-core .clinerules"
---
# 🗒 Backward compat breeds dual sources of truth and compounding complexity

> Backward compatibility creates dual sources of truth that evolve independently, multiplies maintenance burden and bug surface, fragments the codebase into parallel implementations, prevents clean evolution, and adds permanent compounding complexity.

**Node type:** CONTEXT — no deontic force, cannot be violated; participates only in support-flavored relations (defines / exemplifies / motivates), and is one-to-many by nature.

## Role
Skipped by both CSV annotators, yet it is the justification for the entire S07 cluster and the explicit bridge from backward-compat to the dual-sources theme (R09). Justifies the prohibition and its forward-migration default; never determines compliance.

## Grounds (4 rules)
- **support (motivates)** → [[clinerules-tdd/Rules/R09 No parallel patterns or dual sources of truth|R09 No parallel patterns or dual sources of truth]]
- **support (motivates)** → [[clinerules-tdd/Rules/R34 Never independently implement backward compatibility|R34 Never independently implement backward compatibility]]
- **support (motivates)** → [[clinerules-tdd/Rules/R36 Migrate forward, delete the old pattern|R36 Migrate forward, delete the old pattern]]
- **support (motivates)** → [[clinerules-tdd/Rules/R37 Backward-compat exception|R37 Backward-compat exception]]
