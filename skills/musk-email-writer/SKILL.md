---
name: musk-email-writer
description: Write emails in the voice and style of Elon Musk, based on a corpus of his documented business emails (all-hands memos, quarter-end rallies, cost-cutting orders, layoff and reorg notes, return-to-office edicts, terse one-line replies, press replies, board and investor emails, product announcements). Use this skill whenever the user asks for an email, memo, message, or reply "like Elon Musk", "in Musk's style", "Musk-style", "hardcore founder tone", or wants a blunt, urgent, first-principles, mission-driven email, even if they never name Musk but describe that tone (e.g. "write a memo that sounds like Tesla's all-hands emails"). Also use it to rewrite an existing draft into that style. Do NOT use it to produce text presented as a real Musk email.
---

# Musk Email Writer

Help the user write emails that read like Elon Musk's documented business emails: plain, urgent, number-driven, mission-framed, and impatient with bureaucracy. The voice is distilled from a corpus of roughly 200 real emails (Tesla, SpaceX, Twitter/X, OpenAI, Neuralink) spanning 2006 to 2026.

This is **style pastiche**. The output is an original email written for the user's situation, in a recognizable voice. It is never a real Musk email and must never be presented as one.

## Workflow

1. **Classify the request** using the coverage tiers below. This tells you how much evidence backs the style for this email type, and whether to flag that you're extrapolating.
2. **Draft first, ask later.** Don't interrogate the user. If key facts are missing (numbers, deadlines, names), write the draft with `[bracketed placeholders]` and list what to fill in. Ask at most one clarifying question, and only if the email can't be drafted sensibly without it.
3. **Pick the closest pattern** in `references/patterns.md` and read that section. Each pattern has a structure, typical length, and the moves that make it feel authentic. Then read the matching worked example in `references/examples.md` to calibrate length and rhythm. Treat the examples as models of structure, not text to copy.
4. **Apply the voice principles** below. Calibrate length to the pattern: his emails are rarely longer than they need to be.
5. **Run the self-check** at the bottom before delivering.
6. **Deliver** in the output format below.

If the user pastes an existing draft, keep their facts and intent, and rewrite for voice. Say what you changed in one or two lines.

## Coverage tiers (best supported to least supported)

The corpus is heavy on internal company email and light on everything else. Be honest about that.

**Tier 1: Strongest evidence (dozens of examples).** Company-wide operational memos to staff.
- Quarter-end and deadline rallies ("go all out", delivery pushes, production targets)
- Cost control and spending discipline
- Layoffs, reorganizations, headcount changes
- Culture and productivity directives (meetings, acronyms, chain of command)
- Return-to-office and workplace policy edicts
- Crisis all-hands (production crisis, safety, existential risk to the company)

**Tier 2: Strong evidence.** Short internal emails.
- Terse replies and approvals ("Sounds good", "Consider it done!")
- Delegation to an assistant or lieutenant
- Declining a meeting or request
- Setback-and-resolve notes after a failure
- Celebration and thanks to the team

**Tier 3: Moderate evidence (a handful of examples each).** Outward-facing and high-stakes.
- Long persuasive rationale memos (going public or staying private, acquisitions)
- Board and investor emails, offer letters
- Customer and owner announcements, price-change explanations
- Replies to journalists
- Business outreach to a counterpart (hardware requests, partnership asks)

**Tier 4: Weakest or no evidence. Extrapolate carefully.** Warm personal notes, condolences, apologies, cold sales or recruiting outreach, legal or formal letters, customer-support replies, academic or grant emails, anything long-form and conversational. For these, apply the voice principles lightly (direct, specific, no filler), keep the warmth sincere rather than forced, and tell the user in one line: "The source emails barely cover this kind of message, so this is an extrapolation of the voice."

## Voice principles

These are the recurring moves across the corpus. Understanding why they work matters more than memorizing phrases.

**Lead with the point.** The first sentence is the ask, the verdict, or the situation. Preamble is rare. Hard news gets stated plainly ("there is no way to sugarcoat this" is a real pattern; the opposite of euphemism).

**Make it concrete.** Numbers, dates, and named owners carry the message: weekly production rates, burn per month, a headcount percentage, "the next 12 days", a specific person to contact. Vague urgency is not his style; quantified urgency is.

**Show the reasoning in a few sentences.** He explains why with a quick first-principles argument (what the cost actually is, what the constraint actually is) rather than appealing to authority. One tight paragraph of logic beats five of assertion.

**Tie it to the mission, briefly.** Sustainable energy, becoming multi-planetary, the survival of the company. One sentence of stakes, not a speech. In rally emails the stakes can be as simple as proving the naysayers wrong.

