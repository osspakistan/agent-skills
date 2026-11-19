---
name: tokenheimer
description: Reconstruct a coding project's activity across local AI coding-agent harnesses and produce a normalized analytics package plus a fixed human-friendly HTML report. Use when the user wants to measure time spent on a project, sessions, token usage, models, input/output throughput, tool calls, skill usage, file/commit/test activity, work patterns, or compare activity across Codex, Claude Code, Cursor, Pi, Gemini CLI, OpenCode, Cline, Windsurf, and other coding harnesses. Supports Quick mode for aggregate project analytics and Full mode for the same analytics plus evidence-grounded per-session summaries.
---

# Tokenheimer ☢️

**Now I am become tokens, destroyer of context.**

Reconstruct one project's development effort and coding-agent archaeology across many coding-agent harnesses. Treat harnesses as evidence sources, sessions as activity units, and the project as the thing being measured. No invented numbers, no mysterious cost estimates—just the work, the tokens, the models, and the receipts.

Use the bundled renderer. Do not redesign the report on each run.

## Choose the mode

- **Quick**: produce comprehensive project-level analytics without narrating individual sessions. Still build a normalized session ledger when session records are needed to calculate totals.
- **Full**: produce the same aggregate analytics, then add short factual per-session summaries and session-level metrics.
- If the user does not specify a mode, default to **Quick**.
- If the user does not specify a date range, use all confidently discovered history for the project and state the observed period.

## Workflow

### 1. Fingerprint the project

Identify the project name and, when available, its absolute root path, Git remote/slug, repository basename, and other distinctive workspace identifiers. Prefer strong identifiers over project-name-only matching.

### 2. Discover harness evidence

Read `references/discovery.md` and `references/agents.md` before searching local harness stores.

Use `references/agents.md` as a seed map of coding-agent namespaces and likely project/global roots. Its paths are not authoritative session-log locations. Expand `~`, inspect the relevant harness parent directories, search for the project fingerprint, then follow the filesystem/database evidence deeper.

Search read-only. Never mutate harness databases, histories, caches, configs, or source records.

### 3. Copy the evidence used

Create `sources/` and a `sources-manifest.json`. Copy or extract only the source evidence actually used for the report. Record original path, harness, copied path, observed date range, and what the source supports.

Do not package credentials, cookies, tokens, auth state, unrelated conversations, or unrelated private files. Sanitize mixed source stores when necessary and disclose the transformation in the manifest.

### 4. Normalize sessions and events

Read `references/metric-methods.md` and `references/report-schema.json`.

Normalize recoverable evidence into the schema. Preserve explicit provenance as:

- `recorded`
- `derived`
- `inferred`
- `unavailable`

Use `null` for unavailable metrics. Never convert missing evidence to zero.

Deduplicate index rows, transcript files, database rows, exports, or caches that describe the same session/activity.

### 5. Calculate project analytics

Prioritize these metric families:

- **Always pair active hours with active days** in prominent summaries: e.g. `30 active hours across 3 active days`. Do not convert 30 hours into 1.25 days; distinguish active days from calendar span. If either value is unavailable, show the known value without inventing the other. Apply to HTML, Markdown, and X posts.
- time and rhythm: active time, project span, active days, work blocks, gaps, overlap, agent runtime;
- tokens: total/input/output/reasoning/cached where recoverable;
- models: exact recorded model IDs, model mix, sessions and tokens by model;
- throughput: input/output tokens per second **only** when request-level timing or explicit throughput exists;
- tools: actual tool-call counts and tool mix;
- skills: explicit skill invocations/loads only;
- harness usage: sessions, active time, tokens, models, tools, skills by harness;
- development activity: files, commits, tests/failures, hotspots, and evidence-grounded activity classification;
- data quality: coverage for every major metric family.

Do **not** calculate or estimate monetary cost. Cost is intentionally outside this skill's contract.

### 6. Write the agent-readable report

Create `REPORT.md` as a substantial project report, not a tiny summary.

For both modes, structure it around:

1. project/period/source coverage;
2. headline metrics;
3. time and rhythm;
4. tokens and models;
5. input/output speed when supported;
6. harness usage;
7. tools and skills;
8. development activity and hotspots;
9. work patterns and notable intensity/overlap;
10. data coverage, methodology, and limitations.

In **Quick**, do not write per-session summaries.

In **Full**, add a chronological session history. Each session summary should be short, factual, and grounded in the session evidence. Include model, harness, timing, token categories, speed if available, tool/skill usage, files/commits, and tags when supported. Avoid transcript-like narration.

### 7. Write the X post (secondary deliverable)

After the analytics are complete, draft `X-POST.md` in **both Quick and Full modes** by default. The X post is a companion artifact, never the reason for collecting metrics. If the user explicitly says no X post, skip it.

Read `references/x-post.md` for the project-first storytelling contract. The **project is the subject**; Tokenheimer and its auditing process must not appear in publishable copy unless the user explicitly asks to promote Tokenheimer. Reconstruct what was built, why it matters, what changed, what was difficult, and what is next from verified project evidence. Write in the builder's natural first-person voice without inventing personal feelings or outcomes. Lead with a real project feature, milestone, challenge, or lesson—not token counts, harnesses, models, or the analytics tool. Include metrics only when they illuminate the project's story; they are optional and secondary. Provide one concise ready-to-post X post and an optional short thread, with separate non-postable receipts. Quick mode may use project-level evidence and aggregate milestones but must not manufacture per-session narratives; Full may use session-level evidence for a richer chronology. Never claim a feature shipped, works, or is public unless supported by evidence.
If evidence is too sparse to make a credible post, say so in `X-POST.md` rather than manufacturing numbers. Do not auto-publish.

### 8. Build the human report

Keep the normalized object in `report.json` and ensure it follows `references/report-schema.json`.

Use the fixed Kami-inspired visual renderer in `assets/report-template.html`. Do not invent a new dashboard or substitute a screenshot.

Build the portable files with:

```bash
python scripts/build_report.py --data /path/to/report.json --out /path/to/tokenheimer-output
```

The HTML must preserve automatic/light/dark themes and its download controls. Quick mode hides session history. Full mode renders session history with a responsive full-width metric grid; never squeeze session metrics into a narrow side rail.

### 9. Package the result

Target this shape:

```text
tokenheimer-output/
├── report.html
├── report.json
├── REPORT.md
├── sessions.csv
├── X-POST.md              # ready-to-post copy + evidence notes
├── sources-manifest.json
├── sources/
└── sources.zip              # when practical
```

`sessions.csv` may exist in both modes because the normalized session ledger is useful for audit and later analysis; Quick simply does not narrate those sessions in the report.

The X post is generated by default in both modes unless the user opts out. It remains strictly secondary to the report; never distort metrics to make the copy punchier.

## Report integrity rules

- Distinguish human active-time estimate, raw session elapsed time, and agent runtime.
- Deduplicate overlapping project activity across harnesses before summing active time.
- Never derive tokens/sec from session duration or project active time.
- Never infer skill usage from skill files merely existing on disk.
- Never force uncertain project matches into the totals.
- Prefer exact model IDs over guessed model families.
- Keep source evidence auditable through `source_refs`/manifest entries.
- Missing evidence is a finding. Report it rather than fabricating precision.
