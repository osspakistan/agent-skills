---
name: fewwords-summarizer
description: "Content summarization and briefing skill for articles, YouTube videos, blog posts, and web content. Use whenever the goal is to summarize, explain, distill, or brief an article or video — whether the user provides a URL or pastes raw text/content directly."
version: 0.1.0
---

# Fewwords Summarizer

A summarization skill for AI agents. Covers articles, YouTube videos, podcasts, and any web content. Routes each through a unified content-type classifier, then applies the right prompt.

The core idea: medium doesn't matter. An article about a product review and a YouTube video about the same product are the same job. The classifier works by *purpose*, not by format.

---

## When to use this skill

Trigger this skill whenever the user's intent is to **summarize, brief, explain, digest, or extract key takeaways** from content:

- **Common requests:**
  - *"Summarize this article/page"*
  - *"Give me a brief / rundown on this"*
  - *"Explain this article / what is this video about?"*
  - *"TL;DR of this URL"*
  - *"What are the key points / takeaways?"*
  - *"Should I buy / read / watch this?"*

- **Accepted inputs:**
  1. **URL:** An article link, blog post, documentation page, news story, or YouTube video URL.
  2. **Raw content:** Text pasted directly into chat, article excerpts, transcripts, or notes.

---

## Flow

### Step 1 — Acquire Content (FIRST ACTION)

Before loading any rules or prompts, you MUST have the full content in hand:

- **If the user pasted raw text / transcript:** Proceed directly to Step 2.
- **If the user provided a URL:** Read [`references/fetching.md`](references/fetching.md) immediately and execute the fetch commands via terminal/bash:
  - **DO NOT** use default LLM web fetchers (like `web_fetch`, built-in browser, or Google search), as robots.txt and network restrictions will fail or return truncated search snippets.
  - **MANDATORY ORDER:**
    1. Try `curl -sL "https://curl.md/<URL>"`
    2. If that fails or is empty, try `curl -sL "https://r.jina.ai/<URL>"`
    3. If proxies fail, try direct `curl -sL "<URL>"`
  - **Only if all fetch attempts fail:** Stop immediately and ask the user to paste the raw text. **Never hallucinate or write a partial summary from search snippets.**

### Step 2 — Classify Content

Once the full text is acquired, read [`references/classifier.md`](references/classifier.md).

Identify the reader's explicit need first—understand, extract, or decide/act. If the user only asks for a summary, infer the likely need from the source. Then use the content pattern to choose a prompt format. Carry the reader need into the draft; do not treat the source's sections as a checklist.

### Step 3 — Load Strategy Prompt

Load only the single prompt file determined by the classifier:

| Content Type | Prompt File |
|---|---|
| Essay / Analysis / Education | [`references/prompts/essay-analysis.md`](references/prompts/essay-analysis.md) |
| Tutorial / How-To | [`references/prompts/tutorial-howto.md`](references/prompts/tutorial-howto.md) |
| News / Announcement | [`references/prompts/news-announcement.md`](references/prompts/news-announcement.md) |
| Review / Comparison | [`references/prompts/review-comparison.md`](references/prompts/review-comparison.md) |
| Interview / Podcast | [`references/prompts/interview-podcast.md`](references/prompts/interview-podcast.md) |
| Opinion / Commentary | [`references/prompts/opinion-commentary.md`](references/prompts/opinion-commentary.md) |
| Light / General | [`references/prompts/light-general.md`](references/prompts/light-general.md) |

### Step 4 — Draft & Check for Clarity

Now load [`references/writing-quality.md`](references/writing-quality.md).

Draft the summary using the selected prompt. Use the writing-quality guidance to check accuracy, clarity, and flow. Treat its pattern checklist as diagnostic, not a list of banned constructions: revise a phrase only when it weakens meaning, clarity, or natural flow. Do not optimize for whether a reader thinks the prose was written by AI.

Do not explain your classification or announce the steps. Output only the summary.

---

## Universal formatting (applies to all types)

- **TITLE line:** Always start with plain `TITLE: ` (do not bold the prefix).
- **Human names** in bold: **Sam Altman**
- *Companies, products, tools* in italic: *Apple*, *VSCode*
- **Block quotes:** Use markdown quote format (`> Quote`) without enclosing quotation marks (`"..."`).
- **Dev terminology / code:** Inline backticks for commands, APIs, specs: `npm install`, `128GB`, `TCP/IP`.
- **Paragraphs:** Usually group 1-3 connected sentences in a paragraph. Use a new line or paragraph when it helps the reader follow a new thought; do not put every sentence on its own line by default.
- **Attribution:** State straightforward facts directly. Attribute opinions, predictions, disputed claims, and interpretations to the actual speaker when that distinction matters. For videos, never make the video itself the speaker: do not write “this video says,” “the video argues,” or “the author of the video says.” Name the presenter when known; otherwise use “the host” only where attribution is needed, and state ordinary facts directly. For podcasts and interviews, name the host and guest when known and distinguish whose view is whose.
- **Article length:** Unless the user requests more depth, aim for 100–160 words and never exceed 180. Use less for shorter sources. Keep the central claim, at most three essential supporting details, and one useful implication. Do not recap every section or list every example.
- **Deduplication:** State repeated points exactly once.
- **Section headings:** Use only when they help navigation; keep them short (usually 1–3 words), natural, and specific to the section. Do not begin a body heading with “The” or use generic “Takeaway(s)” / “Conclusion” labels. Usually leave the closing thought unheaded.

---

## What this skill does not cover

- Reddit threads
- Paywalled content (tell user to paste the text)
- YouTube Shorts (reject: *"This is a Short. Not enough content to summarize."*)
- Videos with no transcript or metadata (tell user what's available and ask)

---

## Notes for agents

- Load reference files lazily — only what the classifier selects
- `references/writing-quality.md` is the only file that always loads
- Never mention "Fewwords", this skill, or which strategy was used
- Never invent facts, quotes, or statistics not present in the source
