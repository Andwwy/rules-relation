---
tags: [context, definition]
node_type: CONTEXT
context_type: definition
grounds_count: 1
source: "gemm/CLAUDE.md"
---
# 🗒 Max safe back-to-back FETCH-DISPATCH = number of columns

> Maximum safe back-to-back FETCH-DISPATCH operations = number of columns (each tile BRAM holds 128 NVs; each FETCH brings 128 NVs; N columns x 128 = capacity).

**Node type:** CONTEXT — no deontic force, cannot be violated; one-to-many support only.

## Role
A capacity constraint the partitioning/dispatch logic must respect; bounds R30.

## Grounds (1 rules)
- **support (defines)** → [[elastix_gemm/Rules/R30 Automatic partitioning across rows (V) and columns (C)|R30 Automatic partitioning across rows (V) and columns (C)]]
