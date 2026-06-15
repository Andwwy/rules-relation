---
tags: [rule]
rule_type: UNKNOWN
source: "synthetic_test_data/.clinerules-tdd"
source_lines: "172–182"
---
# • What qualifies as a configurable primitive

> **What qualifies as a configurable primitive:**
- **UX parameters:** Token limits, response timeouts, retry attempts, debounce delays, animation durations
- **System behavior:** Logging levels, verbosity settings, polling intervals, cache TTLs, batch sizes
- **AI/ML settings:** Model names, temperature, max tokens, voice types, wake word sensitivity
- **Thresholds:** Confidence scores, rate limits, queue depths, memory thresholds

**What does NOT qualify:**
- Mathematical constants (π, conversion factors)
- Protocol-defined values (HTTP status codes, standard ports)
- Arbitrary implementation details that don't affect observable behavior
- Values that appear once and have no foreseeable reason to change

**Type:** UNKNOWN  ·  **Source line:** 172–182

## Judgment
—

## Relations
- **support (defines)** → [[clinerules-tdd/Rules/R59 Primitive values that control UX or system behavior should live in a centralized|R59 Primitive values that control UX or system behavior should live in a centralized]]
