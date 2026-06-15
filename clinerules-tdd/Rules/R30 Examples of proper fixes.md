---
tags: [rule, preference]
rule_type: PREFERENCE
source: "synthetic_test_data/.clinerules-tdd"
source_lines: "83–87"
---
# 💡 Examples of proper fixes

> **Examples of proper fixes:**
- ❌ `// eslint-disable-next-line react-refresh/only-export-components`
- ✅ Move test utilities to separate config that disables the rule for test files
- ✅ Replace `export *` with explicit named exports
- ✅ Capture ref values in effect scope to satisfy exhaustive-deps

**Type:** PREFERENCE  ·  **Source line:** 83–87

## Judgment
—

## Relations
- **support (exemplifies)** → [[clinerules-tdd/Rules/R27 When encountering lint-type errors|R27 When encountering lint-type errors]]
- **support (exemplifies)** → [[clinerules-tdd/Rules/R29 CONFIGURE - If the rule is genuinely inappropriate, update the config file…|R29 CONFIGURE - If the rule is genuinely inappropriate, update the config file…]]
