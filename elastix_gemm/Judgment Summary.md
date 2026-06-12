---
tags: [judgment, moc]
---
# Judgment Summary — elastix_gemm (`gemm/CLAUDE.md`)

## 1. This file is half dictionary, half workflow
Unlike a typical rules file, ~40% of the annotated rows are **architectural definitions** (terminology, tile layout, distribution formulas), not norms. I moved these to **Context** — they have no deontic force (you cannot 'violate' the definition of a Native Vector), but they are load-bearing: [[elastix_gemm/Rules/R30 Automatic partitioning across rows (V) and columns (C)|R30]] is meaningless without the distribution formulas in [[elastix_gemm/Context/C05 Partition distribution formulas|C05]]. The hand annotator's own tags here are unreliable (a definition tagged PERMISSION, another PRESCRIPTION) — a sign the four deontic tags don't fit definitional content, reinforcing the case for a CONTEXT category.

## 2. Prohibition/prescription twins everywhere
The file repeatedly states a norm twice — once as a ban, once as a positive duty: R11 *No hardcoded results* / R12 *use golden references*; R13 *make clean && make* / R14 *never skip clean*; R19 *never assume* / R20 *verify against references*. These are **support** pairs (the positive rule is how you satisfy the prohibition), not duplications.

## 3. Verification is the dominant theme
`test_registers` appears three times; 'verify against references' twice. [[elastix_gemm/Rules/R10 Run test_registers after every change or hardware op|R10]] is a textbook **checkpoint** — no new code obligation, just a mandated verify-moment against R02's robustness.

## 4. Genuine redundancy
R06 (consult the *named* references) and R26 (consult docs frequently) are the same norm at different specificity — a duplication. R16/R22 overlap on README routing.

## 5. Weakly-connected reference rules
The read-only boundary R31 and recovery-readiness R09 are near-isolated — standalone operational constraints with no supporting/ refining structure, much like the independent rules in the clinerules-tdd file.

## Counts
33 rules + 7 context. Heavily prescription-weighted (this is an operational playbook, not a values document).

Up: [[elastix_gemm/elastix_gemm MOC|elastix_gemm MOC]]
