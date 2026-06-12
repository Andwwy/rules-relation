---
tags: [context, definition]
node_type: CONTEXT
context_type: definition
grounds_count: 2
source: "gemm/CLAUDE.md"
---
# 🗒 Dual-Memory Architecture — BRAM vs GDDR6

> Dual-Memory Architecture: BRAM for low-latency result storage and command buffering; GDDR6 for high-bandwidth matrix data.

**Node type:** CONTEXT — no deontic force, cannot be violated; one-to-many support only.

## Role
Hand-tagged PREFERENCE ('could be prescription'); really a structural definition that grounds the control/data separation rule.

## Grounds (2 rules)
- **support (defines)** → [[elastix_gemm/Rules/R33 Separate control and data paths|R33 Separate control and data paths]]
- **support (defines)** → [[elastix_gemm/Rules/R03 MS2.0 modular design with clear boundaries|R03 MS2.0 modular design with clear boundaries]]
