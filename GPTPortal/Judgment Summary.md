---
tags: [judgment, moc]
---
# Judgment Summary — GPTPortal (`RULES.md`)

## 1. A values document, not an operational playbook
Where elastix_gemm is concrete and checkable, this file is dominated by **slogans and preferences**: 'always follow best practices', 'think deeply', 'final solution must be perfect'. The annotator's repeated complaints ('what are best practices?', 'super vague', 'feels softer') track exactly the rules that resist enforcement. The teeth are a minority — the coding-standards and architecture rules.

## 2. One real hierarchy: the architecture anchor
[[GPTPortal/Rules/R26 Prioritize modularity, DRY, performance, and security|R26]] is the hub of the file — its four pillars are each operationalized by concrete rules: R27/R33/R34/R39 (modularity), R31/R37 (DRY), R42 (performance), R41 (security). The cleanest refinement fan in the corpus.

## 3. The workflow is a decomposition, not a refinement
[[GPTPortal/Rules/R04 Core Workflow - Research to Validate|R04]] has four phase-rules (R05-R09). They don't *entail* the parent (doing 'Research' isn't doing the whole workflow), so they are modeled as **support**, not refinement — a deliberate contrast with the R26 fan.

## 4. Two genuine conflicts
- [[GPTPortal/Rules/R21 No opt-in follow-up suggestions unless relevant|R21]] (no follow-up suggestions) vs [[GPTPortal/Rules/R23 End responses with the History-Source Tree-Next Task template|R23]] (the end-template *mandates* a 'Next Task: suggestions' block). A direct contradiction, unresolved.
- [[GPTPortal/Rules/R45 Iterate until the problem is fully solved|R45]] (never stop) vs [[GPTPortal/Rules/R10 3-Try Rule - stop and reflect after three failed attempts|R10]] (stop after three tries). Persistence-vs-stop, no priority rule.

## 5. Redundancy from layered authorship
The file stitches several prompt sources, so norms recur: R36 (fix root cause, don't game tests) ≈ R44 (never take the easy path); R16 restates both. Duplications, not refinements.

## 6. Format-as-context
The start/end response templates are format **specifications**, not norms — modeled as context (C01/C02) that grounds the format rules R22/R23. C02 is also the literal source of the R21/R23 conflict.

## Counts
45 rules + 4 context. Prescription/preference-heavy; one permission (R43), few hard prohibitions.

Up: [[GPTPortal/GPTPortal MOC|GPTPortal MOC]]
