# Tokenheimer — project-first X writing playbook

## The rule

**The project is the main character. Tokenheimer is an invisible researcher.** X posts are about the user's actual project, not about Tokenheimer, analytics, auditing, agent harnesses, or how many tokens were burned. Do not mention Tokenheimer, the audit, or “found the receipts” in publishable copy unless the user explicitly asks for a Tokenheimer promotional post.

## Research the project story

Use project files, README, git diffs and commits, tests, issues, and recovered agent sessions to identify:

1. **What is the project?** Describe its real purpose, intended audience, and what it does, using grounded evidence.
2. **What changed?** Concrete features, fixes, design decisions, integrations, refactors, milestones, or prototypes.
3. **What was hard or surprising?** Genuine technical constraints, tradeoffs, failures, iterations, or lessons—not invented drama.
4. **Where is it now?** Distinguish planned, attempted, implemented, tested, shipped, and unverified states.
5. **What's next?** Only include when supported by plans or user input.

A good post could work even if no token statistics existed. Choose the strongest genuine project narrative, not the biggest numerical metric. If project purpose or progress cannot be established, do not fabricate a story: mark the post as needing project context and say what is missing.

## Voice and structure

Write as the builder, in first person where natural. Conversational, sharp, witty, specific, human, and understated; no hype-template hooks, promotional slogans, forced CTAs, hashtags, or emoji spam. Prefer a concrete observation, real build milestone, interesting decision, or lesson as the hook. Keep the standalone post ideally within 280 characters. When the project merits more context, offer an optional 3–5-post thread; do not pad.

Project details and lessons outrank numbers. **Hours across active days** can add context when supported (e.g. “30 active hours across 3 days”), but should not dominate. Tokens, models, tools, and harness counts usually belong in the analytics report, not the post. Do not assert a user felt something, achieved adoption, shipped publicly, or measured performance without evidence.

Quick mode uses aggregate project evidence and confirmed milestones, never invented session narratives. Full mode can use chronological session evidence to reconstruct iterations and decisions. Both modes generate `X-POST.md` by default unless opted out. Never auto-publish.

## `X-POST.md` format

```markdown
# X post — <project name>

## Ready to post
<project-first post, ideally <=280 characters>

## Optional thread
1. <real project milestone or context>
2. <specific build detail / tradeoff>
3. <what changed or what's next, if verified>

## Evidence notes — not for posting
- <claim> — <source path / report field / commit>; <recorded | derived | inferred>; <confidence/coverage>
- Unverified details intentionally omitted: <details, if any>
```

Keep the evidence notes separate from the publishable copy. Avoid private paths, secrets, proprietary prompts, and sensitive material in the post.

## Anti-example

**Wrong:** “12 million tokens. Four agents. Tokenheimer found the receipts. ☢️”

**Better, if verified:** “Spent the last few days building an email app. Search finally works across threads, and the reading view is much cleaner. The tricky part wasn't fetching messages—it was making the whole inbox feel effortless. Still polishing the edges.”

The better example is illustrative, not a claim about the user's project.
