# Writing Quality

<!-- Bundled from the human-pencil skill (github.com/alwaisy/human-pencil).
     Inlined here so fewwords-summarizer ships as a self-contained skill with zero external dependencies. -->

---

## The Goal

Make the summary sound like a sharp, well-read person wrote it on a good day. Remove formulaic, padded, or AI-coded prose. Preserve meaning, specifics, and the natural shape of the source.

**Never invent facts, sources, quotes, statistics, experiences, or opinions to make prose feel more human.**

---

## Write with a Light Hand

- **Preserve Intent & Nuance:** Keep the point, structure, and level of detail unless they make the draft harder to understand. Do not compress away useful nuance.
- **Tone Calibration:** Notice the source's vocabulary, cadence, humor, bluntness, uncertainty, and polish. Keep strong sentences, distinctive details, real emotion, mixed feelings, and honest uncertainty. A formal or slightly awkward sentence is not automatically a problem.
- **Voice & Clarity:** Use active voice when it clarifies who did what. Keep passive voice when the actor is unknown, irrelevant, or less important than the result. Keep fragments when they fit the writer or format.
- **No Manufactured Intimacy:** Vary sentence length and paragraph shape naturally. Do not add fake intimacy, jokes, first-person opinions, or manufactured urgency to neutral or technical content.
- **Concrete Facts:** Prefer concrete facts, named actors, specific verbs, and examples supported by the draft. When claims need sourcing, flag the gap instead of inventing citations.

---

## Pattern Guide Checklist — Scan Before Finishing

Inspect for pattern clusters, not isolated words. Treat these as diagnostic checkpoints:

### 1. Inflated Claims and Unsupported Authority
- **Significance puffery:** "marks a pivotal moment," "stands as a testament," "plays a vital role," "underscores its importance," "sets the stage for," or claiming a small fact reflects a broad trend. State what happened and let the reader judge.
- **Promotional gloss:** "breathtaking," "vibrant," "stunning," "renowned," "groundbreaking," "must-visit," "must-read" — praise without evidence. Replace with concrete qualities, outcomes, or facts.
- **Vague authority:** "experts say," "industry observers note," "studies show," "widely regarded" without identifying a source. Name the source and what it found, or remove/qualify the claim.
- **Speculative gap filling:** guesses about motives or circumstances wrapped in "details are scarce" or "maintains a low profile." State what is known, flag what is unknown, or omit.
- **Generic scale or notability claims:** lists of media coverage, follower counts, or broad adoption without explaining what they establish.
- **False agency:** data, markets, complaints, or culture "decide," "tell us," "reward," or "become" things. Name the people and mechanism when known.

### 2. Formulaic Structure and Rhythm
- **Binary contrast & negative listing:** "It's not X, it's Y," "not just X but Y," or "not X, not Y, but Z." State the useful claim directly.
- **Canned persuasion formulas:** "In a world where...", "most people do X, the few who win do Y," "stop X, start Y," "if you aren't doing X you're behind," "the real work isn't X, it's Y," "you don't need X, you need Y," "it's never been easier/harder." Replace with the specific consequence or action.
- **Faux-reveal & throat-clearing hooks:** "Here's the truth," "what nobody tells you," "the part everyone misses," "honestly?", "look," "let me be clear" when they delay a routine claim. Start directly with the claim.
- **Rhetorical scaffolding:** "What if I told you?", "think about it," "here's what I mean," self-answered Q&A pairs, or signposts like "let's dive in" / "without further ado." Say the thing.
- **Dramatic fragments & fake punchlines:** strings of clipped sentences, repeated "Not X. Not Y. Z," or final mic-drop metaphors.
- **Rule of three:** ideas repeatedly forced into three-part lists or parallel slogans. Use the exact number the idea needs.
- **Robotic symmetry:** repeated sentence openings, identical paragraph shapes, metronomic mid-length sentences, or every paragraph ending with a punchline.
- **Summary-recap endings:** "In conclusion," generic optimism, "the future looks bright," or a final paragraph that just repeats earlier points. End with the final useful fact, implication, or next step.
- **Formulaic outlook sections:** generic "challenges and future prospects" that list stock problems and declare the subject will thrive.
- **Diff-anchored prose:** describing a thing mainly as a change from an earlier version when it should stand alone. Describe how it works now.
- **Fragmented headers:** a heading followed by a filler sentence that merely repeats it. Begin with the useful detail.
- **False ranges:** "from X to Y" when the endpoints are not meaningful ends of a scale.

