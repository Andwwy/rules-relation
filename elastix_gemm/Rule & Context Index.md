---
tags: [index, moc]
---
# 📑 elastix_gemm — Rule & Context Index

All 33 rules + 7 context nodes.

**Legend:** 🚫 Prohibition · ✅ Prescription · 💡 Preference · 🔓 Permission · 🗒 Context

## Rules
- ✅ [[elastix_gemm/Rules/R01 Read Critical Terminology at start of every conversation|R01 Read Critical Terminology at start of every conversation]]
- ✅ [[elastix_gemm/Rules/R02 All code should be robust and validated|R02 All code should be robust and validated]]
- ✅ [[elastix_gemm/Rules/R03 MS2.0 modular design with clear boundaries|R03 MS2.0 modular design with clear boundaries]]
- ✅ [[elastix_gemm/Rules/R04 Build, test, and validate incrementally|R04 Build, test, and validate incrementally]]
- 🚫 [[elastix_gemm/Rules/R05 Never make large untested changes|R05 Never make large untested changes]]
- ✅ [[elastix_gemm/Rules/R06 Consult MULTI_ROW & AMD_GEMM references for architecture|R06 Consult MULTI_ROW & AMD_GEMM references for architecture]]
- ✅ [[elastix_gemm/Rules/R07 Adopt ready-valid, FIFO decoupling, AMD conventions|R07 Adopt ready-valid, FIFO decoupling, AMD conventions]]
- ✅ [[elastix_gemm/Rules/R08 Use build_and_flash.sh for the automated workflow|R08 Use build_and_flash.sh for the automated workflow]]
- ✅ [[elastix_gemm/Rules/R09 Keep recovery procedures ready|R09 Keep recovery procedures ready]]
- ✅ [[elastix_gemm/Rules/R10 Run test_registers after every change or hardware op|R10 Run test_registers after every change or hardware op]]
- 🚫 [[elastix_gemm/Rules/R11 No hardcoded test results|R11 No hardcoded test results]]
- ✅ [[elastix_gemm/Rules/R12 Tests must use golden references or computed values|R12 Tests must use golden references or computed values]]
- ✅ [[elastix_gemm/Rules/R13 Use make clean && make|R13 Use make clean && make]]
- 🚫 [[elastix_gemm/Rules/R14 Never skip clean|R14 Never skip clean]]
- ✅ [[elastix_gemm/Rules/R15 Run the test suite starting with test_registers|R15 Run the test suite starting with test_registers]]
- ✅ [[elastix_gemm/Rules/R16 Update README.md for technical changes|R16 Update README.md for technical changes]]
- ✅ [[elastix_gemm/Rules/R17 Update CHANGELOG.md for fixes|R17 Update CHANGELOG.md for fixes]]
- ✅ [[elastix_gemm/Rules/R18 Start with basic health checks, build complexity|R18 Start with basic health checks, build complexity]]
- 🚫 [[elastix_gemm/Rules/R19 Never assume|R19 Never assume]]
- ✅ [[elastix_gemm/Rules/R20 Always verify results against references|R20 Always verify results against references]]
- 🚫 [[elastix_gemm/Rules/R21 Update CLAUDE.md only for major shifts|R21 Update CLAUDE.md only for major shifts]]
- ✅ [[elastix_gemm/Rules/R22 Put technical details in README, not CLAUDE.md|R22 Put technical details in README, not CLAUDE.md]]
- ✅ [[elastix_gemm/Rules/R23 Keep core RTL modules modular and parameterized|R23 Keep core RTL modules modular and parameterized]]
- 🚫 [[elastix_gemm/Rules/R24 Do not use obsolete-archived modules|R24 Do not use obsolete-archived modules]]
- ✅ [[elastix_gemm/Rules/R25 Keep test suites clean — essential tests only, archive obsolete|R25 Keep test suites clean — essential tests only, archive obsolete]]
- ✅ [[elastix_gemm/Rules/R26 Consult reference documentation frequently|R26 Consult reference documentation frequently]]
- ✅ [[elastix_gemm/Rules/R27 All inter-module communication uses ready-valid|R27 All inter-module communication uses ready-valid]]
- ✅ [[elastix_gemm/Rules/R28 FIFOs between pipeline stages for flow control|R28 FIFOs between pipeline stages for flow control]]
- 🚫 [[elastix_gemm/Rules/R29 No blocking operations in the data flow|R29 No blocking operations in the data flow]]
- ✅ [[elastix_gemm/Rules/R30 Automatic partitioning across rows (V) and columns (C)|R30 Automatic partitioning across rows (V) and columns (C)]]
- 🚫 [[elastix_gemm/Rules/R31 AMD GEMM RTL is read-only — do not modify|R31 AMD GEMM RTL is read-only — do not modify]]
- ✅ [[elastix_gemm/Rules/R32 Think rigorously, test thoroughly, document clearly|R32 Think rigorously, test thoroughly, document clearly]]
- ✅ [[elastix_gemm/Rules/R33 Separate control and data paths|R33 Separate control and data paths]]

## Context
- 🗒 [[elastix_gemm/Context/C01 Native Vector (NV) — a vector of GFP numbers|C01 Native Vector (NV) — a vector of GFP numbers]]
- 🗒 [[elastix_gemm/Context/C02 Row & row_bram — per-row activation storage|C02 Row & row_bram — per-row activation storage]]
- 🗒 [[elastix_gemm/Context/C03 Dual-Memory Architecture — BRAM vs GDDR6|C03 Dual-Memory Architecture — BRAM vs GDDR6]]
- 🗒 [[elastix_gemm/Context/C04 2-D tile array & mlp_bram weight storage|C04 2-D tile array & mlp_bram weight storage]]
- 🗒 [[elastix_gemm/Context/C05 Partition distribution formulas|C05 Partition distribution formulas]]
- 🗒 [[elastix_gemm/Context/C06 Max safe back-to-back FETCH-DISPATCH = number of columns|C06 Max safe back-to-back FETCH-DISPATCH = number of columns]]
- 🗒 [[elastix_gemm/Context/C07 Buffering patterns — circular & hierarchical|C07 Buffering patterns — circular & hierarchical]]
