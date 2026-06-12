---
tags: [context, definition]
node_type: CONTEXT
context_type: definition
grounds_count: 2
source: "gemm/CLAUDE.md"
---
# 🗒 Buffering patterns — circular & hierarchical

> Circular Buffer Pattern: dual-pointer (rd_ptr/wr_ptr) streaming. Hierarchical Buffering: multiple BRAM levels to decouple stages.

**Node type:** CONTEXT — no deontic force, cannot be violated; one-to-many support only.

## Role
Named architectural patterns (hand: PREFERENCE) that ground the FIFO/decoupling and modular rules.

## Grounds (2 rules)
- **support (defines)** → [[elastix_gemm/Rules/R28 FIFOs between pipeline stages for flow control|R28 FIFOs between pipeline stages for flow control]]
- **support (defines)** → [[elastix_gemm/Rules/R03 MS2.0 modular design with clear boundaries|R03 MS2.0 modular design with clear boundaries]]
