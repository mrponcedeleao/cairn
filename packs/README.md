# Packs

A pack is a JSON file of cards. You bring one into Cairn from the welcome screen, or with **Menu, Import** if you already have a deck. Nothing in this folder loads by itself: you decide what enters your deck, and you can read every file here before you do.

## `cairn-deck.json`, the starter deck. This one becomes your deck.

Six cards: a guide to the app, and a guide to each of the five sections. No content, nothing to delete, nothing of anyone else's.

It carries the name `cairn-deck.json` because that is the name Cairn recognises for a deck. Download it, then press **Open your deck** on the welcome screen and choose it: **it is now your deck, and everything you write goes into it.** Keep it wherever you keep your own files. (If the page and the file happen to sit in one folder, some browsers will open it for you when the page loads, but browsers disagree about that, so the button is the instruction that always holds.)

Start here if you want to start writing.

## `cairn-example-pack.json`, the sample pack. Look at it, or start from it.

Forty cards: **the same six guides as the starter deck**, plus one of every other kind of card, filled in for a made-up field called Trailcraft. A one-unit course with its readings, a small field map with real-shaped opportunities, a research topic with its theses and evidence and the honesty badges showing, an author's shelf, and a complete career plan for an invented person.

It deliberately does **not** carry the deck's name, because adopting it is a decision rather than a default. Two ways to use it:

- **Just look.** Press **Open a cards pack** on the welcome screen. The pack opens; your own deck is untouched.
- **Or start from it.** Rename the file to `cairn-deck.json`, open it with **Open your deck**, and it is your deck, guides and all. Then write your own cards alongside the samples and delete the samples as you go. Every one of them opens with *Sample card: delete me once you have your own* and is tagged `example`, so searching for **example** brings up exactly the ones still to go and nothing of yours.

If instead you import it into a deck you are already keeping, the six guides update in place (same ids) and the sample cards arrive alongside your own, where the same tag makes them easy to find again.

## A note on ids, because it is the one way to lose work

Import matches cards by `id`, and **a card whose id is already in your deck replaces that card whole**, including anything you wrote on it. That is how you update a card on purpose. It is also why a pack from anywhere else deserves a look first, and why the skills in [`../skills/`](../skills/) ship a check that refuses an id your deck already uses unless you say you mean it.

## Licence

CC BY 4.0. Use them, change them, pass them on.
