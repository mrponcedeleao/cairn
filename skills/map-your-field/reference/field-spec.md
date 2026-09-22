# Field spec - `map-your-field`

*Generated from the field registry of Cairn v1.11.91 on 2026-09-22 (skills v0.2). Every line below is read from the registry, not transcribed: the help text is the app's own words, and where a value list appears it is the list the app holds. Figures about the deck carry the date they were measured and are presumed stale after it.*

**How to read the value column.** `one of:` means the app REJECTS anything else on import. `suggested:` means the list is a suggestion - every declared select in Cairn has an "Other..." escape and keeps a typed value verbatim, so an off-list value is a choice, not an error. A field marked `(array)` must be a list and is never comma-split; a field marked `(csv)` is a comma-separated string.

## The three things a Field Map pack gets wrong most often

**A pin does not need `locations[]`.** The map falls back to the card-level `latlng`
(`fieldMapSites`, one function, one place): 219 of 247 live Field Map cards carry no `locations[]`
and 183 of them have a pin. `city` + `country` + `latlng` on the card is a complete answer. An
organisation that names no place gets no pin, and that is the right card - never invent a location
to satisfy a check.

**`geography` is a comma-separated STRING.** The registry declares `valueShape: 'csv'`; 247 of 247
live cards hold a string and none holds a list. A list survives import and is rewritten to a string
the first time the person saves that card.

