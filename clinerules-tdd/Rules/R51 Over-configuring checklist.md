---
tags: [rule, prescription]
rule_type: PRESCRIPTION
hand_tag: "PRESCRIPTION"
llm_tag: "PRESCRIPTION"
annotator_agreement: agree
source: "adamglang/sovereign-core .clinerules"
---
# ✅ Over-configuring checklist

> When you catch yourself over-configuring: ASK is this a real behavioral dial? CHECK are we using it now or within 1-2 steps? If NO to both → well-named constant. If YES → existing config layer.

**Type:** PRESCRIPTION  ·  **Hand tag:** PRESCRIPTION  ·  **LLM tag:** PRESCRIPTION

## Judgment
Mirror image of R43 (over-planning recovery) for the config domain — same catch-yourself trigger, same decision-tree remedy. Inherits R42's 1-2-step horizon. Well-formed.

## Relations
- **checkpoint** → [[clinerules-tdd/Rules/R45 Centralize behavioral primitives in config|R45 Centralize behavioral primitives in config]]
