# Field spec - `card-your-pivot`

*Generated from the field registry of Cairn v1.11.91 on 2026-09-22 (skills v0.2). Every line below is read from the registry, not transcribed: the help text is the app's own words, and where a value list appears it is the list the app holds. Figures about the deck carry the date they were measured and are presumed stale after it.*

**How to read the value column.** `one of:` means the app REJECTS anything else on import. `suggested:` means the list is a suggestion - every declared select in Cairn has an "Other..." escape and keeps a typed value verbatim, so an off-list value is a choice, not an error. A field marked `(array)` must be a list and is never comma-split; a field marked `(csv)` is a comma-separated string.

## The three things a Cairns pack gets wrong most often

**There is one career per person, so every run after the first is an UPDATE.** Ask whether the
person already has a Cairns section and read it before drafting. Cards with new ids do not update
the old ones - they sit beside them, and the person ends up with two Plan As and two baselines
disagreeing about which phase they are in. If they have a section, either send changed cards under
**their existing ids** (and say plainly that import replaces those cards whole), or send only what
is genuinely new.

**A date field is a claim about today.** `checkin.date` and `boundary.lastReviewed` are told "today"
in the steps below only when the person is in the room with you. Working from documents, the honest
value is the document's own date, and the pack's `source` carries it: one working deck writes it
`"Career bootcamp notes, April 2026 - carded September 2026"`. A boundary "last reviewed today", drafted from
a document written five months ago, is a false statement in a date field.

**`opportunity` the card type is not `opportunities[]` the field.** The Cairns `opportunity` card is
a route this person is considering, with a `decision`. The `opportunities[]` field on a Field Map
card is a route the ORGANISATION is offering, with a `status`. Different vocabularies, unrelated.

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

### `baseline` - Baselines

**The front of the card is `body`** - what a reader sees before opening it.

| field | type | what the app says | values |
|---|---|---|---|
| `asOf` | date | when this baseline snapshot was taken. |  |
| `body` **(front)** | textarea |  |  |
| `achievements` | textarea | notable things you have done. Free prose for ε-1; a structured sub-form (title / body / evidence link) is the ε-2 upgrade if smoke shows this reads poorly. |  |
| `strengths` | textarea |  |  |
| `constraints` | textarea | the honest list — what limits what you can plausibly do. |  |
| `motivations` | textarea |  |  |
| `links` | linklist |  |  |
| `myNotes` | textarea | your private working notes. Available on every card. Formatted text is edited with the toolbar on the card itself — if you see HTML code in this box, edit on the card instead. |  |

### `plan` - Plans

**The front of the card is `statement`** - what a reader sees before opening it.

| field | type | what the app says | values |
|---|---|---|---|
| `planLetter` | select | A = primary bet, B = fallback, Z = emergency safety net. | suggested: A, B, Z *(a value outside the list is legal - the app has an "Other..." escape and keeps what you type)* |
| `statement` **(front)** | textarea |  |  |
| `routes` | textarea | the paths this plan takes — e.g. Plan A layers, or a single principal route. |  |
| `targetOrgs` | textarea | places you are aiming at. Cross-link individual institutions via Related cards (relatedIds) — no typed link field per Scope ruling. |  |
| `switchTriggers` | textarea | "I move to Plan B if X hasn't happened by Y" — the trip-wires that flip you to the fallback. |  |
| `status` | select |  | suggested: active, parked, retired, superseded *(a value outside the list is legal - the app has an "Other..." escape and keeps what you type)* |
| `amendments` | textarea | the running log of substantive edits, each anchored to a check-in — one row per amendment (date · check-in · one-line summary · prose). Text for ε-1; structured sub-form arrives at ε-2 if smoke reads poorly. NEVER edit silently — appending here IS the plan's story. |  |
| `myNotes` | textarea | your private working notes. Available on every card. Formatted text is edited with the toolbar on the card itself — if you see HTML code in this box, edit on the card instead. |  |

### `phase` - Phases

**The front of the card is `purpose`** - what a reader sees before opening it.

| field | type | what the app says | values |
|---|---|---|---|
| `order` | number | display order across phases — low to high; drives the spine sort in the Phases bucket. |  |
| `timeframe` | text |  |  |
| `purpose` **(front)** | textarea |  |  |
| `successCriteria` | textarea | the specific outcomes that would prove this phase succeeded. |  |
| `status` | select |  | suggested: upcoming, current, closed *(a value outside the list is legal - the app has an "Other..." escape and keeps what you type)* |
| `retrospective` | textarea | filled at phase close — what actually happened, what shifted, what carries forward. |  |
| `myNotes` | textarea | your private working notes. Available on every card. Formatted text is edited with the toolbar on the card itself — if you see HTML code in this box, edit on the card instead. |  |

