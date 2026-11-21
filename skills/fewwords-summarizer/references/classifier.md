# Classifier

Classify the reader's need before choosing a summary format. Medium (article, video, podcast) does not determine the need.

---

## Step 1: Read the request and source

For URLs, fetch the full content using [`references/fetching.md`](fetching.md). Read enough to identify the user's goal and the source's main purpose. Do not infer a more detailed request than the user made.

---

## Step 2: Identify the reader's primary need

If the user states a goal, follow it. Otherwise infer one primary need from the content and the likely reason someone would read it:

| Reader need | The reader wants to… | Prioritize |
|---|---|---|
| **Understand** | Learn an idea, argument, cause, or context | The central claim and the reasoning that supports it; include only context needed to follow the argument. |
| **Extract** | Get useful facts, specifications, prices, or steps without the backstory | The exact details needed for lookup, comparison, or execution; remove anecdotes, repeated points, and SEO filler. |
| **Decide / act** | Choose, respond, or know whether something matters now | The verdict or change, the most important trade-offs or consequences, and any supported next step. |

A request such as “just the numbers” selects **Extract**, even if the source is an essay. “Should I buy this?” selects **Decide / act**, even if the source is a review video. A generic “summarize this” uses the source's primary purpose to infer the need.

---

## Step 3: Choose the content format

Use the reader need to decide what information belongs; use the source pattern to choose the prompt format. Do not let a format's headings become a checklist of everything to include.

| Source pattern | Usual reader need | Load |
|---|---|---|
| Essay, research, explanation, or deep analysis | **Understand** | `references/prompts/essay-analysis.md` |
| How-to, tutorial, or build guide | **Extract** the steps needed to do it | `references/prompts/tutorial-howto.md` |
| News, launch, or time-sensitive update | **Decide / act** on what changed and why it matters | `references/prompts/news-announcement.md` |
| Product review, buying guide, or comparison | **Decide / act** | `references/prompts/review-comparison.md` |
| Interview, podcast, or conversation | **Understand** the speakers' distinct views | `references/prompts/interview-podcast.md` |
| Opinion or commentary | **Understand** the argument and how well it is supported | `references/prompts/opinion-commentary.md` |
| Entertainment or general-interest piece | **Understand** the gist and whether it is worth the reader's time | `references/prompts/light-general.md` |

When the explicit request conflicts with the usual need in the table, keep the source-appropriate format but follow the user's requested need when selecting facts and emphasis.

---

## Step 4: Resolve ambiguity

- A tutorial with a strong opinion is still a tutorial if the reader wants to follow its steps.
- A news piece with deeper explanation can use Essay / Analysis if the reader wants to understand the argument rather than decide what to do.
- A product article with many specifications is a Review / Comparison when the reader is deciding whether to buy; use Extract when they ask for specs only.
- If the request is generic and the source is explanatory or argumentative, default to **Understand**. Do not turn this default into an exhaustive section-by-section recap.
- If the source mostly entertains and has little useful information, use **Light / General**.

---

## Step 5: Special cases

- **YouTube Shorts:** reject immediately: *“This is a Short. Not enough content to summarize.”*
- **Paywalled content:** tell the user: *“This content is paywalled. Paste the text and I'll summarize it.”*
- **No transcript available:** tell the user what metadata is available and ask if they want a metadata-only summary.
- **Reddit threads:** out of scope for this skill.

---

## Step 6: Draft for that need

Load the selected prompt and `writing-quality.md`. Carry the chosen reader need into the draft. Include only details that help satisfy it; do not fill every section or preserve every example just because the source contains them.
