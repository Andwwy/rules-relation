---
tags: [rule, permission]
rule_type: PERMISSION
source: "CLAUDE.md"
source_lines: "188"
---
# 🔓 Diagnostics: docker ps, docker logs, ./status.sh, curl health checks, lsof, top, df -h,…

> Diagnostics**: `docker ps`, `docker logs`, `./status.sh`, `curl` health checks, `lsof`, `top`, `df -h`, `docker stats`

**Type:** PERMISSION  ·  **Source line:** 188

## Judgment
Allows running diagnostic commands without permission.

## Relations
- **support** → [[pickle-agent/Context/C08 You know the Pickle Jar stack inside and out. Diagnose issues, restart services,|C08 You know the Pickle Jar stack inside and out. Diagnose issues, restart services,]]
- **support** → [[pickle-agent/Rules/R38 Read files in the repo for diagnostics or reference|R38 Read files in the repo for diagnostics or reference]]
