---
tags: [rule, preference]
rule_type: PREFERENCE
source: "synthetic_test_data/.clinerules-tdd"
source_lines: "222–225"
---
# 💡 Violations to avoid

> **Violations to avoid:**
- ❌ `config.get("model", "gpt-4o-mini")` in factory when LLMConfig already has this default
- ❌ `def __init__(self, temperature: float = 0.7)` in provider when config defines it
- ❌ Any duplicate default value in multiple locations

**Type:** PREFERENCE  ·  **Source line:** 222–225

## Judgment
—

## Relations
- **support (exemplifies)** → [[clinerules-tdd/Rules/R72 Configuration values must have exactly ONE default definition|R72 Configuration values must have exactly ONE default definition]]
