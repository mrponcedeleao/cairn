#!/usr/bin/env python3
"""Check a Cairn pack before importing it.

usage:
  python3 check-pack.py your-pack.json
  python3 check-pack.py your-pack.json --deck cairn-deck.json
  python3 check-pack.py pass-2.json --deck cairn-deck.json pass-1.json
  python3 check-pack.py your-pack.json --deck cairn-deck.json --replace card-id,card-id

What it does. It reads schema.json beside this script - the app's own field
registry, carried through with every attribute rather than summarised - and
holds a pack to the same rules the app applies when you import it:

  * enum fields    the app REJECTS an off-list value, so this is an error;
  * suggested      the app ACCEPTS it and warns, so this warns. Every declared
                   select in Cairn has an "Other..." escape and round-trips a
                   typed value verbatim; a check that refused one would be
                   lying about the app;
  * array shapes   a declared array receiving a string is an error and is never
                   comma-split; a csv field receiving a list warns, because the
                   app stringifies it the first time you save that card;
  * ids            an id already in your deck is an ERROR, because import
                   replaces a card whole and takes your notes with it. Say
                   --replace <ids> when you mean it;
  * titles         a title that matches a card already in your deck under a
                   different id warns - that is how one organisation becomes
                   two cards;
  * placement      a membership that files a card nowhere is an error, because
                   a card filed nowhere is invisible and silent about it.

Fields that belong to the person - notes, exercise answers, engagement,
research relevance, reading progress - are printed as NOTES, never as errors or
warnings. They are not for an assistant to clear.

Exit 1 if there are errors, 0 otherwise. No dependencies beyond Python 3.
"""
import json, os, re, sys, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
SCHEMA = json.load(open(os.path.join(HERE, "schema.json"), encoding="utf-8"))
META = SCHEMA.get("_meta", {})
SECTIONS = SCHEMA.get("_sections", {})
ENVELOPE_DOC = SCHEMA.get("_envelope", {})
TYPES = {k: v for k, v in SCHEMA.items() if not k.startswith("_")}

ENVELOPE = set()
for group in ("structural", "placement_and_structure", "declared_or_inert"):
    ENVELOPE |= {k for k in ENVELOPE_DOC.get(group, {}) if not k.startswith("_")}
STRUCTURAL = {"id", "type", "title"}
for group in ("structural", "placement_and_structure"):
    STRUCTURAL |= {k for k in ENVELOPE_DOC.get(group, {}) if not k.startswith("_")}
DECLARED_ELSEWHERE = dict(SCHEMA.get("_fieldOwners", {}))
DECLARED_ELSEWHERE.update({k: v for k, v in ENVELOPE_DOC.get("declared_or_inert", {}).items()
                           if not k.startswith("_")})
PERSONAL = set(ENVELOPE_DOC.get("personal", {}).get("fields", []))
SECTION_VALUES = set(SECTIONS.get("section", []))
MEMBERSHIP_KEYS = set(SECTIONS.get("keys", []))
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
RESEARCH_TYPES = {"thesis", "metric", "evidence", "question", "tension", "framework", "story"}


def load_cards(path):
    data = json.load(open(path, encoding="utf-8"))
    if isinstance(data, list):
        return data
    if isinstance(data, dict) and isinstance(data.get("cards"), list):
        return data["cards"]
    raise ValueError('the file must be {"version": 1, "cards": [...]} or a list of cards')


