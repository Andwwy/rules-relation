---
tags: [rule, prohibition]
rule_type: PROHIBITION
hand_tag: "PROHIBITION"
llm_tag: "PROHIBITION"
annotator_agreement: agree
source: "adamglang/sovereign-core .clinerules"
---
# 🚫 Never disable core features to fix errors

> NEVER "fix" errors by disabling, downgrading, or bypassing core features (e.g., turning off GPU/CUDA, reducing quality, changing defaults, switching to CPU).

**Type:** PROHIBITION  ·  **Hand tag:** PROHIBITION  ·  **LLM tag:** PROHIBITION

## Judgment
Clear deontic force, good examples, hand and LLM agree. Residual vagueness: 'core feature' has no concrete definition (annotator flagged this) — the examples gesture at GPU/quality but the boundary is open.

## Relations
- **refinement** → [[clinerules-tdd/Rules/R01 No silent downgrades|R01 No silent downgrades]]
- **duplication** → [[clinerules-tdd/Rules/R06 Defaults stay on best-supported path|R06 Defaults stay on best-supported path]]
