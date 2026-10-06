# Classifier

Before generating any summary, read enough of the content to classify it. Medium is irrelevant — it's all text in the end.

---

## Step 1: Read the Content

For URLs: fetch using [`references/fetching.md`](fetching.md) (via `curl.md`, `r.jina.ai`, or direct `curl`), then skim the intro, subheadings, and conclusion (or video title, description, transcript).

For pasted text: read the opening paragraph and any visible structure.

---

## Step 2: Pick a Type

Match the **primary purpose** of the content — not the medium (article vs. video).

| Type | What it's doing | Load |
|---|---|---|
| **Essay / Analysis** | Making an argument, explaining a concept, academic writing, long-form research, educational explainer | `references/prompts/essay-analysis.md` |
| **Tutorial / How-To** | Teaching someone to do something, step-by-step, follow-along, build-along | `references/prompts/tutorial-howto.md` |
| **News / Announcement** | Reporting what happened, product launches, press releases, current events | `references/prompts/news-announcement.md` |
| **Review / Comparison** | Evaluating a product or tool, should you buy, hands-on test, "best X" with opinions | `references/prompts/review-comparison.md` |
| **Interview / Podcast** | Conversation with a guest, Q&A, long-form dialogue, profile piece built around quotes | `references/prompts/interview-podcast.md` |
| **Opinion / Commentary** | Personal argument, hot take, reaction, creator's position on something | `references/prompts/opinion-commentary.md` |
| **Light / General** | Entertainment, casual content, lifestyle, no clear thesis, doesn't fit above | `references/prompts/light-general.md` |

---

## Step 3: When It's Ambiguous

**Mixed content** — pick the dominant purpose. A tutorial article with strong opinion = Tutorial. A news article with deep analysis = Essay/Analysis.

**Defaults:**
- Can't tell → **Essay / Analysis**
- Video that clearly entertains more than informs → **Light / General**

---

## Step 4: Special Cases

**YouTube Shorts** — reject immediately: *"This is a Short. Not enough content to summarize."*

**Paywalled content** — tell the user: *"This content is paywalled. Paste the text and I'll summarize it."*

**No transcript available** — tell the user what metadata you can work with and ask if they want a metadata-only summary.

**Reddit threads** — out of scope for this skill.

---

## Step 5: Load and Apply

1. Load the prompt from the file matched above
2. The prompt handles the rest — follow it fully
