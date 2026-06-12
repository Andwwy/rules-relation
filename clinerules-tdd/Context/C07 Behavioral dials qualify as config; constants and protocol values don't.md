---
tags: [context, definition]
node_type: CONTEXT
context_type: definition
grounds_count: 4
source: "adamglang/sovereign-core .clinerules"
---
# 🗒 Behavioral dials qualify as config; constants and protocol values don't

> Qualifies: UX params (timeouts, retries, debounce), system behavior (log levels, TTLs, batch sizes), AI/ML settings (model, temperature), thresholds. Does NOT qualify: math constants, protocol-defined values, non-observable details, one-off values.

**Node type:** CONTEXT — no deontic force, cannot be violated; participates only in support-flavored relations (defines / exemplifies / motivates), and is one-to-many by nature.

## Role
Annotator: 'context for the following set of rules'. This definition makes the vague predicate 'behavioral primitive' decidable across the whole config cluster — without it those rules are unapplicable.

## Grounds (4 rules)
- **support (defines)** → [[clinerules-tdd/Rules/R45 Centralize behavioral primitives in config|R45 Centralize behavioral primitives in config]]
- **support (defines)** → [[clinerules-tdd/Rules/R47 Centralize incrementally|R47 Centralize incrementally]]
- **support (defines)** → [[clinerules-tdd/Rules/R49 Descriptive keys with sensible defaults|R49 Descriptive keys with sensible defaults]]
- **support (defines)** → [[clinerules-tdd/Rules/R51 Over-configuring checklist|R51 Over-configuring checklist]]
