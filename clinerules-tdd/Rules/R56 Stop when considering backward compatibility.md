---
tags: [rule, prescription]
rule_type: PRESCRIPTION
hand_tag: "PRESCRIPTION"
llm_tag: "PRESCRIPTION"
annotator_agreement: agree
source: "adamglang/sovereign-core .clinerules"
---
# ✅ Stop when considering backward compatibility

> If you're considering backward compatibility, STOP and ask for approval first.

**Type:** PRESCRIPTION  ·  **Hand tag:** PRESCRIPTION  ·  **LLM tag:** PRESCRIPTION

## Judgment
Pure duplicate of R35 (compressed). Redundancy is likely intentional reinforcement, but in a rule-consistency audit it counts as a duplicate norm.

## Relations
- **checkpoint** → [[clinerules-tdd/Rules/R34 Never independently implement backward compatibility|R34 Never independently implement backward compatibility]]
