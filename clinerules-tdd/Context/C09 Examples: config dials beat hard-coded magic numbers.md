---
tags: [context, example]
node_type: CONTEXT
context_type: example
grounds_count: 3
source: "adamglang/sovereign-core .clinerules"
---
# 🗒 Examples: config dials beat hard-coded magic numbers

> ✅ llm_temperature: 0.7 in config ❌ hard-coded 0.7 in every call · ✅ wake_word_sensitivity in config ❌ magic number in detector · ❌ BYTES_PER_SAMPLE=2 in config when it's part of the audio format ✅ leave as a module constant.

**Node type:** CONTEXT — no deontic force, cannot be violated; participates only in support-flavored relations (defines / exemplifies / motivates), and is one-to-many by nature.

## Role
Operationalizes the centralize-config rules. Its last case illustrates the NEGATIVE boundary of definition C07 — an example clarifying a definition clarifying a rule (context can chain).

## Grounds (3 rules)
- **support (exemplifies)** → [[clinerules-tdd/Rules/R45 Centralize behavioral primitives in config|R45 Centralize behavioral primitives in config]]
- **support (exemplifies)** → [[clinerules-tdd/Rules/R47 Centralize incrementally|R47 Centralize incrementally]]
- **support (exemplifies)** → [[clinerules-tdd/Rules/R49 Descriptive keys with sensible defaults|R49 Descriptive keys with sensible defaults]]
