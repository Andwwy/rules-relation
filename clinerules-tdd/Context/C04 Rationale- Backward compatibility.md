---
tags: [context]
node_type: CONTEXT
grounds_count: 2
source: "synthetic_test_data/.clinerules-tdd"
---
# 🗒 Rationale: Backward compatibility

> **Rationale:** Backward compatibility:
- Creates dual sources of truth that evolve independently
- Multiplies maintenance burden and bug surface area
- Fragments the codebase into parallel implementations
- Prevents clean evolution toward better patterns
- Adds permanent complexity that compounds over time

**Node type:** CONTEXT — no deontic force; participates only in support relations.

## Role
It gives reasons backward compatibility is bad, explanatory background not a directive.

## Grounds (2 rules)
- **support (motivates)** → [[clinerules-tdd/Rules/R39 NEVER independently implement backward compatibility, multi-version support, or|R39 NEVER independently implement backward compatibility, multi-version support, or]]
- **support (motivates)** → [[clinerules-tdd/Rules/R38 The phrase -backward compatibility- is a CRITICAL WARNING SIGN|R38 The phrase -backward compatibility- is a CRITICAL WARNING SIGN]]
