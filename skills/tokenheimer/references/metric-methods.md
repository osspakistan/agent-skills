# Tokenheimer metric methods

Use this reference when normalizing evidence or deciding whether a metric can be reported.

## Hours + days display rule

Display active work time together with the number of distinct active calendar days: **“30 active hours across 3 active days.”** These are separate measurements, not a conversion. Active days means dates with qualifying project activity in the chosen timezone, not the number of 24-hour periods or elapsed project span. Preserve precision and provenance. If only one value is supported, show it alone and mark the other unavailable.

## Evidence states

- **recorded**: the harness/source directly records the value.
- **derived**: deterministic calculation from recorded values.
- **inferred**: evidence-supported classification or estimate. State the rule used.
- **unavailable**: insufficient evidence. Use `null`; never invent a substitute.

Coverage is the fraction of relevant observed sessions/records that can support the metric. Do not turn missing records into zeroes.

## Time

Keep these separate:

- **session elapsed time**: recorded or derived start-to-end duration for one session.
- **agent runtime**: runtime recorded by the harness/model/tool when available.
- **active time**: an estimate from timestamped project activity, deduplicated across overlapping harnesses.
- **project span**: first observed project activity to last observed project activity.

For active time, prefer event-level timestamps. Build activity intervals using the source's own activity timing when available. Otherwise, sort timestamped events and cap the contribution of long silent gaps rather than counting the whole gap as work. State the inactivity rule in `quality.method_note`. Merge overlapping intervals across harnesses before summing project active time. Never sum raw session durations across concurrent sessions.

## Tokens

Preserve raw token categories when provided: input, output, reasoning, cached. Avoid double-counting cumulative snapshots. When a harness stores cumulative counters, use deltas only when the counter semantics are clear. If only a total is trustworthy, report the total and leave categories null.

## Models

Preserve the exact recorded model identifier. You may add a normalized display name, but never replace the raw identity in source evidence. Count a model only when it appears in project-relevant evidence.

## Input/output speed

Report speed only when timing exists at the request/generation level or the harness explicitly records throughput.

- `input_tokens_per_second`: input/prefill tokens divided by an explicit input-processing duration, or a directly recorded throughput value.
- `output_tokens_per_second`: output tokens divided by an explicit model-generation duration, or a directly recorded throughput value.

Do **not** divide tokens by session duration, wall-clock project time, active time, or agent runtime to fabricate throughput. If request timing is absent, speed is unavailable.

For aggregate/model speed, use a token-weighted aggregate when request-level durations are available. Record coverage because speed will often exist for only a subset of sessions.

## Tools

Count actual tool-call events. Normalize obvious aliases only when their equivalence is clear; retain enough source information to audit the mapping. Useful categories include shell/terminal, file read/write/edit, search/grep, web, browser, test/build, git, MCP/plugin/connector, and subagent calls. Prefer exact tool names in the normalized ledger and optionally group them for the visual report.

## Skills

Count a skill only when the record shows an explicit skill invocation, skill path/load, or equivalent trace. Do not infer skill usage merely because a skill exists on disk or because the session topic resembles a skill.

## Development activity

Files, commits, tests, failures, and hotspots must be grounded in session traces, repository history, or both. Distinguish a file mentioned in conversation from a file actually touched when the source allows that distinction.

`activity_mix` is normally inferred. Classify only the evidence that can reasonably be categorized and disclose the classification method. Keep an `Other`/`Unclassified` bucket rather than forcing every event into a category.

## No cost metric

Tokenheimer intentionally does not require or estimate monetary cost. Pricing is model/provider/account dependent, may be unavailable, and changes over time. Do not add cost to the core schema, session cards, tables, or headline metrics.
