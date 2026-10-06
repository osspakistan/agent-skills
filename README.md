# OSS Pakistan Skills

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/osspakistan/agent-skills?style=flat)](https://github.com/osspakistan/agent-skills/stargazers)

Open-source agent skills for writing, editing, summarization, and communications, maintained by **[OSS Pakistan](https://github.com/osspakistan)**.

Works seamlessly with **Claude Code**, **Cursor**, **Codex**, **Windsurf**, **Antigravity**, and any tool supporting the [Agent Skills specification](https://skills.sh).

---

## Quick Start: Installation

Choose the installation method that fits your workflow:

### 1. Using `skills.sh` CLI (Recommended)

Works with `npx`, `bunx`, or `pnpx` across all supported coding agents (Claude Code, Cursor, Windsurf, Antigravity, etc.).

* **Interactive picker (manually choose skills from a list):**
  ```bash
  # Run without flags to interactively select which skills you want:
  npx skills add osspakistan/agent-skills

  # Or using bunx / pnpx:
  bunx skills add osspakistan/agent-skills
  pnpx skills add osspakistan/agent-skills
  ```

* **Install ALL skills at once:**
  ```bash
  # Project-level
  npx skills add osspakistan/agent-skills --all

  # Global (across all your projects and coding agents)
  npx skills add osspakistan/agent-skills --all -g
  ```

* **Install an INDIVIDUAL skill directly:**
  ```bash
  # Example: Install only fewwords-summarizer
  npx skills add osspakistan/agent-skills --skill fewwords-summarizer

  # Example: Install only human-pencil
  npx skills add osspakistan/agent-skills --skill human-pencil
  ```

* **List available skills before installing:**
  ```bash
  npx skills add osspakistan/agent-skills --list
  ```

---

### 2. Using Claude Code Plugin Marketplace

Inside the Claude Code CLI interface:

1. Add the marketplace:
   ```bash
   /plugin marketplace add osspakistan/agent-skills
   ```
2. Install the skill pack:
   ```bash
   /plugin install skills@skills
   ```

---

### 3. Direct Copy / Git Clone

If you prefer managing skills directly in your repository or user directory:

```bash
# Clone the repository
git clone https://github.com/osspakistan/agent-skills.git

# Install ALL skills to Claude Code:
cp -r skills/skills/* ~/.claude/skills/

# Or copy a SINGLE skill:
cp -r skills/skills/fewwords-summarizer ~/.claude/skills/
```

---

### 4. Claude.ai (Web / Desktop App)

1. Download the ZIP file for the skill from our [Releases](https://github.com/osspakistan/agent-skills/releases).
2. Go to **Customize → Skills → Create skill → Upload a skill**.
3. Select the `.zip` file and enable it.

---

## Available Skills

### 1. [fewwords-summarizer](skills/fewwords-summarizer/README.md)
High-signal, purpose-driven briefs for articles, YouTube videos, and podcasts.
- **When to reach for it:** When you want key takeaways, a quick TL;DR, or an intent-driven briefing.
- **Install:** `npx skills add osspakistan/agent-skills --skill fewwords-summarizer`

### 2. [human-pencil](skills/human-pencil/README.md)
Light-hand human prose editor and AI cliché remover.
- **When to reach for it:** When editing drafts to remove repetitive AI patterns and restore authentic human voice.
- **Install:** `npx skills add osspakistan/agent-skills --skill human-pencil`

### 3. [human-pencil-det](skills/human-pencil-det/README.md)
Duolingo English Test writing practice with a contextual vocabulary bank.
- **When to reach for it:** When practicing writing for DET or elevating vocabulary naturally without robotic stuffing.
- **Install:** `npx skills add osspakistan/agent-skills --skill human-pencil-det`

### 4. [musk-email-writer](skills/musk-email-writer/README.md)
Urgent, first-principles memos in the documented voice of Elon Musk.
- **When to reach for it:** When you need blunt, urgent, numbers-driven business memos or replies.
- **Install:** `npx skills add osspakistan/agent-skills --skill musk-email-writer`

---

## Repository Structure

```
agent-skills/
├── .gitignore                     # Ignores local experiment folders (.wtf/)
├── LICENSE                        # MIT License
├── README.md                      # Main directory & install guide
├── .claude-plugin/
│   ├── marketplace.json           # Claude Code marketplace definition
│   └── plugin.json                # Plugin manifest
└── skills/                        # Production skills directory
    ├── fewwords-summarizer/
    │   ├── SKILL.md               # Agent instructions
    │   ├── README.md              # Human documentation
    │   └── references/            # Intent classifier, fetch rules & prompts
    ├── human-pencil/
    │   ├── SKILL.md
    │   ├── README.md
    │   └── references/
    ├── human-pencil-det/
    │   ├── SKILL.md
    │   ├── README.md
    │   └── references/
    └── musk-email-writer/
        ├── SKILL.md
        ├── README.md
        └── references/
```

## Release & Version Management

This repository uses **Semantic Versioning** (`MAJOR.MINOR.PATCH`).

The current release is **`v1.0.0`**. Version progression follows `1.x.x`:

| Segment | Format | Meaning | When to Use | Examples |
| :--- | :--- | :--- | :--- | :--- |
| **MAJOR** | `X.0.0` | Breaking changes | Incompatible skill workflow changes, removing or deprecating existing skills, major breaking renames. | `2.0.0` |
| **MINOR** | `1.X.0` | New features (backwards-compatible) | Adding a brand new skill (e.g. `skills/brand-writer`), adding new reference modules, adding major templates. | `1.1.0`, `1.2.0` |
| **PATCH** | `1.0.X` | Bug fixes & refinements | Fixing typos, refining prompts in `SKILL.md`, updating references or examples, doc improvements. | `1.0.1`, `1.0.2` |

### When to use `git push` vs `git tag`

| Command | Purpose | When to Use | Triggers GitHub Release? |
| :--- | :--- | :--- | :--- |
| **`git push origin main`** | Code Sync | Daily development, pushing drafts, updates, or fixes to the `main` branch. | **No** (only updates the git tree). |
| **`git tag v1.x.x`**<br>`git push origin --tags` | Production Release | Only when bumping versions (e.g. `v1.0.1`, `v1.1.0`) to publish an official release. | **Yes** (triggers CI build & ZIP publishing). |

- **First-time setup only:** Use `git push -u origin main` once to link your local branch to the remote upstream tracking branch.
- **Regular daily development:** Just use `git commit` followed by `git push`.
- **Ready to ship a new version:** Create an annotated or lightweight tag with `git tag v1.x.x` and push it with `git push origin --tags`.

### Automated GitHub Actions Release Pipeline

Releases and Claude.ai ZIP packages are automatically generated and deployed using GitHub Actions ([`.github/workflows/release.yml`](.github/workflows/release.yml)).

**How to publish a new release:**

1. **Update version in manifests:**
   - Bump `"version"` in `.claude-plugin/plugin.json` (e.g. `"1.1.0"`).
2. **Commit and tag:**
   ```bash
   git commit -am "chore(release): bump version to 1.1.0"
   git tag v1.1.0
   git push origin main --tags
   ```
3. **Automated Deployment:**
   - GitHub Actions automatically triggers on `v*` tags.
   - Packages every skill into an individual `.zip` with the correct root directory layout for Claude.ai.
   - Builds an `all-skills.zip` archive containing the entire collection.
   - Publishes a new GitHub Release with auto-generated release notes and downloadable assets.

---

## Contributing

We welcome new skills and improvements from the community!

1. Fork the repo and create your branch.
2. Add your skill into `skills/<your-skill-name>/`:
   - Include a valid [`SKILL.md`](https://skills.sh) with `name` and `description` YAML frontmatter.
   - Include a clear [`README.md`](skills/fewwords-summarizer/README.md) explaining the skill for humans.
3. Add the skill to `.claude-plugin/plugin.json` and the root list.
4. Submit a Pull Request.

---

## License

[MIT](LICENSE) © [OSS Pakistan](https://github.com/osspakistan)
