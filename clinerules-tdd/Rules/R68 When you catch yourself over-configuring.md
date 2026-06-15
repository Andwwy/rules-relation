---
tags: [rule, prescription]
rule_type: PRESCRIPTION
source: "synthetic_test_data/.clinerules-tdd"
source_lines: "197–201"
---
# ✅ When you catch yourself over-configuring

> **When you catch yourself over-configuring:**
1. **ASK:** "Is this value actually a behavioral dial users/operators will want to adjust?"
2. **CHECK:** "Are we using this now, or will we clearly need to tune it in the next 1-2 steps?"
3. **If NO to both:** Leave it as a well-named constant in the module where it's used
4. **If YES:** Add it to the existing config layer with a descriptive name and default

**Type:** PRESCRIPTION  ·  **Source line:** 197–201

## Judgment
—

## Relations
- **checkpoint** → [[clinerules-tdd/Rules/R60 Make meaningful behavioral dials discoverable and changeable from a single sourc|R60 Make meaningful behavioral dials discoverable and changeable from a single sourc]]
- **support** → [[clinerules-tdd/Rules/R44 NEVER over-architect or plan too far ahead|R44 NEVER over-architect or plan too far ahead]]
