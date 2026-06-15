---
tags: [rule, permission]
rule_type: PERMISSION
source: "synthetic_test_data/.clinerules-tdd"
source_lines: "21–23"
---
# 🔓 Fallbacks (CPU, reduced mode, mocks) are allowed ONLY if

> **Fallbacks (CPU, reduced mode, mocks) are allowed ONLY if:**
- Explicitly requested by the user, OR
- Already defined as an opt-in mode

**Type:** PERMISSION  ·  **Source line:** 21–23

## Judgment
—

## Relations
- **exception** → [[clinerules-tdd/Rules/R02 NEVER -fix- errors by disabling, downgrading, or bypassing core features (e.g.,|R02 NEVER -fix- errors by disabling, downgrading, or bypassing core features (e.g.,]]
- **exception** → [[clinerules-tdd/Rules/R06 Defaults must remain on the best-supported path|R06 Defaults must remain on the best-supported path]]
