# OSS Pakistan Agent Skills

A collection of open-source agent skills for writing, editing, summarization, and business communications. Works seamlessly with Claude Code, Cursor, Codex, Windsurf, Antigravity, and any environment supporting the [Agent Skills specification](https://skills.sh).

---

## Quick Commands & Verification

- **Interactive skill selection:** `npx skills add osspakistan/agent-skills` (or `bunx` / `pnpx`)
- **Install all skills:** `npx skills add osspakistan/agent-skills --all`
- **Install individual skill:** `npx skills add osspakistan/agent-skills --skill <skill-name>`
- **Validate repository skills:** `npx skills add . --list`
- **Claude Code plugin marketplace:**
  - Add marketplace: `/plugin marketplace add osspakistan/agent-skills`
  - Install plugin: `/plugin install skills@skills`

---

## Project Structure

```
agent-skills/
├── .github/workflows/
│   └── release.yml            # CI workflow for auto-packaging releases
├── .claude-plugin/
│   ├── marketplace.json       # Claude Code marketplace configuration
│   └── plugin.json            # Plugin manifest listing available skills
├── skills/                    # Production skills directory
│   ├── fewwords-summarizer/   # Content summarization and briefing
│   ├── human-pencil/          # Natural prose editor & AI cliché remover
│   ├── human-pencil-det/      # DET writing practice & vocabulary bank
│   └── musk-email-writer/     # Urgent, first-principles executive memos
├── LICENSE                    # MIT License
├── README.md                  # Human-facing documentation & install guides
└── AGENTS.md                  # Agent operating instructions & repository rules
```

---

## Skill Architecture

Every skill follows the standard Agent Skills specification:

1. **`SKILL.md` (Agent Instructions):**
   - Must begin with valid YAML frontmatter containing `name` and `description`.
   - The `description` is critical: AI agents use it for intent detection and automatic activation.
   - Body contains actionable workflows, voice principles, and execution steps.
2. **`README.md` (Human Documentation):**
   - Rendered on GitHub when browsing the skill folder.
   - Contains: what the skill does, quick install commands, example prompts, and license.
3. **`references/` (Optional Context & Modules):**
   - Supplementary markdown files (e.g. classification trees, prompt templates, word banks).
   - Referenced by relative links from `SKILL.md`.

---

## Git Workflows & Release Management

### When to use `git push` vs `git tag`

| Action | Command | Purpose | When to Use | Triggers CI Release? |
| :--- | :--- | :--- | :--- | :--- |
| **Initial Upstream Link** | `git push -u origin main` | Sets upstream tracking for branch | Run once on repository creation or when pushing a newly created branch. | **No** |
| **Routine Code Sync** | `git push origin main` | Pushes daily commits and work | Use constantly during routine skill writing, testing, editing prompts, and docs. | **No** |
| **Official Version Release** | `git tag v1.x.x`<br>`git push origin --tags` | Creates immutable version checkpoint | Only when ready to publish an official release (`v1.0.1`, `v1.1.0`, etc.). | **Yes** (Builds ZIPs & publishes GitHub Release) |

### Semantic Versioning Guide (`MAJOR.MINOR.PATCH`)

Current version: **`1.0.0`**. All future versions follow `1.x.x` progression:

| Digit | Scope | When to Increment | Examples |
| :--- | :--- | :--- | :--- |
| **MAJOR (`X.0.0`)** | Breaking changes | Architecture revamps, removing/deprecating skills, breaking output interfaces. | `2.0.0` |
| **MINOR (`1.X.0`)** | New features | Adding a brand new skill (e.g. `skills/brand-writer`), adding new reference classifiers or prompt templates (fully backward-compatible). | `1.1.0`, `1.2.0` |
| **PATCH (`1.0.X`)** | Bug fixes & refinements | Prompt wording refinements in `SKILL.md`, correcting typos, updating examples in `references/`, docs fixes. | `1.0.1`, `1.0.2` |

### GitHub Actions Release & Deployment Pipeline

Automated by [`.github/workflows/release.yml`](.github/workflows/release.yml):
1. **Trigger:** Push of any git tag matching `v*` (e.g. `v1.0.1`, `v1.1.0`), or manual workflow dispatch.
2. **Build:** Packages each skill folder into individual `.zip` files (with the root folder preserved for Claude.ai), plus `all-skills.zip`.
3. **Publish:** Creates GitHub Release, generates changelogs, and uploads the downloadable ZIP assets.

### Agent Release Checklist (When publishing a version)

1. Bump `"version"` in `.claude-plugin/plugin.json` (e.g. `"1.1.0"`).
2. Validate local skills: `npx skills add . --list`.
3. Commit changes: `git commit -am "chore(release): bump version to 1.1.0"`
4. Tag and push: `git tag v1.1.0 && git push origin main --tags`
5. Verify GitHub Action status: `gh run list --repo osspakistan/agent-skills`

---

## PR Review & Contribution Checklist

A pull request is ready to merge when:
- [ ] Every new skill has its own folder under `skills/<skill-name>/`.
- [ ] `SKILL.md` exists with valid YAML frontmatter (`name` matching the folder name exactly).
- [ ] A human-friendly `README.md` is provided in the skill folder.
- [ ] All relative links to `references/` are valid and tested.
- [ ] Skill is added to `.claude-plugin/plugin.json` and the root `README.md` list.
- [ ] `npx skills add . --list` discovers the skill without errors.

---

## Gotchas & Common Pitfalls

- **Directory name matches frontmatter:** `skills/<name>` directory name must be identical to the `name:` field in `SKILL.md`.
- **Do not commit `dist/`:** ZIP archives are generated on the fly by CI and should remain gitignored.
- **Root folder in ZIPs:** Claude.ai requires the ZIP file to contain `<skill-name>/SKILL.md` (not `SKILL.md` at zip root).
- **No external code runtime needed:** Skills are declarative prompt and reference files—do not add npm build scripts or compiler steps unless an explicit helper CLI script is needed.