---
tags: [rule, prescription]
rule_type: PRESCRIPTION
hand_tag: "PRESCRIPTION"
llm_tag: "PRESCRIPTION"
annotator_agreement: agree
source: "adamglang/sovereign-core .clinerules"
---
# ✅ STOP-ASK-WAIT protocol

> If you believe backward compatibility is necessary: 1. STOP immediately 2. ASK with a clear proposal (what, why, complexity cost, migration alternative) 3. WAIT for explicit instruction.

**Type:** PRESCRIPTION  ·  **Hand tag:** PRESCRIPTION  ·  **LLM tag:** PRESCRIPTION

## Judgment
Well-structured halt protocol with a concrete proposal checklist; annotator notes the trigger ('if you believe...') is self-assessed and vague. Duplicated almost verbatim by R56 in the meta-trigger section.

## Relations
- **refinement** → [[clinerules-tdd/Rules/R56 Stop when considering backward compatibility|R56 Stop when considering backward compatibility]] *(this rule is a coarse recap — adds nothing R35 does not entail)*
- **checkpoint** → [[clinerules-tdd/Rules/R34 Never independently implement backward compatibility|R34 Never independently implement backward compatibility]]
