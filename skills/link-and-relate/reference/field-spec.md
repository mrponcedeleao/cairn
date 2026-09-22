# Field spec - `link-and-relate`

*Generated from the field registry of Cairn v1.11.91 on 2026-09-22 (skills v0.2). Every line below is read from the registry, not transcribed: the help text is the app's own words, and where a value list appears it is the list the app holds. Figures about the deck carry the date they were measured and are presumed stale after it.*

**How to read the value column.** `one of:` means the app REJECTS anything else on import. `suggested:` means the list is a suggestion - every declared select in Cairn has an "Other..." escape and keeps a typed value verbatim, so an off-list value is a choice, not an error. A field marked `(array)` must be a list and is never comma-split; a field marked `(csv)` is a comma-separated string.

## The placement contract, as the app reads it

**A work on a principal's shelf carries `{"cast": "<principal id>"} ALONE.** The app implies Further
Reading membership from the cast id (`matchesSection`), and **0 of 2,122 live cards carry both** that
and a bare `{"section": "furtherReading"}`. Adding the section membership beside the cast one is an
error, not redundancy.

**A principal's id MUST begin `fr-member-`.** The implication above is written against that prefix
literally: `m.cast.startsWith('fr-member-')`. A principal called `member-ada-lovelace` gathers
nothing and its works land nowhere, silently. All five live principals use the prefix.

**A shelf GATHERS by `source`.** The principal's `resources` rows carry `sourceMatch`; each work's
card carries the matching string in `source`; the app matches them by bidirectional containment. A
work with an empty `source` sits under the principal and outside every row of the shelf. `source` is
not course-only: all 171 live Further Reading cards carry one.

**`title` is the shelf's name; `castMatch` is the cast card's title EXACTLY.** They are not the same
string and were never meant to be. The shelf's title takes the person-or-organisation form -
"Ada Lovelace / Analytical Engine Society" - while `castMatch` must equal the cast card's
title character for character, because that is what pairs them.

## A principal who is not in the deck yet

Step 1 says never guess an id, and a new principal has none. Mint one, in this order:

1. Write the `sectionMember` card first: `id` = `fr-member-<surname>`, `sectionRoot: furtherReading`,
   `title` = the person or person/organisation, `castMatch` = the cast card's title exactly, `order`
   = the next free number (ask, or leave it out and say so), `description` = who they are and why
   they are here, and one `resources` row per work with a short distinctive `sourceMatch`.
2. Then the `cast` card for the person, `{"cast": "<that id>"}`, title exactly equal to `castMatch`.
3. Then each work as a `library` card, `{"cast": "<that id>"}`, `source` = the string that matches
   its `resources` row.
4. Send all of it in ONE pack, so the ids resolve when the person imports it.

## Placement - where a card is filed

A membership is one of these shapes. A section value outside this list files the card nowhere, silently - matchesSection is exact string equality.

- A membership is one of: `section`, `subUnit`, `course`, `unitKey`, `cast`.
- `section` is one of: `cairns`, `fieldMap`, `furtherReading`, `research`.
- Course cards do NOT use {section: course}: a content card carries {subUnit: <syllabus card id>} and a syllabus card carries {course: <guide id>, unitKey: unit-N}.
- A work on a principal's shelf carries {cast: <principal id>} ALONE. The app implies Further Reading membership from a cast id beginning fr-member- (matchesSection), and 0 of 2,122 live cards carry both that and {section: furtherReading}.

## The envelope - fields every card can carry

These are not declared by a card type; they are the card's frame. The first group is on every card.

| field | what it is |
|---|---|
| `id` | the card's own id - unique in the deck; import replaces a card whole by id |
| `type` | one of the types below |
| `title` | the card's name, shown everywhere |
| `memberships` | where the card is filed - see sections below |
| `tags` | free tags; filters and search read them |
| `source` | the reading, course or work this card came from; the string a syllabus resources row's sourceMatch clusters against |
| `track` | for research cards, the frontier's title - this is what files the card under its frontier |
| `unit` | legacy free-text unit label; empty on every live Field Map card |
| `relatedIds` | list of card ids; Related cards render when BOTH cards point at each other |
| `references` | list of reference strings |
| `starred` | the person's star |
| `completed` | the person's completion mark |
| `created` | ISO timestamp |
| `modified` | ISO timestamp |

