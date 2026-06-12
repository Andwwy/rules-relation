---
tags: [rule, prescription]
rule_type: PRESCRIPTION
hand_tag: "—"
llm_tag: "PRESCRIPTION"
annotator_agreement: disagree
source: "gemm/CLAUDE.md"
---
# ✅ Run test_registers after every change or hardware op

> After any change, run test_registers to verify device health (run after every hardware operation).

**Type:** PRESCRIPTION  ·  **Hand:** —  ·  **LLM:** PRESCRIPTION

## Judgment
Consolidates L91 and L147. A checkpoint: it adds no new code obligation, only a designated moment to verify device health against R02's robustness.

## Relations
- **checkpoint** → [[elastix_gemm/Rules/R02 All code should be robust and validated|R02 All code should be robust and validated]]
