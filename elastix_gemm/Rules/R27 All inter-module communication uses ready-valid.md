---
tags: [rule, prescription]
rule_type: PRESCRIPTION
hand_tag: "—"
llm_tag: "PRESCRIPTION"
annotator_agreement: disagree
source: "gemm/CLAUDE.md"
---
# ✅ All inter-module communication uses ready-valid

> All inter-module communication uses ready/valid protocol (ready/valid signals between all FSMs).

**Type:** PRESCRIPTION  ·  **Hand:** —  ·  **LLM:** PRESCRIPTION

## Judgment
Consolidates L117 and L127. Concretizes R07's 'adopt ready/valid' into a universal requirement.

## Relations
- **refinement** → [[elastix_gemm/Rules/R07 Adopt ready-valid, FIFO decoupling, AMD conventions|R07 Adopt ready-valid, FIFO decoupling, AMD conventions]]
