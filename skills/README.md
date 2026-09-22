# Cairn skills, for AI assistants

A skill is a folder with an instruction file (`SKILL.md`) that an AI assistant reads first, so the cards it drafts follow the same conventions as the guides in your deck. Give your assistant the folder (or paste `SKILL.md` and the files under `reference/`) together with the source you want carded, and ask for a pack: a JSON file you then import into Cairn (Menu, Import). Nothing reaches your deck until you import it, and you read every card first.

| Skill | Use it when | Section it fills |
|---|---|---|
| `card-a-course` | a syllabus, a module, a certificate, a reading group, a book studied chapter by chapter | Course |
| `map-your-field` | an organisation, a lab, a funder, a course provider, a community, a job board; or a whole field | Field Map |
| `card-your-research` | your own notes, drafts, transcripts, a question you are sitting with | Research |
| `card-your-pivot` | a CV, bootcamp notes, a plan you wrote once, a journal | Cairns |
| `link-and-relate` | a card that belongs in two places, an author's shelf, a course card that bears on your research, a card that landed in the wrong place | placement in any section |

Every skill has the same shape: `SKILL.md` (what a good card is, the steps, the nevers), `reference/field-spec.md` (every field with the app's own help text, generated from the app's registry), `reference/example-pack.json` (a finished example for a made-up field, in the exact shape to produce), and `reference/check-pack.py` with `schema.json` (a check to run before importing: `python3 check-pack.py your-pack.json --deck cairn-deck.json`).

## What every skill holds to

- **Nothing invented.** Facts come from the source and say where they came from. Empty is an answer; a guess is a defect.
- **The person's fields stay as they are:** notes, exercise answers, engagement, research relevance, reading progress. They are yours, and an assistant neither fills them nor clears them.
- **Badges are set truthfully.** Maturity starts at Intuition; provenance says developed with AI when it was; evidence never ships without a limitation; a safety stance is not-assessed until someone has looked.
- **One card, one id.** Importing replaces a card whole by id, so a pack never reuses an id already in your deck unless it means to replace that card — and never mints a *new* id for something you already have, which is how one organisation becomes two cards.
- **Plain English first, the hard word second.** Acronyms are glossed the first time they appear on a card, because a stranger meets cards in any order.

## Reading the check

`check-pack.py` prints three kinds of line, and they are not the same kind of thing.

- **ERROR** — the app would reject this, or it would file the card nowhere, or it would overwrite something of yours. Fix it.
- **WARN** — a claim about your deck or about the app that you should look at and decide on. An off-list value in a suggested list is legal: every select in Cairn has an "Other…" escape and keeps what you type. A warning is not an instruction, and an assistant that rewrites your words to clear one has done the wrong thing.
- **NOTE** — a field that belongs to you. Never something for an assistant to fix.

The check ends by saying what it did **not** look at, because a clean run is not a statement that the cards are right.

## The deck file, in one paragraph

`cairn-deck.json` is `{"version": 1, "cards": [ ... ]}`. Each card is an object with an `id`, a `type` (one of the twenty-eight in `schema.json`), a `title`, the fields its type declares, and an envelope: `memberships` (where it is filed), `tags`, `source`, `track`, `relatedIds`, `references`, `myNotes`, `starred`, `completed`, `created`, `modified`. A pack is the same shape with fewer cards. Placement is by `memberships`: a course content card is `{"subUnit": "<syllabus id>"}`, a syllabus card is `{"course": "<guide id>", "unitKey": "unit-N"}`, Further Reading is `{"section": "furtherReading"}` — or, for a work on an author's shelf, `{"cast": "<principal id>"}` **alone**, where the principal's id begins `fr-member-`; Research is `{"section": "research"}` with `track` naming the frontier; the Field Map is `{"section": "fieldMap"}`; Cairns is `{"section": "cairns"}`. `link-and-relate` has the full contract.

## Which version this is

**Skills v0.2, generated against Cairn v1.11.91, 22 September 2026.**

These are revised as the app moves and as people tell us what confused them: v0.1 was tested by five readers on five real sources, and almost everything in this version comes from what they could not work out. Check back here for a newer copy — **a skill older than your app can name a field that has since moved.** Every `reference/field-spec.md` and `schema.json` says which version of Cairn it was generated against, and the check prints it too.

If something here confused you, that is worth telling us: the address is on Cairn's Contact button, or open an issue on this repository. It is the only way the next version gets better.

## Making your own skill

Copy any folder, keep the four files, change `SKILL.md`. `reference/schema.json` and the field specs are generated from the app's own registry, so they can be rebuilt whenever the app moves. If you write a skill for a card type these do not cover, or for a field these do not know, send it to the address on Cairn's Contact button or open an issue on this repository.