**`topics` has a real vocabulary** - it is the one Field Map multiselect whose options the app
hard-codes. The 27 values are listed below. Off-list values are legal and round-trip verbatim, but a
value that is a near-duplicate of a listed one ("AI policy & politics" beside "AI governance &
policy") does not group with its peers on the Topics axis, which is what the field is for.

**`safety`, in one sentence each.** `mission` = safety IS the work, in its own statement of what it
does. `programme` = it does safety work as one strand among others. `partial` = safety appears in
some of what it does without being a declared strand. `none-found` = you looked at its own pages and
found none, in the languages you searched - a finding. `not-assessed` = you have not looked. The
badge colours the pin on the map, so the difference between the last two is visible.

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

### `institution` - Institutions

**The front of the card is `blurb`** - what a reader sees before opening it.

| field | type | what the app says | values |
|---|---|---|---|
| `blurb` **(front)** | text |  |  |
| `orgType` | text | the kind of organisation it is (lab, funder, nonprofit…). Choose "Other…" to add a type the list does not have yet; it joins the list next time. | one of: commercial, nonprofit, academic, government, intergovernmental, network/community **(the app rejects anything else)** |
| `orgTypeNote` | text | why this type was chosen when the organisation does not say so itself, and any part of the old compound description that the sector alone does not carry — an insurer, a media company. orgType is always filled in, so this is where an author judgement is declared instead of being left to look like a stated fact. |  |
| `geography` | multiselect (csv) | the countries or regions it mainly operates in. Many values allowed — tap to toggle. Choose "Other…" to add one the list does not have yet; that box alone is comma-separated, so several can be typed at once. | *(the suggestions are whatever the deck already holds; anything is legal)* |
| `activityBucket` | text | what this org or tool mainly does, its category in the Field Map taxonomy. Choose "Other…" to add a category the list does not have yet; it joins the list next time. |  |
| `details` | textarea |  |  |
| `frontierRelevance` | multiselect (csv) | which research frontier(s) this org or tool touches. Many values allowed — tap to toggle; the "Other…" box alone is comma-separated, so several can be typed at once. This is only the research cross-link; to also show it in a course unit, set that separately in placement. | *(the suggestions are whatever the deck already holds; anything is legal)* |
| `topics` | multiselect (array) | what this organisation is ABOUT — the subject, not the sector or the activity. Many values allowed. Choose "Other…" to add a subject the list does not have yet. | suggested: technical safety & alignment, interpretability, evaluations & red-teaming, multi-agent systems & agents, AI for science, AI governance & policy, compute & hardware governance, international security & geopolitics, military & autonomous systems, biosecurity, cybersecurity, law, AI ethics & philosophy, fairness, bias & discrimination, privacy & surveillance, information integrity, economics & labour, education & learning, human–AI interaction, accessibility & assistive technology, public understanding, language access & multilingual AI, AI welfare & digital minds, consciousness science, forecasting & measurement, existential risk, wellbeing & mental health *(a value outside the list is legal - the app has an "Other..." escape and keeps what you type)* |
| `city` | text | the city it mainly operates from. Leave empty if it has no single base — empty is a legitimate answer here, not a gap. |  |
| `country` | text | the country it mainly operates from. Leave empty if not stated on its own pages. |  |
| `region` | select | the broad region, chosen by hand. Not derived from Country — an organisation with no single country can still be Distributed / global, and an unstated country stays empty rather than being guessed. | suggested: Africa, Australia, China, Continental Europe, Distributed / global, Gulf States, India, Israel, Japan, Latin America, North America, Russia, Singapore, South Korea, Taiwan, UK & Ireland *(a value outside the list is legal - the app has an "Other..." escape and keeps what you type)* |
| `safety` | select | how seriously it treats safety. "none-found" means none found BY US, in the languages we searched, on the pages it publishes — it is a finding. "not-assessed" means we have not looked. Never use one for the other. | one of: mission, programme, partial, none-found, not-assessed **(the app rejects anything else)** |
| `safetyNote` | text | one line of evidence for the posture above, in its own terms. |  |
| `openness` | select | what it puts into the commons and whether you can reuse it. | one of: open, partial, closed, not-stated **(the app rejects anything else)** |
| `opennessNote` | text | what specifically, and under what licence — open weights, open datasets, CC BY-SA, paywalled, members-only. |  |
| `workMode` | select | how it works across the organisation. A specific role may differ — that is recorded per opportunity. | one of: onsite, hybrid, remote-friendly, fully-remote, not-stated **(the app rejects anything else)** |
| `workModeNote` | text | the evidence, in its own terms — which roles, which cities, what the page actually states. Leave empty where the mode alone says it. |  |
| `eligibilityNote` | text | constraints that hold across EVERY route it offers — visa sponsorship policy, nationality restrictions, hiring geography. Constraints specific to one route belong on that opportunity, not here. |  |
| `stance` | text | One line, in its own terms. Only where the organisation actually takes a position — leave it empty otherwise. Most research bodies do not argue for anything, and an empty stance is a finding rather than a gap. |  |
| `links` | linklist |  |  |
| `contacts` | linklist |  |  |
| `opportunities` | opportunities | the concrete ways in — one entry per route, each with its own status and dates. Cards still holding the older prose write-up keep it in a plain text box; clearing that box and saving switches the card to the structured editor. |  |
| &nbsp;&nbsp;↳ `opportunities[].kind` | None |  | suggested: job, fellowship, internship, PhD / studentship, postdoc, course, grant, scholarship, advising, residency, visiting, volunteer, expression-of-interest, prize, event, collaboration, resource *(a value outside the list is legal - the app has an "Other..." escape and keeps what you type)* |
| &nbsp;&nbsp;↳ `opportunities[].label` | None |  |  |
| &nbsp;&nbsp;↳ `opportunities[].url` | None |  |  |
| &nbsp;&nbsp;↳ `opportunities[].status` | None |  | one of: open, upcoming, rolling, closed, by-invitation, not-stated **(the app rejects anything else)** |
| &nbsp;&nbsp;↳ `opportunities[].asOf` **required** | None |  |  |
| &nbsp;&nbsp;↳ `opportunities[].deadline` | None |  |  |
| &nbsp;&nbsp;↳ `opportunities[].stipend` | None |  |  |
| &nbsp;&nbsp;↳ `opportunities[].eligibility` | None |  |  |
| &nbsp;&nbsp;↳ `opportunities[].workMode` | None | how this specific route works. Resources and collaborations have no work mode — leave them not-stated. | one of: onsite, hybrid, fully-remote, not-stated **(the app rejects anything else)** |
| `engagement` | text | your own status with it, applied, targeting, engaged, ruled out, on the radar. |  |
| `researchRelevance` | textarea | how this card connects to your research, if it does. Optional; leave blank for pure study cards. It only shows on the card when filled. |  |
| `myNotes` | textarea | your private working notes. Available on every card. Formatted text is edited with the toolbar on the card itself — if you see HTML code in this box, edit on the card instead. |  |
| `depth` | select | how far this card has been researched. "full" is authored from the organisation's own pages; "stub" is a one-line blurb and a link; "seed" is a name and a pointer. | one of: full, stub, seed **(the app rejects anything else)** |
| `checkedOn` | date | the date this card was last verified against the organisation's live pages. |  |
| `provenance` | textarea | how this card was authored: which of the organisation's own pages, read when, in which language. |  |

### `platform` - Platforms

**The front of the card is `blurb`** - what a reader sees before opening it.

| field | type | what the app says | values |
|---|---|---|---|
| `blurb` **(front)** | text |  |  |
| `orgType` | text | the kind of organisation it is (lab, funder, nonprofit…). Choose "Other…" to add a type the list does not have yet; it joins the list next time. | one of: commercial, nonprofit, academic, government, intergovernmental, network/community **(the app rejects anything else)** |
| `orgTypeNote` | text | why this type was chosen when the organisation does not say so itself, and any part of the old compound description that the sector alone does not carry — an insurer, a media company. orgType is always filled in, so this is where an author judgement is declared instead of being left to look like a stated fact. |  |
| `geography` | multiselect (csv) | the countries or regions it mainly operates in. Many values allowed — tap to toggle. Choose "Other…" to add one the list does not have yet; that box alone is comma-separated, so several can be typed at once. | *(the suggestions are whatever the deck already holds; anything is legal)* |
| `activityBucket` | text | what this org or tool mainly does, its category in the Field Map taxonomy. Choose "Other…" to add a category the list does not have yet; it joins the list next time. |  |
| `details` | textarea |  |  |
| `frontierRelevance` | multiselect (csv) | which research frontier(s) this org or tool touches. Many values allowed — tap to toggle; the "Other…" box alone is comma-separated, so several can be typed at once. This is only the research cross-link; to also show it in a course unit, set that separately in placement. | *(the suggestions are whatever the deck already holds; anything is legal)* |
| `topics` | multiselect (array) | what this organisation is ABOUT — the subject, not the sector or the activity. Many values allowed. Choose "Other…" to add a subject the list does not have yet. | suggested: technical safety & alignment, interpretability, evaluations & red-teaming, multi-agent systems & agents, AI for science, AI governance & policy, compute & hardware governance, international security & geopolitics, military & autonomous systems, biosecurity, cybersecurity, law, AI ethics & philosophy, fairness, bias & discrimination, privacy & surveillance, information integrity, economics & labour, education & learning, human–AI interaction, accessibility & assistive technology, public understanding, language access & multilingual AI, AI welfare & digital minds, consciousness science, forecasting & measurement, existential risk, wellbeing & mental health *(a value outside the list is legal - the app has an "Other..." escape and keeps what you type)* |
| `city` | text | the city it mainly operates from. Leave empty if it has no single base — empty is a legitimate answer here, not a gap. |  |
| `country` | text | the country it mainly operates from. Leave empty if not stated on its own pages. |  |
| `region` | select | the broad region, chosen by hand. Not derived from Country — an organisation with no single country can still be Distributed / global, and an unstated country stays empty rather than being guessed. | suggested: Africa, Australia, China, Continental Europe, Distributed / global, Gulf States, India, Israel, Japan, Latin America, North America, Russia, Singapore, South Korea, Taiwan, UK & Ireland *(a value outside the list is legal - the app has an "Other..." escape and keeps what you type)* |
| `safety` | select | how seriously it treats safety. "none-found" means none found BY US, in the languages we searched, on the pages it publishes — it is a finding. "not-assessed" means we have not looked. Never use one for the other. | one of: mission, programme, partial, none-found, not-assessed **(the app rejects anything else)** |
| `safetyNote` | text | one line of evidence for the posture above, in its own terms. |  |
| `openness` | select | what it puts into the commons and whether you can reuse it. | one of: open, partial, closed, not-stated **(the app rejects anything else)** |
| `opennessNote` | text | what specifically, and under what licence — open weights, open datasets, CC BY-SA, paywalled, members-only. |  |
| `workMode` | select | how it works across the organisation. A specific role may differ — that is recorded per opportunity. | one of: onsite, hybrid, remote-friendly, fully-remote, not-stated **(the app rejects anything else)** |
| `workModeNote` | text | the evidence, in its own terms — which roles, which cities, what the page actually states. Leave empty where the mode alone says it. |  |
| `eligibilityNote` | text | constraints that hold across EVERY route it offers — visa sponsorship policy, nationality restrictions, hiring geography. Constraints specific to one route belong on that opportunity, not here. |  |
| `stance` | text | One line, in its own terms. Only where the organisation actually takes a position — leave it empty otherwise. Most research bodies do not argue for anything, and an empty stance is a finding rather than a gap. |  |
| `links` | linklist |  |  |
| `contacts` | linklist |  |  |
| `opportunities` | opportunities | the concrete ways in — one entry per route, each with its own status and dates. Cards still holding the older prose write-up keep it in a plain text box; clearing that box and saving switches the card to the structured editor. |  |
| &nbsp;&nbsp;↳ `opportunities[].kind` | None |  | suggested: job, fellowship, internship, PhD / studentship, postdoc, course, grant, scholarship, advising, residency, visiting, volunteer, expression-of-interest, prize, event, collaboration, resource *(a value outside the list is legal - the app has an "Other..." escape and keeps what you type)* |
| &nbsp;&nbsp;↳ `opportunities[].label` | None |  |  |
| &nbsp;&nbsp;↳ `opportunities[].url` | None |  |  |
| &nbsp;&nbsp;↳ `opportunities[].status` | None |  | one of: open, upcoming, rolling, closed, by-invitation, not-stated **(the app rejects anything else)** |
| &nbsp;&nbsp;↳ `opportunities[].asOf` **required** | None |  |  |
| &nbsp;&nbsp;↳ `opportunities[].deadline` | None |  |  |
| &nbsp;&nbsp;↳ `opportunities[].stipend` | None |  |  |
| &nbsp;&nbsp;↳ `opportunities[].eligibility` | None |  |  |
| &nbsp;&nbsp;↳ `opportunities[].workMode` | None | how this specific route works. Resources and collaborations have no work mode — leave them not-stated. | one of: onsite, hybrid, fully-remote, not-stated **(the app rejects anything else)** |
| `engagement` | text | your own status with it, applied, targeting, engaged, ruled out, on the radar. |  |
| `researchRelevance` | textarea | how this card connects to your research, if it does. Optional; leave blank for pure study cards. It only shows on the card when filled. |  |
| `myNotes` | textarea | your private working notes. Available on every card. Formatted text is edited with the toolbar on the card itself — if you see HTML code in this box, edit on the card instead. |  |
| `depth` | select | how far this card has been researched. "full" is authored from the organisation's own pages; "stub" is a one-line blurb and a link; "seed" is a name and a pointer. | one of: full, stub, seed **(the app rejects anything else)** |
| `checkedOn` | date | the date this card was last verified against the organisation's live pages. |  |
| `provenance` | textarea | how this card was authored: which of the organisation's own pages, read when, in which language. |  |

## The data-derived vocabularies, as one deck holds them

*`activityBucket` and `geography` have no fixed list: the app suggests whatever the deck already holds, so a new deck starts with none. These are the values in one working deck of 2,122 cards on 2026-09-22, offered as a starting taxonomy rather than a rule. Keep one list across a batch and tell the person which buckets you used, so they can rename a bucket once in the app instead of card by card.*

**activityBucket (18):** AI welfare & digital minds · Advocacy · Career guidance & decision tools · Courses & learning · Fellowships & talent programmes · Field-building & convening · Forecasting & measurement · Frontier model development · Funding & grantmaking · Governance, policy & ethics · Human effects & interaction · Job boards & opportunity aggregators · Learning, education & neurodiversity · Research support & infrastructure · Security & defence policy research · Security & threat intelligence · Technical safety & alignment · Work, livelihoods & flourishing

**geography (46):** Australia, Bangladesh, Belgium, Canada, Chile, China, Czechia, Denmark, Estonia, Europe, European Union, Finland, France, Germany, Ghana, Global, India, Indonesia, Israel, Italy, Japan, Jordan, Kenya, Latin America and the Caribbean, Malaysia, Netherlands, Nigeria, Philippines, Poland, Portugal, Qatar, Russia, Rwanda, Saudi Arabia, Singapore, South Africa, South Korea, Spain, Sweden, Switzerland, Taiwan, Tunisia, UK, US, Ukraine, United Arab Emirates

---

*This file is generated. If your Cairn is newer than Cairn v1.11.91, a field here may have moved; check the skills folder on the repository for a newer copy.*