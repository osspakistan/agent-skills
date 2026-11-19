# Tokenheimer

> Reconstruct a coding project's development effort and token activity across local AI coding-agent harnesses into normalized analytics and an interactive HTML report.

`tokenheimer` reconstructs one project's full development history by parsing and normalizing evidence across local agent stores (Claude Code, Cursor, Codex, Pi, Gemini CLI, OpenCode, Cline, Windsurf, etc.). It calculates aggregate development metrics (active time, token consumption, models used, tool calls, file/commit churn) and compiles them into a portable, standalone HTML report with a CSV session ledger.

---

## Quick Install

Install just this skill using [`skills.sh`](https://skills.sh):

```bash
# Project-level
npx skills add osspakistan/agent-skills --skill tokenheimer

# Or globally across all your coding agents
npx skills add osspakistan/agent-skills --skill tokenheimer -g
```

---

## What It Measures

1. **Time & Rhythm:** Active development time, calendar span, active days, work sessions, gaps, and concurrency.
2. **Tokens & Throughput:** Input, output, reasoning, and cached token totals; input/output tokens per second when request timing exists.
3. **Models & Mix:** Exact recorded model identifiers, model distribution, and tokens consumed per model.
4. **Tools & Skills:** Quantitative breakdown of tool executions and explicit skill invocations.
5. **Cross-Harness Comparison:** Normalized activity across Claude Code, Cursor, Codex, Pi, Cline, Windsurf, etc.
6. **Code Churn:** Files touched, git commits, test executions/failures, and editing hotspots.

*(Note: Monetary cost is intentionally excluded from the data contract, as API pricing varies by account, tier, and changes over time.)*

---

## Modes

- **Quick (Default):** Generates high-level project analytics, KPI summary cards, time distribution, model/tool breakdowns, and data quality metrics without detailing individual chat transcripts.
- **Full:** All Quick mode analytics plus chronological, evidence-grounded session summaries and full session metrics.

---

## Example Triggers

- *"Run Tokenheimer on this project to analyze our agent usage"*
- *"How many tokens, models, and hours have we spent across harnesses on this codebase?"*
- *"Generate a Tokenheimer report for this repository"*
- *"Analyze coding-agent activity in full mode"*

---

## Skill Contents

- [`SKILL.md`](SKILL.md) — Workflow, discovery rules, normalization, metric methods, and reporting standards.
- [`scripts/build_report.py`](scripts/build_report.py) — Standalone Python renderer to produce `report.html` and `sessions.csv` from normalized `report.json`.
- [`assets/report-template.html`](assets/report-template.html) — Standalone, responsive HTML dashboard template with light/dark/auto themes.
- [`references/discovery.md`](references/discovery.md) — Guide for identifying and discovering harness evidence across local databases and logs.
- [`references/agents.md`](references/agents.md) — Directory map of known local coding agent storage paths and formats.
- [`references/metric-methods.md`](references/metric-methods.md) — Rigorous calculation standards for timing, tokens, and data provenance.
- [`references/report-schema.json`](references/report-schema.json) — JSON Schema for normalized report validation.
- [`references/visual-system.md`](references/visual-system.md) — Visual styling and layout specifications.

---

## License

MIT © [OSS Pakistan](https://github.com/osspakistan)
