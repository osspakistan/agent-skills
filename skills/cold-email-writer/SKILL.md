---
name: cold-email-writer
description: Write, rewrite, and critique cold outreach emails that get replies. Covers investor/fundraising outreach, customer and sales prospecting, partnership asks, recruiting, press and advisor intros, and follow-ups. Use this skill whenever the user asks for a cold email, cold DM, outreach message, investor email, intro request, "email to a stranger", follow-up to an ignored email, or wants a draft reviewed or tightened, even if they never say "cold email". Also use it when they paste a draft and ask why it isn't getting replies. Drafts are short, proof-first, and free of fake personalization.
---

# Cold Email Writer

Write cold emails a busy stranger will actually answer. Distilled from Y Combinator's cold-email advice, OpenVC's critique of the "custom hook" template, a 5-rule founder slide, Alex Hormozi's offer and sales advice, and the terse style of ~200 documented Musk emails.

Core idea: a cold email earns a reply with **proof and clarity**, not flattery or fake personalization. AI and mail-merge made the "Heard you on the podcast, congrats on X, since you're big on Y..." hook free, so recipients now read it as a template.

## Workflow

1. **Gather inputs.** Need: sender (founder or SDR/agent?), recipient, what you do, best proof, the ask. If something is missing, draft anyway with `[placeholders]` and list what to fill in. Ask at most one question, only if the draft can't be written sensibly without it.
1b. **Check the offer** (sales, services, agency outreach). If there is no concrete offer (outcome, mechanism, timeline), fix that first. Read `references/offer-and-sales.md`.
2. **Decide on personalization.** Read `references/personalization.md`. Default is no hook. Include one only if it passes the "could this be pasted onto another recipient?" test.
3. **Draft** using the structure below. Read `references/principles.md` for the full rule set and `references/examples.md` to calibrate length and tone.
4. **Run the self-check** below and fix failures silently.
5. **Deliver** in the output format.

If the user pastes a draft, keep their facts, diagnose in 3-5 bullets (what reads as template, what's buried, what's unverifiable), then give the rewrite.

## Structure (3-5 sentences, under 60 seconds to read)

1. **What you do**, plain words, zero jargon. Say what the product does, not the category.
2. **Best proof**, one or two checkable facts: paid pilots, revenue, growth, launch, named customers, a technical team with relevant credentials. Put the strongest first.
3. **Why it matters to them** (only if real and specific). Their pain in their words, or one genuine reason it's them. For sales, lead with the outcome and name the pain accurately (see `references/offer-and-sales.md`).
4. **The ask**, explicit and on its own line right before the sign-off. Ask for something small: a reply, advice, an intro, permission to send a short demo or deck. Not a 30-minute meeting from a stranger.
5. Sign off with name and role. Short, casual subject line (what + proof, e.g. "Automated bank QA, 2 paid pilots").

## Self-check before delivering

- Under ~100 words? Readable aloud in under a minute?
- First sentence says what the company does, with no warm-up?
- Zero flattery, zero backstory, zero origin story?
- Every claim checkable? No "proven 10x ROI" or "$18B market" without a source or definition.
- Any hook passes the swap test, or is removed?
- One goal, one ask, on its own line, smaller than a meeting?
- Sounds like a person talking, not an AE or a pitch deck? ("Cheers", "I'd love to pick your brain", "game-changing" = cut.)
- Subject line short and casual?
- (Sales) Is there a real offer: outcome, mechanism, timeline? Scarcity or guarantee only if true?

## Output format

1. The email (subject + body) in a block.
2. Under it, 2-4 lines: what's placeholder, what claim needs a source, and one optional variant (e.g. shorter, or with a real hook) only if useful.
3. Add the follow-up (see `references/followups-and-delivery.md`) only if asked or if the user is sending a sequence.

Keep commentary tight. Don't lecture about the rules unless asked.

## Sender matters

Founder-sent emails get away with more brevity because the sender is the proof. An SDR, agent, or AI sender has to earn the reply from the email alone: stronger proof, clearer fit, borrowed credibility (customer names, YC, past employers). Ask or infer who is sending and adjust.

## Tone

Default: plain, direct, founder-voice. If the user wants it blunter or more "Musk-style", read `references/musk-tone.md`. This is style only. Never present output as a real Musk email, and note that his emails are mostly warm or internal, so brevity there leaned on existing credibility.

## Reference files

- `references/principles.md`: the consolidated rule set and where sources agree or conflict
- `references/personalization.md`: when and how to personalize, the swap test
- `references/examples.md`: before/after rewrites (investor, sales) and a bad-vs-good checklist
- `references/offer-and-sales.md`: Hormozi offer rules mapped onto email copy, value equation, sales-process rules, how they reconcile with YC/OpenVC
- `references/musk-tone.md`: terse-style moves and their limits for cold use
- `references/followups-and-delivery.md`: follow-up cadence, ignored emails, SPF/DKIM/DMARC check