### Placement and structure

| field | what it is |
|---|---|
| `sectionRoot` | on a guide, the section it heads (cairns | course | fieldMap | research | furtherReading). A frontier card carries sectionRoot: research and a Further Reading principal carries sectionRoot: furtherReading; the registry declares the key on guide only and fixes the value for the other two. |
| `courseId` | on a courseUnit, the course guide's id |
| `unitKey` | on a courseUnit, unit-1, unit-2 ... |
| `subLabel` | on a syllabus card, "4.4" |
| `order` | sort order within a section or unit |
| `castMatch` | on a Further Reading principal, the cast card's title EXACTLY - this is what pairs the shelf with the person's cast card |
| `locations` | Field Map: list of sites, each {city, country, latlng, approxLocation, note} |
| `latlng` | Field Map: card-level coordinates; the map falls back to these when locations[] is absent |
| `approxLocation` | Field Map: true when the pin is a city-level approximation |
| `learningOutcomes` | course structure cards |
| `responseTemplate` | exercise scaffolding |

### Declared on some types, inert on the rest

These keys are declared by SOME types and not by others. The app stores whatever you write, and renders the field only on a type that declares it: a maturity badge on a concept card is data with no row on the form and no line on the face. Write them only on the types listed.

| field | declared on |
|---|---|
| `readingStatus` | thesis, metric, evidence |
| `maturity` | thesis, metric, evidence |
| `theFrontier` | thesis |
| `sourceType` | evidence |
| `provenance` | thesis, metric, evidence, institution, platform |
| `researchRelevance` | concept, cast, framework, library, question, thesis, metric, evidence, institution, platform |
| `myNotes` | 26 of the 28 types |
| `resourceProgress` | no type declares it; it holds the person's own review and flashcard ticks and an assistant never writes it |

### The person's own fields - never written by an assistant

These belong to the person. An assistant leaves them exactly as they are - absent on a new card, untouched on an existing one. The check prints them as NOTES, never as something to fix.

`myNotes` · `userResponse` · `engagement` · `researchRelevance` · `resourceProgress`

## The types this skill writes

### `sectionMember` - Section members

**The front of the card is `title`** - what a reader sees before opening it.

| field | type | what the app says | values |
|---|---|---|---|
| `resources` | resources | the readings, talks, papers, and prompts by or about this Further Reading principal. Title is the only required field; everything else can be left blank. Reorder via the ↑/↓ buttons. The source-match field at the bottom of each block links a reading to a library card; leave it blank to match by title. |  |
| `description` | textarea | who this Further Reading principal is and why they're here — free prose. Renders as the head of the principal's view when non-empty (once the principal is openable). |  |
| `order` | number | where this principal sits in the Further Reading running order, a number, low to high. |  |

### `cast` - Cast

**The front of the card is `role`** - what a reader sees before opening it.

| field | type | what the app says | values |
|---|---|---|---|
| `disambiguation` | text | a short tag to tell this person apart from others, affiliation, role, or the claim to note. |  |
| `photo` | text |  |  |
| `role` **(front)** | text |  |  |
| `stance` | textarea | where they stand on the questions that matter, whether in your research or a course topic. |  |
| `keyWorks` | linklist | notable things they have made or written, a book, a paper, a talk, a project; label plus optional link per row. |  |
| `anchor` | textarea | a concrete example or moment that makes the idea stick, where it "lands" for you. A Story card often serves as the anchor, a worked scene you can point to. |  |
| `whyTheyMatter` | textarea |  |  |
| `researchRelevance` | textarea | how this card connects to your research, if it does. Optional; leave blank for pure study cards. It only shows on the card when filled. |  |
| `myNotes` | textarea | your private working notes. Available on every card. Formatted text is edited with the toolbar on the card itself — if you see HTML code in this box, edit on the card instead. |  |

