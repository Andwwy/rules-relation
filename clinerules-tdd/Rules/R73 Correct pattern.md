---
tags: [rule, preference]
rule_type: PREFERENCE
source: "synthetic_test_data/.clinerules-tdd"
source_lines: "217–220"
---
# 💡 Correct pattern

> **Correct pattern:**
- ✅ Pydantic `Field(default=value)` in config.py - single source of truth
- ✅ Factories use `config["key"]` - direct access, no fallbacks
- ✅ Provider constructors require config params - no defaults for user-facing settings

**Type:** PREFERENCE  ·  **Source line:** 217–220

## Judgment
—

## Relations
- **support (exemplifies)** → [[clinerules-tdd/Rules/R72 Configuration values must have exactly ONE default definition|R72 Configuration values must have exactly ONE default definition]]
