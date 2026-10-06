# OSS Pakistan Agent Skills

A curated collection of open-source agent skills for writing, editing, summarization, and communications. Works seamlessly with Claude Code, Cursor, Codex, Windsurf, Antigravity, and other tools supporting the Agent Skills specification.

## Build & Test

• Install skill: `npx skills add osspakistan/agent-skills --skill <skill-name>`
• Install all skills: `npx skills add osspakistan/agent-skills --all`
• Interactive skill selection: `npx skills add osspakistan/agent-skills`
• List available skills: `npx skills add osspakistan/agent-skills --list`
• List Claude Code plugins: `~plugin list`
• Install Claude plugin: `~plugin install skills@skills`
• Clone and copy skills: `cp -r skills/skills/* ~/.claude/skills/`

## Project Layout

├─ **skills/** → Contains all agent skills for Claude
│  ├─ **fewwords-summarizer/** → Content summarization and briefing skill
│  ├─ **human-pencil/** → Human prose editor and AI cliché remover
│  ├─ **human-pencil-det/** → DET English Test writing practice
│  └─ **musk-email-writer/** → Urgent, first-principles memos in Musk's voice
├─ **.claude-plugin/** → Claude Code marketplace integration
│  ├─ **plugin.json** → Agent skill definitions
│  └─ **marketplace.json** → Marketplace metadata
└─ **README.md** → Installation guide and skill documentation

## Architecture Overview

A monorepo housing specialized agent skills for AI-assisted writing and communication. Each skill follows the Agent Skills specification with a unified structure: a SKILL.md file containing the agent's instructions, a README.md for human documentation, and a references/ directory with supporting files (classifier, prompts, patterns). The repository provides a centralized distribution point for skills that work across multiple AI coding agents (Claude Code, Cursor, Codex, Windsurf, etc.) through the skills.sh CLI and Claude Code plugin marketplace.

Key architectural decisions:
- Each skill is independently installable and maintainable
- Skills follow a consistent pattern for easy onboarding
- Repository serves as both source and distribution channel
- Plugin integration provides seamless AI agent access

## Development Patterns & Constraints

### Coding Style
• **Language**: JavaScript/TypeScript (skill metadata, classifier logic)
• **Formatting**: YAML frontmatter in SKILL.md, Markdown in documentation
• **Naming**: snake_case for skill names, kebab-case for directory names
• **Imports**: YAML frontmatter for skill metadata, Markdown for documentation
• **Exports**: JSON via marketplace.json, file system for skill distribution

### Component Patterns
• **Skill Structure**: SKILL.md (agent instructions) + README.md (human docs) + references/
• **File Organization**: Colocated skill definitions with supporting documentation
• **Type definitions**: YAML frontmatter in SKILL.md for skill metadata
• **Styling approach**: Markdown for documentation, YAML for configuration
• **Import patterns**: Agent Skills spec uses absolute paths (skill-name, SKILL.md)

### Error Handling
• **Flow control**: Skill instructions using Claude's function_call format
• **Fallback patterns**: Multiple fetch strategies in references/fetching.md
• **Content validation**: Classifier-based content type matching
• **Import errors**: File system path checks for skill components

### Async Patterns
• **Content acquisition**: Terminal commands (curl, fetch) for web content
• **Classifier matching**: Sequential content type identification
• **Prompt application**: Single prompt selection based on classification

### Testing Patterns
• **Manual verification**: Human documentation review and examples
• **Integration testing**: Skills tested across multiple AI agents (Claude, Cursor, etc.)
• **Quality checking**: Pattern-based reviews for AI cliché detection

## Security

• **Access control**: Skills distributed through authenticated package managers
• **Content filtering**: Classifier prevents inappropriate content processing
• **Input validation**: URL validation and fetch error handling
• **Source verification**: Skills verified through GitHub releases
• **Plugin permissions**: Claude plugin operates with user consent

## Git Workflows & Release Management

• **Branching strategy**: Standard `main` workflow with feature branches.
• **Commit conventions**: Conventional Commits (e.g., `feat:`, `fix:`, `docs:`, `chore(release):`).
• **PR requirements**: Pull requests for new skills, reference updates, or fixes.
• **Protected branches**: `main` branch holds production release state.

### Semantic Versioning Guide (`MAJOR.MINOR.PATCH`)

Current version: **`1.0.0`**. All future versions follow `1.x.x` progression:

| Digit | Scope | When to Increment | Examples |
| :--- | :--- | :--- | :--- |
| **MAJOR (`X.0.0`)** | Breaking changes | Architecture revamps, removing/deprecating skills, breaking prompt changes that change expected output interfaces. | `2.0.0` |
| **MINOR (`1.X.0`)** | New features | Adding a brand new skill (e.g. `skills/brand-writer`), adding new reference classifiers or prompt templates (fully backward-compatible). | `1.1.0`, `1.2.0` |
| **PATCH (`1.0.X`)** | Bug fixes & refinements | Prompt wording refinements in `SKILL.md`, correcting typos, updating examples in `references/`, docs fixes. | `1.0.1`, `1.0.2` |

### GitHub Actions Release & Deployment Pipeline

The repository uses [`.github/workflows/release.yml`](.github/workflows/release.yml) to automate packaging and production release deployment.

• **Workflow Trigger**: 
  - Git tag push matching `v*` (e.g. `v1.0.1`, `v1.1.0`, `v2.0.0`).
  - Manual trigger via GitHub Actions UI (`workflow_dispatch`).
• **Automated Pipeline Steps**:
  1. Checkouts codebase via `actions/checkout@v4`.
  2. Iterates over `skills/*` and packages each folder into individual `.zip` archives inside `dist/` with directory preservation for Claude.ai compatibility.
  3. Packages `all-skills.zip` containing the full skill set.
  4. Creates GitHub Release via `softprops/action-gh-release@v2`, generates changelogs, and uploads all zip assets.

### Agent Release Checklist (When publishing a version)

1. Bump `"version"` in `.claude-plugin/plugin.json` (e.g. `"1.1.0"`).
2. Verify all references and `SKILL.md` files pass `npx skills add . --list`.
3. Commit changes: `git commit -am "chore(release): bump version to 1.1.0"`
4. Tag and push: `git tag v1.1.0 && git push origin main --tags`
5. Verify GitHub Action run: `gh run list --repo osspakistan/agent-skills`

## Evidence Required for Every PR

A pull request is reviewable when it includes:

• All skill files complete: SKILL.md, README.md, references/
• Skill metadata valid in plugin.json: name, description, version
• YAML frontmatter properly formatted in SKILL.md
• Example outputs or documentation demonstrating skill behavior
• No broken links or missing references in skills/
• Skill installation instructions in README.md updated
• No unexplained dependencies in references/

## External Services

• **GitHub**: Skill distribution, releases, marketplace
• **Agent Skills spec**: Skill specification and installation via skills.sh
• **Claude Code**: Plugin marketplace integration
• **npm registries**: Skill installation via package managers

## Gotchas & Common Pitfalls

• Skills are case-sensitive: Install exact skill name (e.g., "fewwords-summarizer" not "Fewwords-summarizer")
• References must be complete: Missing classifier or fetch files breaks skill operation
• Plugin installation requires proper permissions: Ensure ~/.claude directory exists
• ZIP packaging preserves directory structure: All zip files maintain skills/* structure
• Skill metadata must be YAML-valid: Invalid frontmatter breaks agent integration
• Template accuracy matters: CLIs like skills.sh expect specific skill.json structure
• Plugin naming conflicts: Multiple plugins with same name can cause installation issues
• Fetch order is critical: skills.sh classifier requires sequential curl attempts