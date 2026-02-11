# PosterGen setup (Nano-Banana-Pro / Poe)

## Location

All poster-related code lives under:

`AmbassadorProgramme/PosterGen`

## What’s here

- **poster.html** – Workshop poster source.
- **prepPoster.md** – Brief for the poster.
- **screenshot-poster.js** – Exports the poster to `poster.jpg` (`npm run screenshot`).
- **genBetterPoster.js** – Calls Poe API using the key in `AmbassadorProgramme/LLM/poeKey.md` to produce **betterPoster.md** from `poster.html`.

## Using Poe (Nano-Banana-Pro) for betterPoster.md

1. Put your Poe API key in `AmbassadorProgramme/LLM/poeKey.md` (first line). See `AmbassadorProgramme/LLM/dummyPoe.md` if needed.
2. From `AmbassadorProgramme/PosterGen` run:
   ```bash
   npm install
   npm run better
   ```
   This uses the Poe model **Nano-Banana-Pro** by default. If that model isn’t available or you prefer another, set:
   ```bash
   POE_POSTER_MODEL=Claude-Sonnet-4 npm run better
   ```
3. Output is written to **betterPoster.md** in this folder (summary, suggestions, optional revised copy).

