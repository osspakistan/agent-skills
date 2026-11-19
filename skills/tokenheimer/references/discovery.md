# Project Grind evidence discovery

Use this reference when locating coding-agent/harness records for a project.

## Principle

Treat `references/agents.md` as a **seed map**, not a database of session-log locations. Its project/global skill paths reveal common harness namespaces and home/config roots. Start there, then inspect the actual filesystem and let evidence determine where the harness stores histories, transcripts, databases, caches, and project metadata.

## Establish project identity first

Build a project fingerprint before searching:

1. project display name;
2. absolute project/repository path when available;
3. repository directory basename;
4. Git remote URL(s) and owner/repo slug when available;
5. distinctive workspace/package names if useful.

Prefer exact path, cwd, repository root, or remote matches over a plain project-name match. Names such as `app`, `api`, or `web` are too ambiguous by themselves.

## Seed harness locations

Read `references/agents.md`. Expand `~` to the current home directory. For each plausible installed harness, use the listed project/global paths to identify its namespace. Examples include roots such as `~/.claude`, `~/.cursor`, `~/.gemini`, `~/.agents`, `~/.config/opencode`, `~/.codeium`, and similar harness-specific directories.

The listed paths are for skills, not necessarily session history. Search the relevant parent namespace and nearby harness data/config roots rather than assuming logs live under `/skills/`.

## Search progressively

Within each relevant harness namespace:

1. inspect top-level names and metadata;
2. search textual files for exact project root, cwd, Git remote, repo slug, then project name;
3. inspect likely history/session/transcript/conversation/project/workspace/cache/state directories;
4. inspect structured stores such as JSON, JSONL, SQLite, msgpack or other databases when present;
5. use timestamps and session IDs to connect related records;
6. follow references deeper when a record points to another file or database.

Prefer targeted searches inside harness roots. Do not recursively scan the entire home directory unless targeted discovery fails and the user has authorized broad local inspection.

Useful search terms include the exact project path, escaped path variants, repo slug, remote URL, cwd, `project`, `workspace`, `session`, `conversation`, `history`, `transcript`, and the project name.

## Database handling

Treat source stores as read-only. For SQLite or similar databases, inspect schema/table names first, then query narrowly. Never migrate, vacuum, rewrite, or otherwise mutate a source database.

## Select project-relevant sessions

A session belongs to the project when strong evidence connects it to the project fingerprint. Rank evidence roughly as:

1. exact cwd/project-root/repository path;
2. exact Git remote or repo identifier;
3. explicit harness project/workspace mapping;
4. repeated distinctive file paths from the project;
5. project name alone.

When only weak name evidence exists, mark the match uncertain or exclude it rather than contaminating totals.

## Deduplicate

Harnesses may keep indexes, exported copies, databases, and per-session files for the same activity. Deduplicate using stable session IDs first; otherwise combine timestamps, harness, cwd/repo identity, message/tool fingerprints, and source relationships. Never count an index row and its backing transcript as two sessions.

## Preserve evidence safely

Copy only source files/rows/artifacts actually used to support the report. Keep originals untouched. Build a source manifest recording harness, original location, copied location, time range, and what metrics it supports.

Do not package credentials, API keys, auth tokens, cookies, unrelated conversations, or other secrets. If a source file mixes project evidence with sensitive unrelated content, extract the minimum relevant evidence into a sanitized copy and record that transformation in the manifest.
