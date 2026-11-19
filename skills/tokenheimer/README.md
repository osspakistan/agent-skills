# Tokenheimer ☢️

> **Now I am become tokens, destroyer of context.**
> 
> Local-first coding-agent archaeology. Reconstruct the fallout: tokens, active time, models, tools, and rhythm across local AI coding harnesses into normalized analytics and a standalone HTML report.

Your agents talked. Your tools ran. Your context windows exploded. Tokenheimer reconstructs the fallout. It investigates available harness histories (Claude Code, Cursor, Codex, Pi, Gemini CLI, OpenCode, Cline, Windsurf, etc.), connects sessions to the right repository, and turns the evidence into a readable report. No invented numbers. No mysterious cost estimates. Just the work, the tokens, the models, and the receipts.

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

## Two Ways to Investigate

- **Quick (Default):** The big picture. Active development time, sessions, models, token breakdowns, input/output throughput when measured, tool calls, skill invocations, activity trends, development hotspots, and source coverage. No session-by-session narration.
- **Full:** Everything in Quick, plus a chronological, searchable session history with grounded summaries and per-session metrics. The director's cut, minus hallucinated scenes.

---

## What It Produces

```text
tokenheimer-output/
├── report.html            # The human-friendly fallout map (Kami-inspired single-file HTML)
├── report.json            # Normalized data for machines
├── REPORT.md              # Detailed agent-readable report
├── sessions.csv           # Session ledger
├── sources-manifest.json  # Evidence provenance
├── sources/               # Sanitized copies of evidence used
└── sources.zip            # Optional evidence archive
```

The HTML report uses a Kami-inspired editorial design with light, dark, and automatic themes, responsive session cards, search in Full mode, and local export controls. It is a portable single-file report, not a dashboard subscription.

---

## What Counts (and What Doesn't)

- **Recorded:** A source explicitly supplied the value.
- **Derived:** Deterministic calculation from observed evidence.
- **Inferred:** An evidence-backed estimate, clearly labeled.
- **Unavailable:** The data does not exist in logs. Zero is not a synonym for unknown.

*Token speed requires actual request-level timing. Active human time is an estimate, not raw session elapsed time. Skill usage requires invocation evidence, not just installed files on disk. Monetary cost is intentionally excluded.*

---

## Example Triggers & Usage

```text
/tokenheimer quick — analyze this repository across my local coding agents
/tokenheimer full — investigate ~/projects/my-app from October 1 to November 1
```

Or ask in natural language:
- *"Run Tokenheimer on this project to analyze our agent usage"*
- *"How many tokens, models, and hours have we spent across harnesses on this codebase?"*
- *"Generate a Tokenheimer fallout report for this repository"*

---

## Manual Report Generation

```bash
python scripts/build_report.py --data /path/to/report.json --out /path/to/tokenheimer-output
```

The report data must follow `references/report-schema.json`.

---

## Skill Contents

- [`SKILL.md`](SKILL.md) — The investigator's playbook, discovery rules, normalization, and reporting standards.
- [`scripts/build_report.py`](scripts/build_report.py) — Standalone Python renderer to produce `report.html` and `sessions.csv` from normalized `report.json`.
- [`assets/report-template.html`](assets/report-template.html) — Standalone, responsive HTML dashboard template with light/dark/auto themes.
- [`references/discovery.md`](references/discovery.md) — Guide for identifying and discovering harness evidence across local databases and logs.
- [`references/agents.md`](references/agents.md) — Seed map of coding-agent namespaces and local storage paths.
- [`references/metric-methods.md`](references/metric-methods.md) — Calculation standards for timing, tokens, and data provenance.
- [`references/report-schema.json`](references/report-schema.json) — JSON Schema for normalized report validation.
- [`references/visual-system.md`](references/visual-system.md) — Visual styling and layout specifications.

---

## License

MIT © [OSS Pakistan](https://github.com/osspakistan)
