---
name: card-your-pivot
description: Turn a person's career documents (a CV, bootcamp notes, a plan they wrote once, a journal) into the Cairns section of their Cairn deck, a career plan as cards, a baseline, plans A, B and Z, phases, goals with dates, opportunities with a reasoned decision, uncertainties with their cheapest test, boundaries, and a first check-in, every line a scaffold in the person's own words for them to overwrite. Use when someone asks to plan a career change, structure a job search, or set up their Cairns.
---

# Card your pivot

You are drafting cards for Cairn, a study companion that keeps everything a person is learning in one local file. This skill makes the **Cairns** section: a career plan kept next to the work it is for, so the plan cannot drift silently and every check-in leaves a stone. Everything you write here is a scaffold of the person's own voice, built from their own documents, for them to overwrite; you add nothing they did not say.

## Two things to settle before you draft

**1. Do they already have a Cairns section?** Ask, or read their deck. **There is one career per person**, so every run after the first is an update, not a new section. Cards with new ids do not replace the old ones — they land beside them, and the person ends up with two Plan As, two baselines and two Phase 1s disagreeing about which phase they are in. If they have a section: send changed cards under **their existing ids**, say plainly in your reply that importing replaces each of those cards whole, and send only what has actually changed. If they do not: mint ids as `cairn-<type>-<slug>` (`cairn-plan-a`, `cairn-phase-1`), which is what the app's own section uses.

**2. How old are the documents?** A CV from April read in September describes April. **`source` on every card names the document and its date**, in the form a working deck uses: *"Career bootcamp notes, April 2026 — carded September 2026"*. `baseline.asOf` is the document's date, not today's. And **no field is filled with "today" unless the person is in the room with you**: a boundary marked `lastReviewed` today, drafted from a five-month-old document, is a false statement in a date field, and a check-in dated today says a check-in happened today. Working from documents alone, take those dates from the documents or leave them out and say so in your reply.

## What the section is made of

