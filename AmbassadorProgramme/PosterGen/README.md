# PosterGen

Code, assets, and automation for generating and improving the **Ambassador Programme** workshop poster (Generative AI Agent 101 / Agent AI 101).

## Folder Structure

```
PosterGen/
├── README.md                   ← this file
├── package.json                ← npm scripts & dependencies
├── package-lock.json
│
├── posters/                    ← HTML / SVG poster source files
│   ├── poster.html             ← original workshop poster
│   ├── posterBetter.html       ← AI-improved version (generated)
│   ├── finalPoster.html        ← final polished version
│   ├── posterTrae.html         ← Trae-branded variant
│   ├── posterTrae.svg          ← SVG vector version of Trae poster
│   └── poster_A4.html          ← high-res A4 print version
│
├── scripts/                    ← Node.js automation
│   ├── screenshot-poster.js    ← screenshot poster.html → output/poster.jpg
│   ├── screenshot-better.js    ← screenshot posterBetter.html → output/betterPoster.jpg
│   ├── screenshot-a4.js        ← screenshot poster_A4.html → output/poster_A4.png (3× A4)
│   ├── genBetterPoster.js      ← Poe API → docs/betterPoster.md (suggestions)
│   └── genBetterPosterJpg.js   ← Poe API → posterBetter.html + screenshot
│
├── output/                     ← generated images (screenshots)
│   ├── betterPoster.jpg
│   └── poster_A4.png
│
├── assets/                     ← logos & images
│   ├── HKBULClogos/            ← HKBU and Language Centre logos
│   └── editPoster/             ← Trae logo and supporting files
│
└── docs/                       ← planning, prompts, setup notes
    ├── prepPoster.md           ← original brief & requirements
    ├── betterPoster.md         ← AI-generated feedback & suggestions
    ├── editPoster.md           ← editing notes for the poster
    └── setupNano.md            ← Poe / Nano-Banana-Pro setup guide
```

## Setup

1. **Install dependencies** (from this folder):

   ```bash
   cd AmbassadorProgramme/PosterGen && npm install
   ```

2. **Poe API key** (needed for the `better` / `better-jpg` scripts):
   - Create `AmbassadorProgramme/LLM/poeKey.md` with your Poe API key on the first line.
   - See `AmbassadorProgramme/LLM/dummyPoe.md` for full instructions.

## npm Scripts

Run from `AmbassadorProgramme/PosterGen`:

| Command | Description |
|---|---|
| `npm run screenshot` | Export `poster.html` → `output/poster.jpg` |
| `npm run screenshot-better` | Export `posterBetter.html` → `output/betterPoster.jpg` |
| `npm run screenshot-a4` | Export `poster_A4.html` → `output/poster_A4.png` (high-res 3× A4) |
| `npm run better` | Call Poe API to generate `docs/betterPoster.md` (design suggestions) |
| `npm run better-jpg` | Call Poe API to generate improved HTML + screenshot |

To use a different Poe model:

```bash
POE_POSTER_MODEL=Claude-Sonnet-4 npm run better
```

## Poster Versions

| File | Description |
|---|---|
| `poster.html` | Original "Generative AI Agent 101" poster |
| `posterBetter.html` | AI-improved version (auto-generated) |
| `finalPoster.html` | Final version for distribution |
| `posterTrae.html` | Variant branded with Trae / IDE sponsor |
| `posterTrae.svg` | Vector (SVG) version of Trae poster |
| `poster_A4.html` | Print-ready A4 layout with university logos |
