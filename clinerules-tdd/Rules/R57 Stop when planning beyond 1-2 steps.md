---
tags: [rule, prescription]
rule_type: PRESCRIPTION
hand_tag: "PRESCRIPTION"
llm_tag: "PRESCRIPTION"
annotator_agreement: agree
source: "adamglang/sovereign-core .clinerules"
---
# ✅ Stop when planning beyond 1-2 steps

> If you're planning more than 1-2 steps ahead or building for hypothetical future needs, STOP and simplify to current requirements.

**Type:** PRESCRIPTION  ·  **Hand tag:** PRESCRIPTION  ·  **LLM tag:** PRESCRIPTION

## Judgment
Duplicate of R42 + R43 compressed into a tripwire. Same reinforcement-by-repetition authoring style.

## Relations
- **checkpoint** → [[clinerules-tdd/Rules/R38 Never over-architect or plan too far ahead|R38 Never over-architect or plan too far ahead]]
- **checkpoint** → [[clinerules-tdd/Rules/R42 Plan one or two steps ahead, not ten|R42 Plan one or two steps ahead, not ten]]