### `goal` - Goals

**The front of the card is `statement`** - what a reader sees before opening it.

| field | type | what the app says | values |
|---|---|---|---|
| `statement` **(front)** | textarea |  |  |
| `phaseId` | text | the phase this goal belongs to — enter the phase card's id (structured phase-picker is an ε-2 nicety). |  |
| `targetDate` | date | optional — cadence-goals without a fixed date exist; the due-soon strip ignores dateless goals. |  |
| `targetTime` | time | optional — consumed by the .ics export at ε-2. All-day event when empty. |  |
| `status` | select |  | suggested: not-started, in-progress, done, dropped, carried-over *(a value outside the list is legal - the app has an "Other..." escape and keeps what you type)* |
| `evidence` | textarea |  |  |
| `outcome` | textarea | the short retro note filled at close. |  |
| `myNotes` | textarea | your private working notes. Available on every card. Formatted text is edited with the toolbar on the card itself — if you see HTML code in this box, edit on the card instead. |  |

### `opportunity` - Opportunities

**The front of the card is `role`** - what a reader sees before opening it.

| field | type | what the app says | values |
|---|---|---|---|
| `org` | text |  |  |
| `role` **(front)** | text |  |  |
| `link` | text |  |  |
| `deadline` | date |  |  |
| `deadlineTime` | time | optional — consumed by the .ics export at ε-2. |  |
| `sourceBoard` | text |  |  |
| `decision` | select | reasoned skip-decisions prevent regret AND silent drift. context-only = kept as reference, not being pursued. | suggested: pursuing, applied, skipped, later, expired, context-only *(a value outside the list is legal - the app has an "Other..." escape and keeps what you type)* |
| `reasoning` | textarea | REQUIRED when decision is set — why this decision, in your terms. |  |
| `outcome` | textarea |  |  |
| `myNotes` | textarea | your private working notes. Available on every card. Formatted text is edited with the toolbar on the card itself — if you see HTML code in this box, edit on the card instead. |  |

### `uncertainty` - Uncertainties

**The front of the card is `question`** - what a reader sees before opening it.

| field | type | what the app says | values |
|---|---|---|---|
| `question` **(front)** | text |  |  |
| `whyItMatters` | textarea |  |  |
| `cheapestTest` | textarea | the smallest experiment that would move you off this uncertainty — the bootcamp Day-3 discipline. |  |
| `testStatus` | select |  | suggested: open, testing, resolved, overtaken *(a value outside the list is legal - the app has an "Other..." escape and keeps what you type)* |
| `result` | textarea |  |  |
| `resolvedDate` | date |  |  |
| `myNotes` | textarea | your private working notes. Available on every card. Formatted text is edited with the toolbar on the card itself — if you see HTML code in this box, edit on the card instead. |  |

### `boundary` - Boundaries

**The front of the card is `statement`** - what a reader sees before opening it.

| field | type | what the app says | values |
|---|---|---|---|
| `statement` **(front)** | textarea |  |  |
| `why` | textarea | the reasoning that made this boundary matter — protects it from casual erosion. |  |
| `status` | select |  | suggested: holding, wobbling, broken, retired *(a value outside the list is legal - the app has an "Other..." escape and keeps what you type)* |
| `lastReviewed` | date |  |  |
| `myNotes` | textarea | your private working notes. Available on every card. Formatted text is edited with the toolbar on the card itself — if you see HTML code in this box, edit on the card instead. |  |

### `checkin` - Check-ins

**The front of the card is `whatMoved`** - what a reader sees before opening it.

| field | type | what the app says | values |
|---|---|---|---|
| `date` | date |  |  |
| `periodCovered` | text | optional — the span this check-in reflects on. |  |
| `whatMoved` **(front)** | textarea |  |  |
| `whatStalled` | textarea |  |  |
| `driftCheck` | textarea | Does the plan still describe what I'm actually doing? If not — should the plan change, or should I? |  |
| `amendmentsMade` | textarea | the substantive plan edits this check-in prompted — mirror into the plan card's amendments log. |  |
| `sustainability` | textarea | a first-class field per the April plan's non-negotiables. Notes on what supports or drains you. |  |
| `nextPriority` | textarea |  |  |
| `myNotes` | textarea | your private working notes. Available on every card. Formatted text is edited with the toolbar on the card itself — if you see HTML code in this box, edit on the card instead. |  |

---

*This file is generated. If your Cairn is newer than Cairn v1.11.91, a field here may have moved; check the skills folder on the repository for a newer copy.*