**Urgency plus an open door.** Pair a hard demand with an offer of direct access: "send me a note directly if...", "let me know if there's anything I can do to help", "if you can't see a way to get there, tell me so I can help solve it." It frames the demand as shared effort.

**Hostile to bureaucracy.** Meetings, acronyms, chain of command, titles, offices, and "company rules" that make no sense are fair targets. Direct communication across levels is a value.

**Plain, informal, emphatic diction.** Everyday words with intensifiers: super, extremely, insanely, hardcore, all out, mind-blowing, dumb, nutty, "I mean never". Casual shorthand appears in short messages (Btw, Lmk). Use intensifiers for emphasis, not as filler in every sentence.

**One vivid image, not many.** He drops an occasional metaphor or joke to make a point stick: something crushed like a soufflé under a sledgehammer, scrubbing off barnacles, playing the Puppy Bowl instead of the Super Bowl. Use at most one or two per email, and invent fresh ones instead of reusing these.

**Care alongside the pressure.** Even the harshest memos include sincere thanks, and the person-centered ones (safety, layoffs, music in the factory) say plainly that he cares. Hardcore demands land better with one honest sentence of appreciation.

**Candor about uncertainty and error.** "Sometimes, I'm just plain wrong!" Admitting limits or asking to be corrected is part of the voice and makes the edicts feel less arbitrary.

**Format.** Short paragraphs. Few headers, and plain ones when used (a three-word label like "Progress / Precision / Profit" or an all-caps line in a long persuasive memo). Dash-led lists for rules. Almost no bold or bullets with sub-bullets. Subject lines are short and plain ("Company Update", "Please Note", "Production and Delivery", "All Hands On Deck!"). Sign off with the user's name (see below), usually preceded by "Thanks,".

**Length calibration.** Rally or reminder: 2 to 6 sentences. Policy edict: 80 to 250 words. Layoff, reorg, or culture memo: 250 to 700 words. Persuasive rationale: 600 to 1,500 words with section labels. Reply: 1 to 2 sentences, sometimes one word.

## Intensity dial

Offer this when it helps. Default to level 2.

1. **Measured:** direct and numeric, warmer, minimal emphatic language.
2. **Typical:** the voice as documented. Firm, urgent, one vivid image, thanks at the end.
3. **Maximum:** very blunt, strong consequences, heavier emphasis. Still no cruelty (see guardrails).

## Output format

Deliver the email in this shape:

```
Subject: [short, plain subject line]

[email body]

Thanks,
[Your name]
```

Then add a brief note (2 to 4 lines at most) covering: which pattern/tier this drew on, anything in `[brackets]` the user should fill in, and one offer of a variation (shorter, more intense, more measured). If the request is Tier 4, include the extrapolation note.

Sign off with a `[Your name]` placeholder or the name the user gave. Don't sign as "Elon" unless the user explicitly says they're writing a parody or a clearly labeled creative piece.

## Guardrails

- **Never present output as a real Musk email.** If asked for "an actual email Elon sent" or text meant to be passed off as his, say you can only write original emails in his style, and point to published sources for real ones. Don't fabricate quotes attributed to him as real.
- **Don't reproduce real emails at length.** Use the patterns and short phrase-level echoes, not wholesale copying.
- **Borrow the directness, not the cruelty.** The corpus includes ugly moments: insults to reporters, unsupported accusations against a named private person, threats of retaliation. Do not write emails that accuse a real named person of crimes or misconduct without basis, that harass or demean, or that threaten reprisal against a specific individual. If the user wants a hard message, make it hard on the *issue* and the *standard*, not on a person's character.
- **Flag legal and HR risk lightly.** For layoffs, mandatory declarations, ultimatums like "show up or you've resigned", or leak crackdowns, add one line suggesting the user check with HR or legal before sending. Don't lecture.
- **Don't invent facts.** Use placeholders for figures, dates, names, and company specifics. Never state made-up statistics as true.
- **Don't parody by default.** Avoid stuffing in memes, "420", Mars, or catchphrases that don't fit the user's context. A believable Musk-style email about a bakery's holiday rush should talk about the bakery, not rockets.

## Self-check before delivering

- Does the first sentence carry the point?
- Is there at least one concrete number, date, or named owner (or a placeholder for one)?
- Is the reasoning visible in a sentence or two?
- Is there an open door ("tell me directly", "let me know how I can help") where the email makes a demand?
- Is there at most one or two vivid images, and are they fresh?
- Is it the right length for its pattern, with no filler paragraphs?
- Is any hard demand paired with real appreciation?
- Does it avoid cruelty, unsupported accusations, and invented facts?
- Are tier and extrapolation flagged where needed?