Every card: `memberships: [{"section": "cairns"}]`, a `source` naming the document, `tags` — one standing tag for the section is the convention (`cairns-seed`) — and the fields below (the spec has the app's own help text for each).

- **baseline** (one): where they started. `asOf` (the documents' date), `body` (who they are on day one, in their words — the front of the card), `achievements`, `strengths`, `constraints`, `motivations`, `links`.
- **plan** (up to three): `planLetter` A (the primary bet), B (the fallback), Z (the safety net); `statement` (the front), `routes`, `targetOrgs`, `switchTriggers` ("I move to Plan B if X has not happened by Y"), `status` (`active` for A, `parked` for B and Z unless they say otherwise), `amendments` empty at creation (the app logs them as the plan changes; never pre-fill a history).
- **phase** (a few): `order`, `timeframe`, `purpose` (the front), `successCriteria` (things that can be checked), `status` — **read from the documents' own clock, not from today's**: `closed` for a phase the documents show behind them, `current` for the one they were in, `upcoming` for the rest. If the documents are old, say in your reply that the person may have moved on.
- **goal**: `statement` (the front), `phaseId` (the phase card's id — note that the app does not yet group by it; it is a link the section will use later, not a live one), `targetDate` (only if they named one; never invent a date), `status` (`not-started` unless they say otherwise), `evidence` and `outcome` empty.
- **opportunity**: a real posting or route they mentioned: `org`, `role` (the front), `link`, `deadline` as printed or `null`, `sourceBoard`, `decision`, `reasoning` in their words. The six `decision` values: `pursuing` (working on it now), `applied` (sent), `skipped` (looked and decided against), `later` (right thing, wrong time), `expired` (the route closed), `context-only` (kept because it tells them something about the field, not because they will apply). **This card type is not the `opportunities[]` field on a Field Map card** — that one is a route an organisation is offering, with its own vocabulary.
- **uncertainty**: `question` (what they do not know and the plan rests on — the front), `whyItMatters`, `cheapestTest` (one conversation before one course), `testStatus: open`.
- **boundary**: `statement` (what they will not do — the front), `why`, `status: holding`, `lastReviewed` (see above).
- **checkin** (one, the first): `date` (see above), `periodCovered`, and **the six questions**, answered from their documents where they are answered and left empty where they are not: `whatMoved`, `whatStalled`, `driftCheck`, `amendmentsMade`, `sustainability`, `nextPriority`.

`links` is a list of `{"label": "...", "url": "..."}`. Where a document holds a link and no card type has a home for it, say so in your reply rather than forcing it somewhere.

## Rules

- **Their words, their facts.** Every achievement, constraint, figure and date comes from the documents. Where a document is silent, the field is empty and your reply says so. No motivational language, no rewording a modest sentence into a bold one.
- **What they wrote is theirs to keep.** A person who hands you a planning document has already decided what goes in it. Carry what they wrote into the field that asks for it — `constraints` asks for credentials, location, health and runway in the app's own words, and `sustainability` on a check-in is a first-class field, not an optional one. **Do not add anything they did not write, and do not quietly leave out what they did**: emptying `sustainability` to be careful produces a thinner and less true plan than the one they keep themselves. **In your reply, list what you carried that they may want off a card**, so removing it is one edit and one decision of theirs.
- **Other people are not theirs to publish.** A named third party — a peer, a manager, a contact — does not go on a card unless the person asks for it. Their own detail is theirs; someone else's is not.
- **Dates only where they gave them.** A goal without a date is still a goal; the app's due-soon strip needs real dates, not decorative ones. A bare day and month with no year is a date you do not have: leave it `null` and put the wording in the field beside it. If a document writes a date ambiguously (`03/10/2026`), say in your reply which reading you took and why, because the app will treat it as a hard fact.
- **One plan per letter.** If the documents show two primary bets — *"both of these feel like the main road depending on the week"* — **do not pick one.** Write the plan they name as Plan A, and make an `uncertainty` card whose `question` is which road is the main one, with the documents' own sentence in `whyItMatters`. The indecision is information; resolving it silently is the one thing this section exists to prevent.
- **The check-in is theirs to write from then on.** You draft the first one only, from their documents; after that the app asks the six questions on their cadence.
- **Leave `myNotes` exactly as it is** — absent on a new card, untouched on one that already exists. On an update, sending it empty deletes what they wrote, because import replaces a card whole.
- **This section is as private as the person keeps it, and no more.** Cairns is a first-class row in the app's export, with its eight buckets under it and "Everything" above them — there is no privacy gate anywhere in that path. Do not tell the person their Cairns cannot travel; tell them what is on the cards.

## Do this, in order

1. Read the documents whole. List for yourself what is stated: strengths, constraints, motivations, routes, target organisations, deadlines, doubts, rules they set themselves — and the date each document was written.
2. Draft the baseline, then Plan A and any B or Z they described, then phases, then goals attached to phases, then opportunities, uncertainties, boundaries, and the first check-in.
3. Output one JSON file `{"version": 1, "cards": [...]}` shaped like `reference/example-pack.json`; run `python3 reference/check-pack.py your-pack.json --deck cairn-deck.json`. Fix the errors. **Read the warnings and decide** — they are claims about the app, not commands. Lines marked NOTE are the person's own fields and are never yours to clear.
4. In your reply: every field you left empty because the documents did not say; everything you carried that they may want off a card; every date you inferred; and, if they already had a section, exactly which of their cards this pack would replace.

## Files in this skill

- `reference/field-spec.md`: every Cairns card type, its fields, options and the app's own help text, plus the envelope every card carries.
- `reference/example-pack.json`: a made-up person's Cairns, one of each card type and a second phase, goal, opportunity and check-in, in the exact shape to produce.
- `reference/check-pack.py` with `schema.json`: the check to run before handing over a file.
