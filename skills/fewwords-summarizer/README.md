# Fewwords Summarizer

> High-signal, purpose-driven summarization for articles, YouTube videos, podcasts, and web content.

`fewwords-summarizer` is an agent skill that cuts through bloated web content and delivers clear, structured briefs. Instead of naive bullet lists, it classifies the **underlying intent** of the material (product review, technical tutorial, news, interview, deep-dive essay) and applies a specialized briefing framework.

---

## Quick Install

Install just this skill using [`skills.sh`](https://skills.sh):

```bash
# Project-level
npx skills add osspakistan/agent-skills --skill fewwords-summarizer

# Or globally across all your coding agents
npx skills add osspakistan/agent-skills --skill fewwords-summarizer -g
```

---

## How It Works

1. **Acquires Content:** Automatically grabs transcripts from YouTube or extracts readable text from articles using CLI tooling (`yt-dlp`, markdown fetchers).
2. **Intent Classification:** Routes the content into one of 7 categories:
   - **Review / Comparison:** Buying verdict, trade-offs, and target audience.
   - **Tutorial / How-To:** Prerequisites, sequence of steps, and failure modes.
   - **News / Announcement:** What happened, why it matters, and who is affected.
   - **Interview / Podcast:** Guest background, core thesis, key quotes, and highlights.
   - **Essay / Analysis:** Core argument, evidence presented, and counterarguments.
   - **Opinion / Commentary:** Author's stance, reasoning, and context.
   - **Light / General:** Fast TL;DR and core takeaways.
3. **High-Signal Output:** Delivers a zero-fluff summary matching the reader's intent.

---

## Example Triggers

You can trigger this skill in your AI agent with prompts like:

- *"Summarize this article: https://example.com/post"*
- *"Give me a brief and the key takeaways of this YouTube video: https://youtube.com/watch?v=..."*
- *"TL;DR on this draft — should I read this?"*
- *"Extract the main lessons and action items from this podcast transcript"*

---

## Skill Contents

- [`SKILL.md`](SKILL.md) — Main prompt workflow and intent router.
- [`references/fetching.md`](references/fetching.md) — Fast terminal-based content extraction instructions.
- [`references/classifier.md`](references/classifier.md) — Intent classification decision trees.
- [`references/prompts/`](references/prompts/) — 7 intent-specific briefing prompt templates.
- [`references/writing-quality.md`](references/writing-quality.md) — Anti-fluff writing guidelines.

---

## License

MIT © [OSS Pakistan](https://github.com/osspakistan)
