---
tags: [context, definition]
node_type: CONTEXT
context_type: definition
grounds_count: 1
source: "gemm/CLAUDE.md"
---
# 🗒 Partition distribution formulas

> First (V % num_rows) rows get (V/num_rows + 1) NVs; first (C % num_cols) columns get (C/num_cols + 1) NVs; distribute evenly, remainder to lower-indexed partitions.

**Node type:** CONTEXT — no deontic force, cannot be violated; one-to-many support only.

## Role
These formulas define exactly how R30's 'automatic partitioning' behaves — the rule is unverifiable without them.

## Grounds (1 rules)
- **support (defines)** → [[elastix_gemm/Rules/R30 Automatic partitioning across rows (V) and columns (C)|R30 Automatic partitioning across rows (V) and columns (C)]]
