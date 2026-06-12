---
tags: [context, definition]
node_type: CONTEXT
context_type: definition
grounds_count: 4
source: "adamglang/sovereign-core .clinerules"
---
# 🗒 Signs of over-planning: future-proofing, premature config, deep hierarchies

> Over-planning red flags: abstractions for "future extensibility" not needed now; config systems before knowing what needs configuring; complex class hierarchies; features "because we'll need them eventually"; architectures for hypothetical scale.

**Node type:** CONTEXT — no deontic force, cannot be violated; participates only in support-flavored relations (defines / exemplifies / motivates), and is one-to-many by nature.

## Role
Annotator: 'not a rule but useful context'. It supplies the observable detection criteria that R43's self-assessed 'catch yourself over-planning' trigger lacks — this context is what rescues R43 (and the R57 tripwire) from unfalsifiability. The 'config before needed' flag also reaches into the config rules.

## Grounds (4 rules)
- **support (defines)** → [[clinerules-tdd/Rules/R38 Never over-architect or plan too far ahead|R38 Never over-architect or plan too far ahead]]
- **support (defines)** → [[clinerules-tdd/Rules/R43 Over-planning recovery protocol|R43 Over-planning recovery protocol]]
- **support (defines)** → [[clinerules-tdd/Rules/R45 Centralize behavioral primitives in config|R45 Centralize behavioral primitives in config]]
- **support (defines)** → [[clinerules-tdd/Rules/R57 Stop when planning beyond 1-2 steps|R57 Stop when planning beyond 1-2 steps]]
