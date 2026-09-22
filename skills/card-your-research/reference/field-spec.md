# Field spec - `card-your-research`

*Generated from the field registry of Cairn v1.11.91 on 2026-09-22 (skills v0.2). Every line below is read from the registry, not transcribed: the help text is the app's own words, and where a value list appears it is the list the app holds. Figures about the deck carry the date they were measured and are presumed stale after it.*

**How to read the value column.** `one of:` means the app REJECTS anything else on import. `suggested:` means the list is a suggestion - every declared select in Cairn has an "Other..." escape and keeps a typed value verbatim, so an off-list value is a choice, not an error. A field marked `(array)` must be a list and is never comma-split; a field marked `(csv)` is a comma-separated string.

## The two things a research pack gets wrong most often

**The frontier may already exist.** Before naming one, ask for the person's list of research topics,
or for the deck. A topic whose name they have not settled cannot be matched by title, and a second
card for the same direction is worse than a wrong name: it splits the working set in two. If the
notes reserve the naming decision, use their provisional words and add a `question` card recording
that the name is theirs to settle.

**`track` files the card; `theFrontier` only renders a line.** `track` = the frontier card's title
exactly, on every card in the working set. `theFrontier` is a thesis-only display field; on any
other type the app stores it and shows nothing.

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

### `frontier` - Research topics

**The front of the card is `title`** - what a reader sees before opening it.

| field | type | what the app says | values |
|---|---|---|---|
| `title` **(front)** | text |  |  |
| `label` | text | An optional short name for the spine. Leave blank to show the full Topic name. The full name always shows on the topic's head. |  |
| `order` | number | where this sits in its section's running order, a number, low to high. |  |
| `description` | textarea |  |  |
| `myNotes` | textarea | your private working notes. Available on every card. Formatted text is edited with the toolbar on the card itself — if you see HTML code in this box, edit on the card instead. |  |

### `thesis` - Theses

**The front of the card is `definition`** - what a reader sees before opening it.

| field | type | what the app says | values |
|---|---|---|---|
| `statement` | textarea |  |  |
| `theFrontier` | text |  |  |
| `definition` **(front)** | textarea |  |  |
| `anchor` | textarea | a concrete example or moment that makes the idea stick, where it "lands" for you. A Story card often serves as the anchor, a worked scene you can point to. |  |
| `metaphor` | text | a short image or comparison in one line, the kind that makes the idea easier to hold and recall. |  |
| `whyItMatters` | textarea |  |  |
| `researchRelevance` | textarea | how this card connects to your research, if it does. Optional; leave blank for pure study cards. It only shows on the card when filled. |  |
| `evidenceFor` | textarea |  |  |
| `openProblems` | textarea |  |  |
| `maturity` | select | how settled this claim is. *Intuition*, a hunch you have not tested. *Developing*, taking shape but still moving. *Evidenced*, backed by something you would defend. *Contested*, a live disagreement you are holding open. Shows as a badge. | suggested: Intuition, Developing, Evidenced, Contested *(a value outside the list is legal - the app has an "Other..." escape and keeps what you type)* |
| `readingStatus` | select | how far you have engaged with the underlying source. *Unread*. *Skimmed*. *Read*. *Verified*, you have checked it closely. *Original*, it is your own work. | suggested: Unread, Skimmed, Read, Verified, Original *(a value outside the list is legal - the app has an "Other..." escape and keeps what you type)* |
| `provenance` | text | where this came from. *Own work*, yours. *Developed with AI*, worked out with an AI assistant. *From the literature*, drawn from others' work. Keeps attribution honest. |  |
| `myNotes` | textarea | your private working notes. Available on every card. Formatted text is edited with the toolbar on the card itself — if you see HTML code in this box, edit on the card instead. |  |

### `metric` - Metrics

**The front of the card is `definition`** - what a reader sees before opening it.

| field | type | what the app says | values |
|---|---|---|---|
| `whatItMeasures` | textarea |  |  |
| `howCalculated` | textarea |  |  |
| `definition` **(front)** | textarea |  |  |
| `anchor` | textarea | a concrete example or moment that makes the idea stick, where it "lands" for you. A Story card often serves as the anchor, a worked scene you can point to. |  |
| `whyItMatters` | textarea |  |  |
| `researchRelevance` | textarea | how this card connects to your research, if it does. Optional; leave blank for pure study cards. It only shows on the card when filled. |  |
| `validityConcerns` | textarea | reasons to be cautious about what the metric really captures. |  |
| `maturity` | select | how settled this claim is. *Intuition*, a hunch you have not tested. *Developing*, taking shape but still moving. *Evidenced*, backed by something you would defend. *Contested*, a live disagreement you are holding open. Shows as a badge. | suggested: Intuition, Developing, Evidenced, Contested *(a value outside the list is legal - the app has an "Other..." escape and keeps what you type)* |
| `readingStatus` | select | how far you have engaged with the underlying source. *Unread*. *Skimmed*. *Read*. *Verified*, you have checked it closely. *Original*, it is your own work. | suggested: Unread, Skimmed, Read, Verified, Original *(a value outside the list is legal - the app has an "Other..." escape and keeps what you type)* |
| `provenance` | text | where this came from. *Own work*, yours. *Developed with AI*, worked out with an AI assistant. *From the literature*, drawn from others' work. Keeps attribution honest. |  |
| `myNotes` | textarea | your private working notes. Available on every card. Formatted text is edited with the toolbar on the card itself — if you see HTML code in this box, edit on the card instead. |  |

