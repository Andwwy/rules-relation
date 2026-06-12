---
tags: [rule, prescription]
rule_type: PRESCRIPTION
hand_tag: "PRESCRIPTION"
llm_tag: "PRESCRIPTION"
annotator_agreement: agree
source: "adamglang/sovereign-core .clinerules"
---
# ✅ Debug artifacts go in tests _temp_ dir

> Ad-hoc debug scripts, reproduction tests, or diagnostic files created during debugging must go in tests/_temp_/ for easy cleanup. Use descriptive names (debug_tts_state.py, repro_audio_hang.py).

**Type:** PRESCRIPTION  ·  **Hand tag:** PRESCRIPTION  ·  **LLM tag:** PRESCRIPTION

## Judgment
Concrete path, concrete examples — fully checkable. One of the most enforceable rules in the file.

## Relations
- **refinement** → [[clinerules-tdd/Rules/R58 Keep the repo clean|R58 Keep the repo clean]]
