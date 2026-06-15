---
tags: [rule, prescription]
rule_type: PRESCRIPTION
source: "synthetic_test_data/.clinerules-tdd"
source_lines: "106–114"
---
# ✅ If you believe backward compatibility is necessary

> If you believe backward compatibility is necessary:

1. **STOP** implementation immediately
2. **ASK** the user for explicit approval with a clear proposal:
   - What will be maintained for backward compatibility
   - Why it's necessary
   - What complexity it adds
   - What the migration path would be instead
3. **WAIT** for explicit instruction before proceeding

**Type:** PRESCRIPTION  ·  **Source line:** 106–114

## Judgment
—

## Relations
- **support** → [[clinerules-tdd/Rules/R39 NEVER independently implement backward compatibility, multi-version support, or|R39 NEVER independently implement backward compatibility, multi-version support, or]]
- **support** → [[clinerules-tdd/Rules/R78 If you're considering backward compatibility, STOP and ask for approval first|R78 If you're considering backward compatibility, STOP and ask for approval first]]