### `evidence` - Evidence

**The front of the card is `finding`** - what a reader sees before opening it.

| field | type | what the app says | values |
|---|---|---|---|
| `finding` **(front)** | textarea |  |  |
| `sourceRef` | text | the underlying source in citation form, authors, venue, year. |  |
| `strength` | textarea |  |  |
| `limitations` | textarea |  |  |
| `supportsThesis` | textarea | which thesis this bears on, and how it strengthens or complicates it. |  |
| `whyItMatters` | textarea |  |  |
| `researchRelevance` | textarea | how this card connects to your research, if it does. Optional; leave blank for pure study cards. It only shows on the card when filled. |  |
| `maturity` | select | how settled this claim is. *Intuition*, a hunch you have not tested. *Developing*, taking shape but still moving. *Evidenced*, backed by something you would defend. *Contested*, a live disagreement you are holding open. Shows as a badge. | suggested: Intuition, Developing, Evidenced, Contested *(a value outside the list is legal - the app has an "Other..." escape and keeps what you type)* |
| `readingStatus` | select | how far you have engaged with the underlying source. *Unread*. *Skimmed*. *Read*. *Verified*, you have checked it closely. *Original*, it is your own work. | suggested: Unread, Skimmed, Read, Verified, Original *(a value outside the list is legal - the app has an "Other..." escape and keeps what you type)* |
| `sourceType` | select |  | suggested: Peer-reviewed study, Preprint, Industry research, Institutional report, Journalism, Essay or commentary, Primary document, Original observation *(a value outside the list is legal - the app has an "Other..." escape and keeps what you type)* |
| `provenance` | text | where this came from. *Own work*, yours. *Developed with AI*, worked out with an AI assistant. *From the literature*, drawn from others' work. Keeps attribution honest. |  |
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

### `tension` - Tensions

**The front of the card is `crux`** - what a reader sees before opening it.

| field | type | what the app says | values |
|---|---|---|---|
| `partyA` | text | the two sides of the disagreement, a short name or label for each. |  |
| `claimA` | textarea | each side's position, in their own terms. |  |
| `partyB` | text | the two sides of the disagreement, a short name or label for each. |  |
| `claimB` | textarea | each side's position, in their own terms. |  |
| `crux` **(front)** | textarea | the single point the two sides actually disagree on, the heart of it, not the whole debate. |  |
| `whereItAppears` | text | the units, readings, or research topics where this tension shows up. |  |
| `myNotes` | textarea | your private working notes. Available on every card. Formatted text is edited with the toolbar on the card itself — if you see HTML code in this box, edit on the card instead. |  |

### `framework` - Frameworks

**The front of the card is `definition`** - what a reader sees before opening it.

| field | type | what the app says | values |
|---|---|---|---|
| `definition` **(front)** | textarea |  |  |
| `components` | textarea | the parts the framework breaks into, its named elements or steps. One formatted block of prose, not a list field. |  |
| `whenToUse` | textarea |  |  |
| `anchor` | textarea | a concrete example or moment that makes the idea stick, where it "lands" for you. A Story card often serves as the anchor, a worked scene you can point to. |  |
| `metaphor` | text | a short image or comparison in one line, the kind that makes the idea easier to hold and recall. |  |
| `whyItMatters` | textarea |  |  |
| `researchRelevance` | textarea | how this card connects to your research, if it does. Optional; leave blank for pure study cards. It only shows on the card when filled. |  |
| `myNotes` | textarea | your private working notes. Available on every card. Formatted text is edited with the toolbar on the card itself — if you see HTML code in this box, edit on the card instead. |  |

### `story` - Stories

**The front of the card is `metaphor`** - what a reader sees before opening it.

| field | type | what the app says | values |
|---|---|---|---|
| `metaphor` **(front)** | text | a short image or comparison in one line, the kind that makes the idea easier to hold and recall. |  |
| `body` | textarea |  |  |
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

---

*This file is generated. If your Cairn is newer than Cairn v1.11.91, a field here may have moved; check the skills folder on the repository for a newer copy.*