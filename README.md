# genAI2026

AI Ambassador Programme and course materials at HKBU (2025-26).

## Repository Structure

```
genAI2026/
├── index.html                  ← GitHub Pages landing page
├── README.md                   ← this file
│
├── AmbassadorProgramme/        ← Student Ambassador Programme
│   ├── PosterGen/              ← poster generation & automation (see its own README)
│   ├── LLM/                    ← Poe API key setup
│   ├── setup/                  ← onboarding & dev environment setup
│   ├── articulate-one-click/   ← AI agent strength & one-click tool docs
│   ├── workshop/               ← workshop planning & latest content
│   └── messaging/              ← programme messaging, issue drafts, published issues
│
├── courses/                    ← Course materials
│   ├── gcap3056/               ← GCAP 3056 – Community engagement group projects
│   ├── gcap3226/               ← GCAP 3226
│   ├── UCLC1008/               ← UCLC 1008 – Academic writing, AWQ prep, lessons
│   └── PTHdebate/              ← Mandarin debate demo (AI-assisted research)
│
├── replit/                     ← Web app (Vite + React + Express), work in progress
│   └── (see replit/README.md)
│
├── Ollama/                     ← Local LLM app (macOS binary, gitignored)
└── Ollama-darwin.zip           ← Ollama installer archive (gitignored)
```

## Running the Web App

```bash
cd replit && npm install && npm run dev
```

See [replit/REPLIT.md](./replit/REPLIT.md) for Replit deployment details.

## GitHub Pages

All HTML and static files in this repo are published via GitHub Pages:

1. **GitHub** > **Settings** > **Pages**
2. **Source:** Deploy from branch `main`, folder `/ (root)`
3. `.nojekyll` at root disables Jekyll -- all files are served as-is

**Base URL:** https://tesolchina.github.io/genAI2026/

## Key Sub-areas

### Ambassador Programme

The `AmbassadorProgramme/` folder contains everything for the Generative AI Agent Student Ambassador Programme:

| Subfolder | Purpose |
|-----------|---------|
| `PosterGen/` | Poster HTML sources, Puppeteer screenshot scripts, Poe API automation |
| `LLM/` | API key configuration (Poe) |
| `setup/` | Environment setup guides for participants |
| `articulate-one-click/` | AI agent capabilities and one-click tool documentation |
| `workshop/` | Workshop planning and latest content |
| `messaging/` | Programme announcements, GitHub issue drafts, revision history |

### Courses

| Course | Description |
|--------|-------------|
| `gcap3056/` | Community engagement projects (6 student groups), weekly materials, project meta-director |
| `gcap3226/` | Course materials and resources |
| `UCLC1008/` | Academic writing -- AWQ study guides, mock practice, lessons, Moodle posts, real materials |
| `PTHdebate/` | Mandarin debate preparation demo with AI-powered web search scripts |
