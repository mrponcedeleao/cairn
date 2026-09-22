---
name: link-and-relate
description: Decide and write how Cairn cards connect, when a card should appear in two places (a reading in a course and on an author's shelf; a question in a course and in the research), when it should only link through Related cards, how a Further Reading shelf is built around a principal, and how a research-relevance line is written. Use when someone asks to file a card in two homes, build an author's shelf, connect course cards to their research, or fix cards that landed in the wrong place.
---

# Link and relate

You are working on cards for Cairn, a study companion that keeps everything a person is learning in one local file. This skill is about **placement**: where a card is filed, when one card lives in two homes, and when two cards should merely point at each other. It edits placement on cards the person already has, or sets it on cards other skills produced. It creates no content.

## The three ways cards connect, and when each is right

**1. Two homes, one card (`memberships`).** Use when the same thing genuinely belongs in two sections: a book chapter a course assigns is one `library` card that appears in the unit and on its author's shelf; an open question a reading raises and the person is now researching is one `question` card in the unit and in the research. The card's back says where it appears; editing it once changes it everywhere. Never make a copy.

- In a course unit: `{"subUnit": "<syllabus card id>"}` and `source` = the string that matches that reading's `sourceMatch` row.
- In Further Reading, on the general list: `{"section": "furtherReading"}`.
- On a principal's shelf: `{"cast": "<principal id>"}` — **never `{"section": "furtherReading"}` beside it.** A `{"subUnit": …}` home may stand alongside, and often should: a course reading that is also on an author's shelf is one card with both. See below.
- In the Research section: `{"section": "research"}` and `track` = the frontier's title.
- In the Field Map: `{"section": "fieldMap"}` — always on an institution or platform, and it may carry a `subUnit` as well when a course names that organisation.
- In Cairns: `{"section": "cairns"}`.

**2. A pointer, not a home (`relatedIds`).** Use when the connection is worth a click but the card would be wrong in the other list: an institution a plan targets (the plan points; the institution stays in the Field Map); a concept from the course that a thesis leans on (the thesis points; the concept stays in its unit). `relatedIds` is a list of card ids; Related cards render at the foot of both cards' backs **only if both point**, so write the id on both sides when the relation is symmetric.

**3. A sentence (`researchRelevance`).** Use when a course or reading card bears on the person's research: one or two sentences saying what this reading contributes to which frontier, naming the frontier. It shows only when filled and is read aloud with the card. **It is the person's own field** — write it only when they have told you what the reading contributes, in their words; otherwise leave it empty and ask.

**Which to choose:** if the card would look right in the other list, two homes; if it would look out of place there but a reader would want the jump, a pointer; if the link is an argument rather than a place, a sentence.

## The shelf, exactly as the app reads it

A shelf is a **principal**: a `sectionMember` card with

- **`id` beginning `fr-member-`** — this is load-bearing, not a convention. The app decides that a card belongs to Further Reading by looking at the cast id and testing that prefix literally. A principal called `member-ada-lovelace` gathers nothing and its works land nowhere, silently.
- `sectionRoot: furtherReading`, `order`, `description` (who they are and why they are here).
- **`title`** = the shelf's name, in the person-or-organisation form: *Dario Amodei / Anthropic*, *Demis Hassabis / DeepMind*.
- **`castMatch`** = the title of that person's `cast` card, **character for character**. `title` and `castMatch` are two different strings doing two different jobs: the title names the shelf, `castMatch` pairs it with the cast card. A working deck's shelf reads *"Ada Lovelace — Notes on the Analytical Engine"* against a `castMatch` of *"Ada Lovelace"*.
- **`resources` rows**, one per work: `title`, `author`, `year`, `readTime`, `required: false`, `summary`, links, and **`sourceMatch`** — a short distinctive fragment of the work's title.

Then each work is a `library` card carrying `{"cast": "<the principal's id>"}` **alone**, with **`source`** set to a string that matches its `sourceMatch` row. That match is what gathers the shelf: the app compares the two by containment, either way round, case-insensitively. A work with an empty `source` sits under the principal and outside every row of the shelf. The person's `cast` card for the same person carries `{"cast": "<id>"}` too, and its title equals `castMatch` exactly.

**Do not add `{"section": "furtherReading"}` beside a `{"cast": ...}` membership.** The section is implied from the cast id; 0 of 2,122 cards in the live deck carry both, and the pairing is an error rather than a redundancy.

## A principal who is not in the deck yet

Step 1 below says never guess an id — and a new principal has no id to guess. Mint one, in this order, and send the whole set as one pack so the ids resolve on import:

1. The `sectionMember` card: `fr-member-<surname>`, with everything above. `order` is the next free number — ask for it, or leave it out and say so in your reply.
2. The `cast` card for the person: `{"cast": "<that id>"}`, `title` exactly equal to `castMatch`.
3. One `library` card per work: `{"cast": "<that id>"}`, `source` matching its `resources` row.

## Fixing a misplaced card

A card is misplaced when it appears under a section or unit it does not belong to, or cannot be found where expected. Search finds it by any word in it; its back says where it appears. Correct the `memberships` list, keeping any home that is right and removing the wrong one. **Re-import the corrected card under its own id** — import replaces the card whole, so send the whole card, not only the placement, and say so in your reply, because everything you leave out is deleted.

## Do this, in order

1. Ask for, or read from the deck file, the ids you need: the syllabus card of the unit, the principal of the shelf, the frontier's title. Never guess an id — `check-pack.py --deck cairn-deck.json` tells you whether one exists.
2. For each card, choose two homes, a pointer or a sentence by the rule above, and say which and why in your reply.
3. Send back whole cards with the corrected `memberships`, `relatedIds`, `source`, `track` or `researchRelevance`, as a pack `{"version": 1, "cards": [...]}`; run `python3 reference/check-pack.py your-pack.json --deck cairn-deck.json`.
4. Leave `myNotes` alone.

## Files in this skill

- `reference/field-spec.md`: the placement contract, the envelope, and the card types most often placed in two homes, with the `resources` row contract for shelves.
- `reference/example-pack.json`: a principal with two works, one of them a course reading in two homes, the principal's cast card, a question in a unit and in the research, and the course cards those placements point at.
- `reference/check-pack.py` with `schema.json`: the check to run, with `--deck` so ids are verified against the deck.
