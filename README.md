# Cairn

**A companion for a crossing: into a new field, out of one career and into another, or from study into work.**

Cairn is one web page and one file. The page is `index.html`. The file is your deck of cards, and it stays on your device.

It holds five kinds of thing that usually live in five different places:

- a **course**, carded reading by reading, so what you studied is still there a month later;
- a **map of the field**: the organisations, labs, funders and platforms, with what each one is actually offering right now;
- your own **research**, structured so that how sure you are is written on the card rather than remembered;
- a **shelf** of reading beyond any course, gathered under the people who wrote it;
- and the **plan** for the crossing itself: where you started, plan A and its fallbacks, what you will not do, and a check-in that leaves a stone each time.

## What it is not

It is not a service, and there is no account. Nothing you write is uploaded, because there is nowhere for it to go: the page reads your file, and your file sits where you put it. It works offline once it is open, on a laptop or a phone.

It is not finished, and it is not polished in the places nobody has needed yet. It was built for one person's crossing and it is shared because the shape of it may be useful to someone else's.

## Starting

1. **Open the app.** Either use it in your browser at <https://mrponcedeleao.github.io/cairn/>, or save `index.html` onto your own computer and open it from there. They are the same page, and both work offline once open. **On a phone, use the web address.** Cairn can read your cards aloud with your device's own voices anywhere, but the optional cloud voice has to call out to a speech service, and an iPhone opening the page as a local file will not let it: the call never leaves, and the read-aloud quietly falls back to the device voices. From the web address it works, including on 4G with the screen locked.
2. **Download a deck.** [`packs/cairn-deck.json`](packs/) is six guide cards and nothing else. It carries that name because `cairn-deck.json` is the name Cairn recognises for a deck.
3. **Open it.** On the welcome screen press **Open your deck** and choose the file you just downloaded. That is the step that works in every browser, and from then on it is your deck: everything you write goes into it.
4. **Know how saving works before you start.** It is the one thing that differs between browsers, and it is worth thirty seconds now rather than a surprise later.
   - **Chrome or Edge on a computer:** Save writes straight back into the file you opened.
   - **Safari or Firefox on a computer:** Save hands you a fresh copy of the file under the same name, and you replace the old one.
   - **On a phone:** Save writes a small patch of only what changed, and importing that patch into the full deck on your computer merges it.

*If you keep `index.html` and your `cairn-deck.json` in one folder, some browsers will open the deck for you when you open the page. It is a convenience rather than the way in: browsers disagree about whether a page may read a file sitting next to it, so **Open your deck** is the instruction that always holds.*

## The two packs, and which one to start from

Both are in [`packs/`](packs/), and **both carry the same six guide cards**: one for the app and one for each of the five sections. The guides are the manual in card form, and they are worth keeping whichever pack you begin with.

### The starter deck, `cairn-deck.json`

The six guides and nothing else. No content to read, nothing to delete, nothing of anyone else's. Download it, open it with **Open your deck**, and start writing your own cards. This is the one to take if you know what you want to card.

### The sample pack, `cairn-example-pack.json`

The same six guides **plus one of every other kind of card**, filled in for a made-up field called Trailcraft: a one-unit course with its readings, a small field map with real-shaped opportunities, a research topic with its theses and evidence and the honesty badges showing, an author's shelf, and a complete career plan for an invented person. It is there so you can see the shapes before you make your own.

There are two ways to use it, and both are fine.

- **Just look.** Press **Open a cards pack** on the welcome screen. It shows you the pack without adopting it as your deck.
- **Or start from it.** Rename the file to `cairn-deck.json`, open it with **Open your deck**, and it is your deck, guides and all. Write your own cards alongside the samples and **delete the samples as you go**: every one of them opens with *Sample card: delete me once you have your own*, and they are all tagged `example`, so searching for **example** brings up exactly the ones still to go and nothing of yours.

## The user guide

[`docs/USER-GUIDE.md`](docs/USER-GUIDE.md) walks through the whole app with a picture for each step: getting started, each of the five sections, working with an AI assistant, and what to do when something goes wrong.

**It is a first draft.** It was checked against the app screen by screen and read by a newcomer before it went up, but few people have used it yet, so parts of it will change. If a step does not match what you see, or something is missing, that is exactly what it needs to hear: use the Contact button in the app, or open an issue on this repository.

## Your cards are yours

The deck is plain JSON. You can read it, back it up, put it in a folder you sync, or open it in anything. Import adds cards to the deck you already have, matching by `id`, and **a card with an id you already use is replaced whole**, which is how you update a card on purpose and the one way to lose one by accident. The packs and the skills' check both warn about this before it happens.

## Who made it

Maria do Rosário Ponce de Leão, for her own move from twenty years in product into AI safety research, because the tools she could find held one of those five things and not the others. It is open and contributions are welcome.

Cairn was built by one person working with AI assistants, and the cards in the example pack were drafted the same way and checked by hand. That is worth highlighting on a tool whose whole argument is that a card should say where it came from.

## Licences

The app is MIT. The card packs here are CC BY 4.0: use them, change them, pass them on.

## Saying something

There is a Contact button in the app, and the address is <cairn.app.feedback@gmail.com>. If something confused you, that is the most useful thing you can send. Issues on this repository are read too.
