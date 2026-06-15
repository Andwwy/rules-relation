---
tags: [rule, prescription]
rule_type: PRESCRIPTION
source: "synthetic_test_data/.clinerules-tdd"
source_lines: "246"
---
# ✅ Enforcement: Before completing a debug task, verify all temporary files are deleted or…

> **Enforcement:** Before completing a debug task, verify all temporary files are deleted or in `tests/_temp_/`.

**Type:** PRESCRIPTION  ·  **Source line:** 246

## Judgment
—

## Relations
- **checkpoint** → [[clinerules-tdd/Rules/R81 Ad-hoc debug scripts, reproduction tests, or diagnostic files created during deb|R81 Ad-hoc debug scripts, reproduction tests, or diagnostic files created during deb]]
- **checkpoint** → [[clinerules-tdd/Rules/R84 Clean up after investigation completes|R84 Clean up after investigation completes]]
- **checkpoint** → [[clinerules-tdd/Rules/R80 keep repo clean|R80 keep repo clean]]
