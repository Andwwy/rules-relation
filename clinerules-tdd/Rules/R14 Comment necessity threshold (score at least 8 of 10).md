---
tags: [rule, prescription]
rule_type: PRESCRIPTION
hand_tag: "PREFERENCE"
llm_tag: "PROHIBITION"
annotator_agreement: disagree
source: "adamglang/sovereign-core .clinerules"
---
# ✅ Comment necessity threshold (score at least 8 of 10)

> Before adding any comment, rate 1-10 how necessary it is; if less than 8, do not add the comment.

**Type:** PRESCRIPTION  ·  **Hand tag:** PREFERENCE  ·  **LLM tag:** PROHIBITION

## Judgment
Three-way framing: hand tagged the rating ritual PREFERENCE and the cutoff PRESCRIPTION; the LLM collapsed both into a PROHIBITION. The pseudo-quantitative threshold is clever prompt engineering but unfalsifiable — the score is self-assigned, so the rule is really 'default to no comment'.

## Relations
- **support** → [[clinerules-tdd/Rules/R43 Over-planning recovery protocol|R43 Over-planning recovery protocol]]
