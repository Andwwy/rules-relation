---
tags: [rule, permission]
rule_type: PERMISSION
hand_tag: "PREFERENCE"
llm_tag: "—"
annotator_agreement: hand-only
source: "adamglang/sovereign-core .clinerules"
---
# 🔓 Acceptable-comments whitelist

> Acceptable comments (when necessity ≥ 8): non-obvious invariants, footguns, links to ADRs, public API TSDoc.

**Type:** PERMISSION  ·  **Hand tag:** PREFERENCE  ·  **LLM tag:** —

## Judgment
Hand tagged PREFERENCE but functionally this is a PERMISSION — it enumerates what MAY be commented once R14's bar is met. Doubles as context that partially operationalizes R14's fuzzy score.

## Relations
- **exception** → [[clinerules-tdd/Rules/R14 Comment necessity threshold (score at least 8 of 10)|R14 Comment necessity threshold (score at least 8 of 10)]]