def check_value(f, v, tag, errors, warnings):
    """One field, by the app's own rules (validateCardDeclaratively)."""
    key = f["key"]
    if v is None or v == "":
        return
    shape = f.get("valueShape")
    if shape == "array" and not isinstance(v, list):
        errors.append(f"{tag}: {key} must be a list, got {type(v).__name__} - the app never comma-splits it")
        return
    if shape == "csv" and isinstance(v, list):
        warnings.append(f"{tag}: {key} is a comma-separated string in the app, not a list; "
                        f"a list is rewritten to a string the first time the card is saved")
        v = ", ".join(str(x) for x in v)
    if f.get("type") == "opportunities":
        check_opportunities(f, v, tag, errors, warnings)
        return
    if f.get("type") == "date" and not DATE.match(str(v)):
        errors.append(f"{tag}: {key} must be YYYY-MM-DD (or null)")
        return
    members = v if isinstance(v, list) else [v]
    if isinstance(f.get("enum"), list):
        for m in members:
            if m not in f["enum"]:
                errors.append(f"{tag}: {key} = {m!r} is not one of: {', '.join(map(str, f['enum']))}")
        return
    pool = f.get("optionsFrom") if isinstance(f.get("optionsFrom"), list) else f.get("options")
    if isinstance(pool, list):
        for m in members:
            if m not in pool:
                warnings.append(f"{tag}: {key} = {m!r} is not in the suggested list - legal "
                                f"(the app has an \"Other...\" escape), so keep it if you mean it")


def check_opportunities(f, v, tag, errors, warnings):
    if isinstance(v, str):
        warnings.append(f"{tag}: opportunities is the legacy prose shape, not the structured rows")
        return
    if not isinstance(v, list):
        errors.append(f"{tag}: opportunities must be a list of rows")
        return
    for i, row in enumerate(v):
        at = f"{tag}: opportunities[{i}]"
        if not isinstance(row, dict):
            errors.append(f"{at} is not an object")
            continue
        for s in f.get("entry", []):
            ev = row.get(s["key"])
            if ev is None or ev == "":
                if s.get("required"):
                    errors.append(f"{at} is missing {s['key']}")
                continue
            if s.get("type") == "date" or s["key"] in ("asOf", "deadline"):
                if not DATE.match(str(ev)):
                    errors.append(f"{at} {s['key']} {ev!r} is not an ISO date (YYYY-MM-DD)")
                    continue
            if isinstance(s.get("enum"), list) and ev not in s["enum"]:
                errors.append(f"{at} {s['key']} {ev!r} is not one of: {', '.join(s['enum'])}")
            elif isinstance(s.get("options"), list) and ev not in s["options"]:
                warnings.append(f"{at} {s['key']} {ev!r} is not in the suggested list")


