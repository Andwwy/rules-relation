---
tags: [context, definition]
node_type: CONTEXT
context_type: definition
grounds_count: 2
source: "gemm/CLAUDE.md"
---
# 🗒 2-D tile array & mlp_bram weight storage

> 2-D Tile Array: 16x16 compute tiles in rows/columns; mlp_bram holds shared weights (right matrix) broadcast to all columns.

**Node type:** CONTEXT — no deontic force, cannot be violated; one-to-many support only.

## Role
Architectural definition grounding partitioning and modular-RTL rules.

## Grounds (2 rules)
- **support (defines)** → [[elastix_gemm/Rules/R30 Automatic partitioning across rows (V) and columns (C)|R30 Automatic partitioning across rows (V) and columns (C)]]
- **support (defines)** → [[elastix_gemm/Rules/R23 Keep core RTL modules modular and parameterized|R23 Keep core RTL modules modular and parameterized]]