### `library` - Library

**The front of the card is `summary`** - what a reader sees before opening it.

| field | type | what the app says | values |
|---|---|---|---|
| `author` | text |  |  |
| `year` | text |  |  |
| `mediaType` | select |  | suggested: Book, Paper, Article, Talk *(a value outside the list is legal - the app has an "Other..." escape and keeps what you type)* |
| `status` | select |  | suggested: To read, Reading, Read *(a value outside the list is legal - the app has an "Other..." escape and keeps what you type)* |
| `whyItMatters` | textarea |  |  |
| `researchRelevance` | textarea | how this card connects to your research, if it does. Optional; leave blank for pure study cards. It only shows on the card when filled. |  |
| `summary` **(front)** | textarea |  |  |
| `myNotes` | textarea | your private working notes. Available on every card. Formatted text is edited with the toolbar on the card itself — if you see HTML code in this box, edit on the card instead. |  |

### `question` - Open Questions

**The front of the card is `question`** - what a reader sees before opening it.

| field | type | what the app says | values |
|---|---|---|---|
| `question` **(front)** | textarea |  |  |
| `whyItMatters` | textarea |  |  |
| `researchRelevance` | textarea | how this card connects to your research, if it does. Optional; leave blank for pure study cards. It only shows on the card when filled. |  |
| `currentThinking` | textarea |  |  |
| `status` | select |  | suggested: Open, Sitting with, Provisionally answered *(a value outside the list is legal - the app has an "Other..." escape and keeps what you type)* |
| `myNotes` | textarea | your private working notes. Available on every card. Formatted text is edited with the toolbar on the card itself — if you see HTML code in this box, edit on the card instead. |  |

### `syllabus` - Syllabus

**The front of the card is `intro`** - what a reader sees before opening it.

| field | type | what the app says | values |
|---|---|---|---|
| `intro` **(front)** | textarea |  |  |
| `duration` | text |  |  |
| `resources` | resources | the readings, talks, papers, and prompts that make up this sub-unit. Title is the only required field; everything else can be left blank. Reorder via the ↑/↓ buttons. The source-match field at the bottom of each block links the resource to a library card; leave it blank to match by title. |  |
| `myNotes` | textarea | your private working notes. Available on every card. Formatted text is edited with the toolbar on the card itself — if you see HTML code in this box, edit on the card instead. |  |

### `guide` - Guides

**The front of the card is `blurb`** - what a reader sees before opening it.

| field | type | what the app says | values |
|---|---|---|---|
| `blurb` **(front)** | text |  |  |
| `description` | textarea |  |  |
| `howToUse` | textarea | plain instructions for a reader, and the suggested way to build cards with AI. Make these yours, notes or edits that help you are part of customising your own Cairn. |  |
| `aiWorkflow` | textarea | plain instructions for a reader, and the suggested way to build cards with AI. Make these yours, notes or edits that help you are part of customising your own Cairn. |  |
| `links` | linklist |  |  |
| `curriculum` | text | used when this guide is the course guide (Section root 'course') — it gives the course its name. The guide's substance (how-to, AI workflow, links) lives in its other fields. |  |
| `sectionRoot` | text | which section this guide heads (cairns, course, fieldMap, research, or furtherReading). The guide both creates the section and introduces it. One guide per section. |  |
| `cadenceDays` | number | how often you intend to check in (days) — drives the staleness colour on the Cairns band. Only consumed by the Cairns section; other guides can leave it blank. |  |
| `colour` | color | section accent — overrides the default. Used by the spine curriculum / section header, the panel label, and the masthead deck-name. Click Reset to clear the override and fall back to the section's default colour. |  |
| `myNotes` | textarea | your private working notes. Available on every card. Formatted text is edited with the toolbar on the card itself — if you see HTML code in this box, edit on the card instead. |  |

---

*This file is generated. If your Cairn is newer than Cairn v1.11.91, a field here may have moved; check the skills folder on the repository for a newer copy.*