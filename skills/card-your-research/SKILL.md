---
name: card-your-research
description: Turn a person's own notes, drafts, transcripts or reading into Cairn research cards, a frontier (research topic) with its working set of theses, metrics, evidence, open questions, tensions, frameworks and stories, with the honesty badges set truthfully (maturity starts at Intuition, provenance says developed with AI when it was, evidence never without a limitation). Use when someone asks to structure their research, their thinking, a thesis, a research programme or a question they are sitting with.
---

# Card your research

You are drafting cards for Cairn, a study companion that keeps everything a person is learning in one local file. This skill makes the **Research** section: a scaffold for thinking in public before publishing, where every claim carries how sure the author is, whether they have read the source, and who wrote it. The person imports what you produce and reads every card first. Nothing here is ever more certain on the card than it is in the person's head.

## What the section is made of

- A **frontier** card (`type: frontier`, `sectionRoot: research`, `order`, `description`): the research topic, one per topic. Its `title` is the topic's name and is what every card under it carries in `track`.
- Under it, the working set, each with `memberships: [{"section": "research"}]` and `track` = the frontier's title:
  - **thesis**: `statement` (the claim in one or two sentences), `definition` (**the front of the card** — what the claim means, at more length), `theFrontier` (the frontier's title again; this type alone renders it), `anchor`, `metaphor`, `whyItMatters`, `evidenceFor`, `openProblems`, `maturity`, `readingStatus`, `provenance`;
  - **metric**: `whatItMeasures`, `howCalculated`, `definition` (the front), `anchor`, `whyItMatters`, `validityConcerns` (always filled: a metric with no doubts is not a metric), `maturity`, `readingStatus`, `provenance`;
  - **evidence**: `finding` (the front), `whyItMatters`, `sourceRef`, `strength`, `limitations` (always filled), `supportsThesis` (**which thesis this bears on and how it strengthens or complicates it** — a sentence, not a title), `sourceType` from the list, `maturity`, `readingStatus`, `provenance`;
  - **question**: `question`, `whyItMatters`, `currentThinking`, `status` (Open · Sitting with · Provisionally answered);
  - **tension**: `partyA`, `claimA`, `partyB`, `claimB`, `crux`, `whereItAppears`;
  - **framework**: `definition`, `components`, `whenToUse`, `anchor`, `metaphor`, `whyItMatters`;
  - **story**: `metaphor` (the front, one line), `body`.

`reference/field-spec.md` has every field with the app's own help text, and says which fields a type does not declare — a `maturity` badge written on a `concept` card is stored by the app and shown nowhere.

## The honesty apparatus, which you enforce

- **`maturity` starts at `Intuition`.** You never set `Developing`, `Evidenced` or `Contested` yourself. If the notes say a claim has evidence behind it, say so in `evidenceFor`, leave the badge at Intuition, and suggest promotion in your reply; promotion is the person's, by hand.
- **`readingStatus` says what the person has read, not what you have.** `Original` for their own thinking; otherwise `Unread` unless they tell you they have read the source.
- **`provenance` is a sentence, in the app's own vocabulary**, on thesis, metric and evidence: *Own work* · *Developed with AI* · *From the literature*, followed by the specifics. A card in a working deck reads like this: *"My own work. The conceptual core developed independently, from product experience and lived observation; the methodological critique was developed in dialogue with an AI assistant during the synthesis phase."* Never smooth it into a cleaner claim than the truth.
- **Evidence never ships without a `limitations` line**, and `sourceType` is from the list in the spec; a field note is `Original observation`, a blog post is `Essay or commentary`.
- **A thesis is one claim.** If the notes hold two, make two cards.
- **Questions are cards, not margins.** Anything the notes leave open becomes a `question` card with `status: Open`.

## Do this, in order

1. Read what the person gave you whole: notes, a draft, a transcript, a folder. Do not read outside it unless they ask for literature.
2. **Ask whether this topic already has a frontier card** — ask for their list of research topics, or for the deck. This matters more than it looks: a research direction whose name a person has not settled cannot be matched by title, so a second frontier card for the same direction is easy to make and splits the working set in two. If it exists, use its id and its exact title in `track`. If it does not, name it in their words, or ask; write its `description` as one paragraph. **If the notes explicitly reserve the naming decision, use their provisional words and add a `question` card saying the name is theirs to settle.** Leave `order` out unless you have the deck and can see the next free number.
3. Draft the working set: theses first, then what would test each (metrics), what is already known for or against (evidence), what is unresolved (questions), where positions clash (tensions), the reusable ways of thinking (frameworks) and the narratives that carry the ideas (stories).
4. Set every badge by the rules above. Where you are unsure whether a claim is the person's or yours, say `Developed with AI` and tell them.
5. **Leave `myNotes` and `researchRelevance` exactly as they are** — absent on a new card, untouched on one that already exists, because import replaces a card whole. `researchRelevance` is how cards elsewhere in the deck point at this research, and the person writes it.
6. **Tag** each card the way the section is tagged: `research`, the card's type, and a slug of the frontier. There is no "pack name" — the tags are how the person finds these cards again.
7. Output one JSON file `{"version": 1, "cards": [...]}` shaped like `reference/example-pack.json`; run `python3 reference/check-pack.py your-pack.json --deck cairn-deck.json` (drop `--deck` only if you do not have their deck, and say so). Fix the errors; read the warnings and decide, because they are claims about the app rather than commands; lines marked NOTE are the person's own fields and are not yours to clear.
8. In your reply, list each thesis with the badge you gave it and why, and every place you were unsure.

## One caution about `track`

`track` is what files a card under its frontier; `theFrontier` only draws a line on a thesis card. Get `track` exactly right — the frontier's title, character for character. A person who works across two frontiers may put both in one `track` string; that is theirs to do, and not a shape to invent for them.

## Files in this skill

- `reference/field-spec.md`: every research card type, its fields, options and the app's own help text, plus the envelope every card carries.
- `reference/example-pack.json`: one made-up frontier with a full working set, in the exact shape to produce.
- `reference/check-pack.py` with `schema.json`: the check to run before handing over a file.