def main(argv):
    if len(argv) < 2 or argv[1] in ("-h", "--help"):
        print(__doc__)
        return 2
    path = argv[1]
    deck_files, replace = [], set()
    i = 2
    while i < len(argv):
        if argv[i] == "--deck":
            i += 1
            while i < len(argv) and not argv[i].startswith("--"):
                deck_files.append(argv[i]); i += 1
            continue
        if argv[i] == "--replace":
            i += 1
            if i < len(argv):
                replace = {x.strip() for x in argv[i].split(",") if x.strip()}
                i += 1
            continue
        i += 1

    deck = {}
    for d in deck_files:
        try:
            for c in load_cards(d):
                if isinstance(c, dict) and c.get("id"):
                    deck[c["id"]] = c
        except Exception as e:
            print(f"ERROR could not read {d}: {e}")
            return 2
    deck_titles = {}
    for cid, c in deck.items():
        deck_titles.setdefault((c.get("type"), str(c.get("title", "")).strip().lower()), []).append(cid)

    try:
        cards = load_cards(path)
    except Exception as e:
        print("ERROR", e)
        return 2

    pack_ids = {c.get("id") for c in cards if isinstance(c, dict)}
    known = pack_ids | set(deck)
    pack_sources = {str(c.get("source", "")).strip().lower() for c in cards if isinstance(c, dict)}
    deck_sources = {str(c.get("source", "")).strip().lower() for c in deck.values()}
    all_sources = {s for s in pack_sources | deck_sources if s}
    frontiers = {str(c.get("title", "")).strip() for c in list(cards) + list(deck.values())
                 if isinstance(c, dict) and c.get("type") == "frontier"}

    errors, warnings, notes = [], [], []
    seen, letters, inert = set(), {}, {}
    for i, c in enumerate(cards):
        tag = f"card {i} ({c.get('id', '?') if isinstance(c, dict) else '?'})"
        if not isinstance(c, dict):
            errors.append(f"{tag}: not an object")
            continue
        t = c.get("type")
        if t not in TYPES:
            errors.append(f"{tag}: unknown type {t!r}")
            continue
        cid = c.get("id")
        if not cid:
            errors.append(f"{tag}: missing id")
        elif cid in seen:
            errors.append(f"{tag}: duplicate id inside this pack")
        elif cid in deck and cid not in replace:
            errors.append(f"{tag}: id {cid!r} already exists in the deck. Importing REPLACES that "
                          f"card whole, including the person's notes. Mint a new id, or say "
                          f"--replace {cid} if replacing it is what you mean.")
        seen.add(cid)
        if not c.get("title"):
            errors.append(f"{tag}: missing title")
        else:
            twin = [x for x in deck_titles.get((t, str(c["title"]).strip().lower()), []) if x != cid]
            if twin:
                warnings.append(f"{tag}: the deck already has a {t} titled {c['title']!r} under a "
                                f"different id ({twin[0]}). Importing adds a SECOND card, not an "
                                f"update. Check whether you mean to update that one.")
        fields = {f["key"]: f for f in TYPES[t]["fields"]}
        extra = set(c) - set(fields) - ENVELOPE - {"id", "type", "title"} - PERSONAL - set(DECLARED_ELSEWHERE)
        if extra:
            errors.append(f"{tag}: no Cairn card type has the field(s) {sorted(extra)}. The app would "
                          f"store them and show nothing; this is almost always a typo.")
        for k in sorted(set(c) & set(DECLARED_ELSEWHERE) - set(fields) - STRUCTURAL - PERSONAL):
            if c.get(k) not in (None, "", [], {}):
                inert.setdefault((k, t), []).append(cid)
        for key, f in fields.items():
            check_value(f, c.get(key), tag, errors, warnings)
        kf = TYPES[t].get("keyField")
        if kf and kf not in ("title",) and not c.get(kf):
            warnings.append(f"{tag}: {kf} (the front of a {t} card) is empty")
        for k in sorted(PERSONAL):
            if c.get(k):
                notes.append(f"{tag}: {k} is the person's own field and is filled. Leave it exactly "
                             f"as it is - this is not something to fix.")

        ms = c.get("memberships")
        if ms in (None, []):
            if t in RESEARCH_TYPES and c.get("track"):
                warnings.append(f"{tag}: no memberships, so this card is filed nowhere; a research "
                                f"card needs [{{\"section\": \"research\"}}]")
        elif not isinstance(ms, list):
            errors.append(f"{tag}: memberships must be a list")
        else:
            for m in ms:
                if not isinstance(m, dict) or not m or not set(m) <= MEMBERSHIP_KEYS:
                    errors.append(f"{tag}: membership {m!r} is not a shape the app reads "
                                  f"({', '.join(sorted(MEMBERSHIP_KEYS))})")
                    continue
                if "section" in m and m["section"] not in SECTION_VALUES:
                    errors.append(f"{tag}: section {m['section']!r} files this card nowhere. The "
                                  f"values are {sorted(SECTION_VALUES)}; course cards file with "
                                  f"{{\"subUnit\": <syllabus id>}} instead.")
                for k in ("subUnit", "course", "cast"):
                    if k in m and m[k] not in known:
                        errors.append(f"{tag}: membership {k} = {m[k]!r} names no card in this pack"
                                      + (" or the deck" if deck else " (pass --deck to check the deck)"))

            sections_on = {m.get("section") for m in ms if isinstance(m, dict) and "section" in m}
            casts_on = [m["cast"] for m in ms if isinstance(m, dict) and "cast" in m]
            if casts_on and "furtherReading" in sections_on:
                errors.append(f"{tag}: a card on a principal's shelf carries {{\"cast\": <id>}} ALONE. "
                              f"The app implies Further Reading from the cast id, and 0 of 2,122 live "
                              f"cards carry both; the bare section membership beside it is wrong.")
            for cst in casts_on:
                if not str(cst).startswith("fr-member-"):
                    errors.append(f"{tag}: cast {cst!r} does not begin \"fr-member-\". The app only "
                                  f"implies Further Reading membership from a cast id with that prefix, "
                                  f"so this card would be filed nowhere. A Further Reading principal's "
                                  f"id must begin fr-member-.")
            if casts_on and t == "library" and not c.get("source"):
                warnings.append(f"{tag}: a work on a shelf gathers by its source matching a "
                                f"sourceMatch row on the principal, and source is empty, so it will "
                                f"not appear under any of the principal's works.")

        if t == "sectionMember":
            if c.get("sectionRoot") == "furtherReading" and not str(cid).startswith("fr-member-"):
                errors.append(f"{tag}: a Further Reading principal's id must begin \"fr-member-\" - "
                              f"the app reads that prefix to imply shelf membership.")
            if not c.get("castMatch"):
                warnings.append(f"{tag}: castMatch is empty. It is the cast card's title EXACTLY, and "
                                f"it is what pairs the shelf with that person's cast card; the shelf "
                                f"title itself may read \"Person / Organisation\".")
            for j, r in enumerate(c.get("resources") or []):
                if not isinstance(r, dict) or not r.get("title"):
                    errors.append(f"{tag}: resources[{j}] has no title")
                    continue
                sm = str(r.get("sourceMatch", "")).strip()
                if not sm:
                    warnings.append(f"{tag}: resources[{j}] has no sourceMatch, so no card can gather "
                                    f"under that work on the shelf")
                elif all(sm.lower() not in s2 and s2 not in sm.lower() for s2 in all_sources):
                    warnings.append(f"{tag}: resources[{j}] sourceMatch {sm!r} matches no card's "
                                    f"source in this pack or the deck - nothing will gather under it")

        if t in ("institution", "platform"):
            if not any(isinstance(m, dict) and m.get("section") == "fieldMap" for m in ms or []):
                errors.append(f'{tag}: a {t} card must carry {{"section": "fieldMap"}}, always. '
                              f'(It may carry more: 25 live Field Map cards also sit in a course '
                              f'sub-unit, which is the two-homes pattern, not an error.)')
            if not c.get("provenance"):
                errors.append(f"{tag}: provenance is empty - which pages, read when, in which language")
            if not c.get("checkedOn"):
                errors.append(f"{tag}: checkedOn is empty")
            if not c.get("locations") and not c.get("latlng"):
                warnings.append(f"{tag}: no locations[] and no card-level latlng, so no pin on the "
                                f"map. That is correct for an organisation that names no place - "
                                f"never invent one to clear this.")
        if t in ("thesis", "metric", "evidence"):
            if not c.get("provenance"):
                warnings.append(f"{tag}: provenance is empty on a {t} (own work, developed with AI, "
                                f"from the literature?)")
            if c.get("maturity") not in (None, "", "Intuition"):
                warnings.append(f"{tag}: maturity is {c.get('maturity')!r}. An assistant sets "
                                f"Intuition and says in its reply why the person might promote it; "
                                f"promotion is theirs.")
        if t == "metric" and not c.get("validityConcerns"):
            warnings.append(f"{tag}: a metric with no validityConcerns - a metric with no doubts is not a metric")
        if t == "evidence" and not c.get("limitations"):
            warnings.append(f"{tag}: evidence without limitations")
        if t in RESEARCH_TYPES:
            tr = c.get("track")
            if tr and frontiers and tr not in frontiers:
                warnings.append(f"{tag}: track {tr!r} names no frontier card in this pack or the "
                                f"deck; the card will not group under one")
            if c.get("theFrontier") and tr and c["theFrontier"] != tr:
                warnings.append(f"{tag}: theFrontier {c['theFrontier']!r} disagrees with track {tr!r}")
        if t == "frontier" and deck:
            deck_frontiers = {x.get("title"): x.get("id") for x in deck.values() if x.get("type") == "frontier"}
            if deck_frontiers and cid not in deck_frontiers.values():
                warnings.append(f"{tag}: this pack MINTS a research topic and the deck already has "
                                f"{len(deck_frontiers)}: {', '.join(sorted(t2 for t2 in deck_frontiers if t2))}. "
                                f"A topic whose name the person has not settled cannot be matched by "
                                f"title - ask them whether this is one of those before minting a second.")
            clash = [x.get("id") for x in deck.values()
                     if x.get("type") == "frontier" and c.get("order") not in (None, "")
                     and x.get("order") == c.get("order") and x.get("id") != cid]
            if clash:
                warnings.append(f"{tag}: order {c.get('order')!r} is already taken in the deck by "
                                f"{clash[0]}; two topics at the same order sort arbitrarily.")

        if t == "courseUnit":
            if not c.get("courseId"):
                errors.append(f"{tag}: courseUnit needs courseId (the course guide's id)")
            elif c["courseId"] not in known:
                errors.append(f"{tag}: courseId {c['courseId']!r} names no card in this pack or the deck")
            if not re.match(r"^unit-\d+$", str(c.get("unitKey", ""))):
                errors.append(f"{tag}: courseUnit unitKey must look like unit-1")
        if t == "syllabus":
            if not any(isinstance(m, dict) and "course" in m and "unitKey" in m for m in ms or []):
                errors.append(f'{tag}: a syllabus card needs a membership {{"course": <guide id>, "unitKey": "unit-N"}}')
            for j, r in enumerate(c.get("resources") or []):
                if not isinstance(r, dict) or not r.get("title"):
                    errors.append(f"{tag}: resources[{j}] has no title")
                    continue
                sm = str(r.get("sourceMatch", "")).strip()
                if not sm:
                    warnings.append(f"{tag}: resources[{j}] has no sourceMatch, so no content card "
                                    f"can cluster under that reading")
                elif all(sm.lower() not in s2 and s2 not in sm.lower() for s2 in all_sources):
                    warnings.append(f"{tag}: resources[{j}] sourceMatch {sm!r} matches no card's "
                                    f"source in this pack or the deck - nothing will cluster under it")
        if t == "plan":
            L = c.get("planLetter")
            if L:
                letters.setdefault(L, []).append(cid)
        if t == "goal" and c.get("phaseId") and c["phaseId"] not in known:
            warnings.append(f"{tag}: phaseId {c['phaseId']!r} names no phase card. (The app does not "
                            f"read phaseId yet; an orphan link is silent rather than visible.)")
        for k in ("date", "lastReviewed", "asOf", "checkedOn"):
            v = c.get(k)
            if v and DATE.match(str(v)) and str(v) > datetime.date.today().isoformat():
                errors.append(f"{tag}: {k} {v!r} is in the future")

    for (k, t), ids in sorted(inert.items()):
        warnings.append(f"{k} is written on {len(ids)} {t} card(s) ({ids[0]}"
                        + (f" and {len(ids)-1} more" if len(ids) > 1 else "")
                        + f") and a {t} card does not declare it: the app stores it and shows "
                          f"nothing - no row on the form, no line on the face. Declared on: "
                          f"{DECLARED_ELSEWHERE[k]}.")

    for L, ids in letters.items():
        if len(ids) > 1:
            errors.append(f"plan letter {L!r} is on {len(ids)} cards ({', '.join(ids)}). One plan per "
                          f"letter: if the person really has two, that is a question for them - put "
                          f"it on an uncertainty card and say so in your reply.")

    for n in notes:
        print("NOTE ", n)
    for w in warnings:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    print(f"\n{len(cards)} card(s): {len(errors)} error(s), {len(warnings)} warning(s), {len(notes)} note(s)")
    print(f"Checked against the field registry of {META.get('app', 'Cairn')}, read "
          f"{META.get('generatedOn', '?')} (skills {META.get('skills', '?')}). If your Cairn is newer, "
          f"check the skills folder for a newer copy of this file.")
    print("NOT checked: whether anything on a card is TRUE; whether the person already has a card "
          "for this thing under another title; the person's own fields; whether an id is the one "
          "they meant" + ("" if deck else "; ANYTHING about the deck, because --deck was not passed"))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
