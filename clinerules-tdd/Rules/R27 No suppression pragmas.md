---
tags: [rule, prohibition]
rule_type: PROHIBITION
hand_tag: "PROHIBITION"
llm_tag: "PROHIBITION"
annotator_agreement: agree
source: "adamglang/sovereign-core .clinerules"
---
# 🚫 No suppression pragmas

> Do not use eslint-disable, @ts-ignore, @ts-expect-error, or similar pragmas to bypass linting or type errors.

**Type:** PROHIBITION  ·  **Hand tag:** PROHIBITION  ·  **LLM tag:** PROHIBITION

## Judgment
Maximally enforceable — these are literal grep-able strings. The best-specified prohibition in the corpus.

## Relations
- **refinement** → [[clinerules-tdd/Rules/R26 NEVER disable linting, compilation, or type errors|R26 NEVER disable linting, compilation, or type errors]]
