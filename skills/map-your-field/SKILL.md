---
name: map-your-field
description: Turn an organisation's or a platform's own web pages into a Cairn Field Map card (institution or platform), with badges left for the person to judge, a provenance line naming the pages read, and one dated opportunities row per live route in. Use when someone asks to add an organisation, a lab, a funder, a course provider, a community or a job board to their Cairn deck, or to map a field.
---

# Map your field

You are drafting cards for Cairn, a study companion that keeps everything a person is learning in one local file. This skill makes **Field Map** cards: one card per organisation (`institution`) or per place where careers and courses happen (`platform`). The person imports the file you produce; nothing you write reaches their deck until they do, and they read every card first.

## What a good card is

A Field Map card is the facts a newcomer needs and the judgement calls a newcomer cannot make, kept apart. The facts come from the organisation's own pages and say where they came from. The judgement calls (a safety stance, an openness rating) are **left as `not-assessed` unless the pages give evidence**, and when you do set one, the note beside it quotes the evidence in the organisation's own words. The card is honest about what it does not know: an empty `city` is an answer, `not-stated` is a finding, and a deadline with no year is `null` with a sentence saying why.

## Before you start: does the person already have this card?

Ask for their deck file, or ask whether they have carded this organisation before. **A card you write under a new id does not update theirs — it lands beside it**, and they end up with two cards for one organisation, one of them carrying their notes and their star. Two sensible slugs of the same name (`inst-tarbell-center`, `inst-tarbell-center-for-ai-journalism`) are all it takes. If they have a card, send yours under **their id** and say plainly in your reply that importing replaces that card whole. If you have their deck, `check-pack.py --deck` will tell you; if you do not, ask.

## Do this, in order

1. **Read the organisation's own pages** — at least About, and Careers / Jobs / Opportunities / Programmes; Locations or Contact if there is one. Read the pages themselves rather than a description of them, and do not take any fact on the card from a third party. If a page cannot be read, say so in `provenance` and leave the fields it would have filled empty.
2. **Decide `institution` or `platform`.** An institution does the work (a lab, an institute, a funder, a company, a government body). A platform is where careers and courses happen (a course provider, a community, a job board, a tool). If it is both, it is an institution.
3. **Fill the fields** in `reference/field-spec.md`, in the person's language and in short plain sentences. `blurb` is one line. `details` is a paragraph a stranger would thank you for. `topics` is what the organisation is ABOUT and has a real 27-value vocabulary in the spec — use it, because an off-list near-duplicate ("AI policy & politics" beside the listed "AI governance & policy") stops the card grouping with its peers. `activityBucket` is what it DOES, and its list grows from the deck: the spec prints the eighteen one working deck holds. `geography` is a comma-separated string, not a list.
4. **Write one `opportunities` row per route in** — job, fellowship, course, grant, event. Each row carries the date you saw it (`asOf`), a `status` from the hard list, and its `deadline` exactly as printed or `null`. The Open opps column counts `open`, `rolling` and `upcoming`, so a wrong status is a wrong number on the person's screen. **A route whose published deadline has passed but which the organisation still lists is `closed`, with that fact written into `eligibility`** — say what you saw. Closed routes may stay as rows if they show what the organisation offers in a normal year.
5. **Write the `provenance` line:** which pages, read when, in which language. This is the card's honesty; never leave it empty. **`checkedOn` is the date you did this work** — it is required, and it is the one date on the card that is about you rather than about them.
6. **Say where it is, if it says where it is.** The simple shape is on the card: `city`, `country`, `latlng` to one decimal, `approxLocation: true` when only the city is known — **that is a complete answer, and it puts a pin on the map**; 183 of the 219 live Field Map cards that carry no `locations[]` list have a pin exactly this way. Use the `locations[]` list only for an organisation with several named sites. **An organisation that names no place gets no pin: leave both empty.** A registered address is not a place of work, and a coordinate you remembered rather than read is an invented fact.
7. **Set `depth`:** `stub` when you have the blurb and little else, `partial`, `full` when the pages answered most of the card. It is a badge on the type row, and it tells the person where to go back to.
8. **Set the envelope:** `memberships: [{"section": "fieldMap"}]` (always; a card may carry more if a course also names this organisation), a stable `id` (`inst-` or `plat-` plus a slug), and `tags` — the deck's own convention is `field-map` plus the depth (`stub` / `full`) plus anything you would filter on later.
9. **Output one JSON file** shaped like `reference/example-pack.json`: `{"version": 1, "cards": [ ... ]}`. Many cards in one file is fine.
10. **Run the check:** `python3 reference/check-pack.py your-pack.json --deck cairn-deck.json` (drop `--deck` if you do not have their deck, and say in your reply that the id and duplicate checks did not run). Fix the errors. **Read the warnings and decide** — they are claims about the app, not commands; a warning that says an off-list value is not in the suggested list is telling you the value is legal and unusual, not that it is wrong. Lines marked NOTE are the person's own fields and are never yours to clear.
11. **Tell the person what you could not verify**, card by card, in your reply, not on the cards.

## Never

- Never invent a figure, a date, a stance, a coordinate or a person. Empty is an answer; a guess is a defect. **If a check ever seems to ask you for a fact you do not have, the check is wrong and you say so in your reply.**
- Never set `safety` to `none-found` unless you searched the pages and found nothing; `not-assessed` is for when you have not looked. The two mean different things and the map colours them differently. The spec defines all five values in one sentence each.
- Never fill `engagement`, `myNotes` or `researchRelevance` for the person. They are theirs.
- Never put a private contact address in `contacts`; public addresses and forms only.
- Never reuse an `id` that exists in the person's deck unless they asked you to replace that card, and never mint a new id for an organisation they already have. Importing replaces a card whole.
- Never write anything on a card that the organisation could not read over your shoulder.

## When the person gives you a whole field at once

Ask for the list of organisations, or the page that lists them, and work in batches of five to ten. Keep one `activityBucket` list and one `topics` list across the batch, and tell the person which buckets you used so they can rename them once in the app rather than card by card. Suggest they import one small batch first, look at the map and the table, and then send the rest.

## Files in this skill

- `reference/field-spec.md`: every field, its type, its options and the app's own help text; the vocabularies, including the ones that only exist in a deck.
- `reference/example-pack.json`: one finished institution card, for a made-up organisation, in the exact shape to produce.
- `reference/check-pack.py` with `schema.json`: the check to run before handing over a file.
