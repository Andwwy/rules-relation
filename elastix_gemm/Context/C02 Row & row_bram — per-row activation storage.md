---
tags: [context, definition]
node_type: CONTEXT
context_type: definition
grounds_count: 2
source: "gemm/CLAUDE.md"
---
# 🗒 Row & row_bram — per-row activation storage

> Row: a row of compute tiles, each with its own row_bram for activations (mapped to a GDDR6 channel); row_bram holds the left matrix.

**Node type:** CONTEXT — no deontic force, cannot be violated; one-to-many support only.

## Role
Hand-tagged PRESCRIPTION but it states an architectural fact, not an obligation — context. Grounds the partitioning and modular-RTL rules.

## Grounds (2 rules)
- **support (defines)** → [[elastix_gemm/Rules/R30 Automatic partitioning across rows (V) and columns (C)|R30 Automatic partitioning across rows (V) and columns (C)]]
- **support (defines)** → [[elastix_gemm/Rules/R23 Keep core RTL modules modular and parameterized|R23 Keep core RTL modules modular and parameterized]]
