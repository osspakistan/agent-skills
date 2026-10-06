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

## Git Workflows

• **Branching strategy**: Standard main workflow with feature branches
• **Commit conventions**: Conventional Commits for release tags
• **PR requirements**: Pull requests for new skills or improvements
• **Protected branches**: Main branch requires code review
• **Release process**: Automated ZIP packaging via GitHub Actions

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