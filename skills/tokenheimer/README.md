# Tokenheimer ☢️

**Now I am become tokens, destroyer of context.**

Your agents talked. Your tools ran. Your context windows exploded. Tokenheimer reconstructs the fallout.

Tokenheimer is a local-first coding-agent archaeology skill. Point it at a project and it investigates available harness histories, connects sessions to the right repository, and turns the evidence into a readable report. No invented numbers. No mysterious cost estimates. Just the work, the tokens, the models, and the receipts.

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

## Time that actually means something

Tokenheimer reports **30 active hours across 3 active days**, rather than just “3 days” or “30 hours.” Hours describe the measured effort; active days describe when that effort happened. Elapsed calendar span is a separate number. This phrasing carries into the HTML report, Markdown summary, and X post when supported.

---

## Two ways to investigate

**Quick** — The big picture. Active time, sessions, models, token breakdowns, input/output throughput when measured, tool calls, skill invocations, activity trends, development hotspots, and source coverage. No session-by-session narration. Includes a ready-to-post X draft.

**Full** — Everything in Quick, plus a chronological, searchable session history with grounded summaries and per-session metrics. It's the director's cut, minus the hallucinated scenes. Includes the same X-post deliverable.

---

## What it produces

```text
tokenheimer-output/
├── report.html            # The human-friendly fallout map
├── report.json            # Normalized data for machines
├── REPORT.md              # Detailed agent-readable report
├── sessions.csv           # Session ledger
├── X-POST.md             # A post worth publishing, with receipts
├── sources-manifest.json  # Evidence provenance
├── sources/               # Sanitized copies of evidence used
└── sources.zip            # Optional evidence archive
```

The HTML uses a Kami-inspired editorial design with light, dark, and automatic themes, responsive session cards, search in Full mode, and export controls. It is a portable single-file report, not a dashboard subscription.

---

## How to use

Install the `tokenheimer/` folder in your coding agent's skills directory, then ask:

```text
/tokenheimer quick — analyze this repository across my local coding agents
/tokenheimer full — investigate ~/projects/my-app from October 1 to November 1
```

Your agent must have read access to the relevant local harness histories. Tokenheimer uses `references/agents.md` as a **starting map**, not as a fictional catalog of session-log paths. It searches harness-specific directories, fingerprints the project by path/name/remote, and follows the actual evidence.

---

## The X post: tell the project's story

The report is about metrics. The X post is about **the thing you actually built**. Tokenheimer reads project evidence to draft a natural builder update: what the project does, what changed, the hardest decision, a meaningful milestone, or what comes next. It is **not** an ad for Tokenheimer, a harness audit, or a token-count flex. Numbers can support the story, but they never replace it.

Both modes write `X-POST.md` by default. Quick uses confirmed project-level milestones; Full can draw on the deeper session chronology. Nothing gets published automatically. Say **no X post** to opt out.

---

## What counts (and what doesn't)

- **Recorded** means a source explicitly supplied the value.
- **Derived** means deterministic math from observed evidence.
- **Inferred** means an evidence-backed estimate, clearly labeled.
- **Unavailable** means unavailable. Zero is not a synonym for unknown.

Token speed requires actual request-level timing. Active human time is an estimate, not session elapsed time. Skill usage requires invocation evidence, not just installed skill folders. Monetary cost is deliberately excluded.

---

## Build a report manually

```bash
python scripts/build_report.py --data /path/to/report.json --out /path/to/tokenheimer-output
```

The report data must follow `references/report-schema.json`. The builder rejects monetary cost fields.

---

## Under the hood

`SKILL.md` is the investigator's playbook; `references/` contains discovery, metric methodology, schema, and design guidance; `assets/report-template.html` is the fixed renderer; and `scripts/build_report.py` packages the result. The agent hunts for evidence. The template does the looking good.

---

## License

MIT © [OSS Pakistan](https://github.com/osspakistan)
