---
name: card-a-course
description: Turn a syllabus page, a course outline or a set of readings into Cairn course cards, structure first (the course guide, its units, one syllabus card per sub-unit with the readings) and then, reading by reading, the content cards (concepts, tensions, frameworks, people, actors, stories, glossary, exercises, open questions, and the reading itself as a library card). Use when someone asks to card a course, a module, a certificate, a reading group, or a book they are studying chapter by chapter.
---

# Card a course

You are drafting cards for Cairn, a study companion that keeps everything a person is learning in one local file. This skill makes the **Course** section: the skeleton of a course and the ideas inside its readings, each as a card the person can search, hear read aloud, mark and write on. The person imports what you produce and reads every card first.

## The two passes

**Pass 1, the structure.** From the syllabus alone, before any reading is opened:

1. **The course guide** (`type: guide`, `sectionRoot: course`): one per course. `title` = the course's name as it will show in the spine; `curriculum` the same name; `blurb` (the front of the card), `description`, `howToUse` and `aiWorkflow` say what this course is and how to study it. **Ask whether the person already has a guide for this course, or check their deck** — if they do, use its id and do not make another. A guide card you mint under a new id does not update theirs, and a guide card you mint under *their* id replaces theirs whole, including anything they wrote on it.
2. **One `courseUnit` per unit**: `courseId` = the guide's id, `unitKey` = `unit-1`, `unit-2`…, `order` = the number, `title` = the unit's full name as the syllabus gives it, `description` = the unit's own introduction, in the person's words if the syllabus's are not free to copy.
3. **One `syllabus` card per sub-unit** (or per unit when the course has no sub-units): `memberships: [{"course": <guide id>, "unitKey": "unit-N"}]`, `subLabel` `"N.M"`, **`title` in the course's own form** — the live deck's twenty-five all read `"Unit 4.4 — Layer 2: Constrain dangerous AI capabilities"`, the number and the name as the provider writes them — `intro` one paragraph (the front of the card), `duration` if stated, and `resources`: one row per reading with `title`, `author`, `year`, `readTime`, `required`, `summary`, `linkWritten`, `linkAudio` if there is one, and **`sourceMatch`**.

**`sourceMatch` is the one to get right.** It is a short distinctive fragment of the reading's title, and the identical string goes in `source` on every content card from that reading. The app matches the two by containment, either way round and case-insensitively, so either string may be the longer one; 97 of the 118 rows in the live deck are a fragment rather than the whole title. Nothing reports a mismatch: the cards simply never cluster under their reading, one card at a time, found by eye. Pick the fragment, write it on both sides, and say in your reply which fragment you used.

**In Pass 1 the `summary` is the provider's description in your words.** If the syllabus gives no description, leave it empty and fill it in Pass 2, when the reading is open. Do not write a summary of something you have not read.

Hand Pass 1 over as its own file and let the person import it and look at the spine before Pass 2. A wrong unit count is cheap to fix now and expensive after two hundred cards hang off it.

**Pass 2, the content, one reading at a time.** Read the reading whole. Then draft the cards it contains, and only those:

- a **library** card for the reading itself: `summary` (the front), `author`, `year`, `mediaType`, `status`. One per reading — the live deck has one on 117 of its 118 resource rows. If the reading is also a work on an author's shelf, it is **one card in two homes**, not two cards: `link-and-relate`, in the folder beside this one, says how.
- a **concept** for each idea worth remembering: `definition` (one or two sentences, the front), `anchor` (the moment in the reading where it lands), `metaphor` (one line), `whyItMatters`. **Title a concept with the proposition, not the noun** — *"The bottleneck is the judging, not the training"* rather than *"Scalable oversight"*. A card you can recall beats a dictionary entry, and the glossary is where the dictionary entry goes.
- a **glossary** entry for a term or acronym: `term`, `expansion`, `definition`, `example`. A term gets a glossary card **or** a concept card, not both: if the reading argues with the idea, it is a concept; if it only names it, it is glossary.
- a **tension** where two positions disagree: `partyA`, `claimA`, `partyB`, `claimB`, `crux` (the actual disagreement, not a summary of both, and the front of the card), `whereItAppears`;
- a **framework** for a reusable way of thinking: `definition`, `components`, `whenToUse`;
- a **cast** card **only for a person the reading keeps returning to**: `role` (the front), `stance`, `keyWorks`, `anchor`, `whyTheyMatter`; the title is the person's name. A reading that cites twenty people and dwells on none gets no cast cards, and that is the common answer.
- an **actor** for a group with power in the field: `whoAreThey` (the front), `whatTheyWant`, `whatTheyFear`, `whatTheyCanDo`, `whatTheyHaveDone`, `whatLimitsThem` — **each one left empty where the reading says nothing**. An actor card with three filled fields and three empty ones is a true card.
- a **story** for a narrative the reading tells: `metaphor` (one line, the front), `body`;
- an **exercise** for each prompt the course sets: `prompt` only; `userResponse` stays empty, it is the person's;
- an **open question** the reading leaves open: `question`, `whyItMatters`, `currentThinking` empty unless the person has one, `status: Open`.

Every content card: `memberships: [{"subUnit": <the syllabus card's id>}]`, `source` = the string matching that reading's `sourceMatch`, and `tags` naming the course and the type.

**How many cards is a reading worth?** As many as there are ideas the person could be asked about later, and no more. If two cards would carry the same sentence, they are one card. Two people running this skill on the same reading will differ, so say in your reply how many of each type you made and why, and let the person tell you if it is too many.

## Rules that keep the cards honest

- The **anchor is written to be remembered**, not to be complete: one concrete moment from the reading, in plain words.
- **Nothing invented.** A definition comes from the reading; if the reading does not define the term, say what the reading uses it to mean and no more. No quotations longer than a sentence; summaries in your words.
- **Plain English first, the hard word second.** Gloss every acronym the first time it appears on a card, because a stranger meets cards in any order.
- **The person's fields are left exactly as they are** — absent on a new card, **untouched on a card that already exists**: `myNotes`, `userResponse`, `researchRelevance`, `resourceProgress`. Sending one of them empty on a card the person already has deletes what they wrote, because import replaces a card whole. `resourceProgress` holds their own review and flashcard ticks — a tick is a claim about what they have actually done.
- **`readingStatus` is not a course field.** The app declares it on thesis, metric and evidence cards only; written on a concept or a library card it is stored and never shown. If the person keeps a convention of their own about it, that is theirs to apply.
- **A syllabus's readings are the provider's.** Titles, authors, links and times are facts; the `summary` is yours. If a course's materials are not free to share onward, say so in your reply; the person decides what a pack may contain.

## Output and check

One JSON file per pass, `{"version": 1, "cards": [...]}`, shaped like `reference/example-pack.json`.

```
python3 reference/check-pack.py pass-1.json --deck cairn-deck.json
python3 reference/check-pack.py pass-2.json --deck cairn-deck.json pass-1.json
```

`--deck` takes more than one file, which is how Pass 2 is checked before Pass 1 has been imported: the syllabus ids its cards point at are in Pass 1. Fix the errors. **Read the warnings and decide** — they are claims about the app, not commands. Lines marked NOTE are the person's own fields and are never yours to clear. Then tell the person, in your reply, which readings you carded, which you could not open, and how many cards of each type.

## Files in this skill

- `reference/field-spec.md`: every course card type, its fields, options and the app's own help text; the envelope; the `resources` row contract.
- `reference/example-pack.json`: a one-unit made-up course, structure and content, in the exact shape to produce.
- `reference/check-pack.py` with `schema.json`: the check to run before handing over a file.