### 3. Word Choice and Sentence Construction
- **AI-coded vocabulary:** *delve, realm, harness, unlock, tapestry, paradigm, cutting-edge, revolutionize, landscape, intricate, crucial, pivotal, leverage, synergy, innovative, game-changer, testament, meticulous, groundbreaking, foster, enhance, holistic, garner, transformative, seamless, optimize, scalable, robust, empower, streamline, elevate, proactive, disruptive, reimagine, agile, intuitive, automate, accelerate, dynamic, efficient, immersive, predictive, integrated, turnkey, future-proof, AI-powered, next-generation, ever-evolving, multifaceted, beacon, embark, supercharge.* Replace when a plain, specific word says more.
- **Empty intensifiers & adverbs:** *really, just, literally, genuinely, honestly, simply, actually, deeply, truly, fundamentally, inherently, inevitably, interestingly, importantly, crucially.* Delete when they add no voice or emphasis.
- **Business jargon:** *navigate challenges, unpack, lean into, double down, deep dive, take a step back, moving forward, circle back, on the same page, utilize.* Use ordinary verbs.
- **Filler openers:** *it's worth noting, it's important to note, at the end of the day, when it comes to, at its core, in today's world, in the age of, the reality is, the truth is, in terms of, with regard to, in order to, going forward, in this article.*
- **Superficial trailing clauses:** "highlighting the team's commitment," "reflecting its importance," "showcasing a deep connection" that claim meaning without adding evidence.
- **Copula avoidance & fake-strong verbs:** "serves as," "stands as," "boasts," "features," "offers" where plain "is" or "has" is clearer.
- **Synonym cycling:** calling the same person or thing "the agent," "the assistant," "the tool," and "the system" solely to avoid repetition. Repeat the accurate term.
- **Passive or subjectless phrasing:** "mistakes were made" or "results are preserved" hiding the actor. Name the actor when known and relevant.
- **Excessive hedging:** layers of *could, potentially, possibly, might* around a simple claim. Keep real uncertainty; cut the padding.
- **Noun piles & weak verb phrases:** "made a decision" or "has the ability to process" → "decided" or "can process."

### 4. Layout, Formatting & Attribution Discipline
- **Paragraph breathing rule:** Keep paragraphs short (2-3 sentences max). Write one sentence per line with a blank line after each sentence.
- **Quotation format:** Use markdown quote blocks (`> Quote goes here`) strictly WITHOUT quotation marks (`"..."`).
- **Dev terminology / code:** Inline code backticks for commands, APIs, protocols, technical specs: `npm install`, `TCP/IP`, `O(n)`.
- **Entity styling:** Human names in **bold**; companies, products, tools, and platforms in *italics*.
- **Title format:** Always output on its own line starting with plain `TITLE: ` (do not bold).
- **Attribution ban:** Speak the information directly as your own. Never use meta-attributions like "the author states", "the article mentions", or "in this video".
- **Deduplication:** If a fact, argument, or warning is repeated multiple times in the source, state it once.
- **Dynamic headers:** Keep body section headings dynamic, conversational, and max 3 words.
- **Header pattern ban:** NEVER use the formulaic `The {xyz}` pattern (banned: *The Overview*, *The Breakdown*, *The Takeaway*, *The Facts*, *The Key Points*).
- **Em/en dashes:** In short copy, usually replace with a period, comma, or parentheses. Retain only when it genuinely improves cadence.
- **Overformatted emphasis:** Do not bold ordinary nouns or scatter emoji headings.
- **Chatbot residue:** Strip "Great question," "I hope this helps," "let me know if you need anything else."

---

## Finish Check

Reread the full output:
1. Does it preserve the source's actual meaning and voice?
2. Is each claim backed by the source, with zero invented facts or metrics?
3. Did you prune away clusters from the checklist that weaken the piece?
