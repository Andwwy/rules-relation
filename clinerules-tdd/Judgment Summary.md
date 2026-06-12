---
tags: [judgment, moc]
---
# Judgment Summary

Overall verdict on the sovereign-core `.clinerules` rule set, consolidated from 100+ annotation rows into 60 unique rules.

## 1. The file has a deliberate architecture
Almost every cluster follows the same template: **slogan anchor → concrete refinements → gated PERMISSION exception → STOP-tripwire enforcement**. The four exceptions ([[clinerules-tdd/Rules/R05 Fallbacks only if requested or opt-in|R05 Fallbacks only if requested or opt-in]], [[clinerules-tdd/Rules/R29 Exception for generated and third-party code|R29 Exception for generated and third-party code]], [[clinerules-tdd/Rules/R37 Backward-compat exception|R37 Backward-compat exception]], [[clinerules-tdd/Rules/R53 Provider-level defaults exception|R53 Provider-level defaults exception]]) share an identical logical shape: narrowly carved out of a hard prohibition, gated on explicit user instruction.

## 2. Explicit hierarchy exists, but only once
[[clinerules-tdd/Rules/R46 Rule hierarchy - Rule 6 wins|R46]] is the file's only priority meta-rule: when config centralization conflicts with the Evolving Architecture Mandate, [[clinerules-tdd/Rules/R38 Never over-architect or plan too far ahead|R38 Never over-architect or plan too far ahead]] wins. [[clinerules-tdd/Rules/R30 Prefer the simplest solution|R30 Prefer the simplest solution]] adds a second partial ordering (spec > simplicity).

## 3. One genuine unresolved conflict
[[clinerules-tdd/Rules/R40 Loose coupling and abstraction layers|R40 Loose coupling and abstraction layers]] (use interfaces, adapters, DI) directly conflicts with [[clinerules-tdd/Rules/R30 Prefer the simplest solution|R30 Prefer the simplest solution]] (fewest layers) and [[clinerules-tdd/Rules/R32 Question every abstraction|R32 Question every abstraction]]. Unlike the config conflict, **no priority rule arbitrates this** — the biggest gap in the rule system. An agent told to wrap every external dependency in an adapter while also choosing the fewest abstractions has no tie-breaker.

## 4. Intentional redundancy
The S10 tripwires duplicate earlier rules ([[clinerules-tdd/Rules/R56 Stop when considering backward compatibility|R56 Stop when considering backward compatibility]] ≈ [[clinerules-tdd/Rules/R35 STOP-ASK-WAIT protocol|R35]]; [[clinerules-tdd/Rules/R57 Stop when planning beyond 1-2 steps|R57 Stop when planning beyond 1-2 steps]] ≈ [[clinerules-tdd/Rules/R42 Plan one or two steps ahead, not ten|R42 Plan one or two steps ahead, not ten]] + [[clinerules-tdd/Rules/R43 Over-planning recovery protocol|R43 Over-planning recovery protocol]]). Likely reinforcement-by-repetition for LLM consumption, but formally duplicate norms. Also [[clinerules-tdd/Rules/R20 State aligned pattern before new modules|R20 State aligned pattern before new modules]] ≈ [[clinerules-tdd/Rules/R12 Summarize chosen pattern before coding|R12 Summarize chosen pattern before coding]], and [[clinerules-tdd/Rules/R06 Defaults stay on best-supported path|R06 Defaults stay on best-supported path]] largely restates [[clinerules-tdd/Rules/R01 No silent downgrades|R01 No silent downgrades]].

## 5. Hand vs LLM tag disagreements cluster on 'should/prefer/avoid' wording
~10 rules got different tags from the two annotators (e.g. [[clinerules-tdd/Rules/R08 Align with established approaches|R08 Align with established approaches]], [[clinerules-tdd/Rules/R14 Comment necessity threshold (score at least 8 of 10)|R14]], [[clinerules-tdd/Rules/R22 Ask for clarification when uncertain|R22 Ask for clarification when uncertain]], [[clinerules-tdd/Rules/R24 No new libraries without approval|R24 No new libraries without approval]], [[clinerules-tdd/Rules/R45 Centralize behavioral primitives in config|R45 Centralize behavioral primitives in config]]). The pattern: the hand annotator tagged by **surface verb** (should/prefer → PREFERENCE), the LLM by **deontic function** (blocking obligation → PRESCRIPTION, approval-gated → PROHIBITION). Worth standardizing in the annotation guideline.

## 6. Enforceability is bimodal
- **Mechanically checkable:** [[clinerules-tdd/Rules/R27 No suppression pragmas|R27 No suppression pragmas]] (grep-able strings), [[clinerules-tdd/Rules/R52 Exactly ONE default definition|R52 Exactly ONE default definition]] (with ✅/❌ examples), [[clinerules-tdd/Rules/R59 Debug artifacts go in tests _temp_ dir|R59]] (concrete path), [[clinerules-tdd/Rules/R17 TODOs - don't create, don't remove|R17]].
- **Self-assessed and unfalsifiable:** every 'when you catch yourself X' trigger ([[clinerules-tdd/Rules/R43 Over-planning recovery protocol|R43 Over-planning recovery protocol]], [[clinerules-tdd/Rules/R51 Over-configuring checklist|R51 Over-configuring checklist]]), the ≥8/10 comment score ([[clinerules-tdd/Rules/R14 Comment necessity threshold (score at least 8 of 10)|R14]]), and 'maximum information' ([[clinerules-tdd/Rules/R41 Defer irreversible decisions|R41 Defer irreversible decisions]]).

## 7. Missing categories the annotator's comments anticipate
The user_comments repeatedly note items that are **context, not rules** (red-flag lists, what-qualifies lists, the warning-sign framing [[clinerules-tdd/Context/C02 The phrase 'backward compatibility' is a warning sign|C02 The phrase 'backward compatibility' is a warning sign]]). A `CONTEXT`/`DEFINITION` tag alongside the four deontic types would clean up the taxonomy, as would an **enforcement axis** (the annotator explicitly asked for one; [[clinerules-tdd/Rules/R60 Clean up and verify before finishing|R60 Clean up and verify before finishing]] shows the file itself sometimes names its enforcement).

## Counts
60 rules: 14 🚫 prohibitions · 31 ✅ prescriptions · 9 💡 preferences · 6 🔓 permissions, across 11 sections.

Up: [[clinerules-tdd/Sovereign-Core Rules MOC|Sovereign-Core Rules MOC]]
