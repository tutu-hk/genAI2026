# Replit deployment

This project can be run on **Replit** or cloned and run locally. All Replit-specific code and docs live in this **`replit/`** folder.

## Live project on Replit

- **Replit project:** [https://replit.com/@tesolchina/GenAI-Clone](https://replit.com/@tesolchina/GenAI-Clone)

Use the link above to open or remix the project on Replit.

---

## Running on Replit

Replit expects a file named `.replit` in the project root. We don’t commit that file; the source of truth is `replit/config.toml`.

**After cloning on Replit, run once:**

```bash
npm run replit:setup
```

This runs `replit/copy-config.mjs`, which copies `config.toml` to `.replit` in the root. Then use the normal run button or `npm run dev`.

---

## If you forked or cloned this repo (running locally or elsewhere)

You don’t need Replit to run the app. Everything Replit-specific is in this folder:

| In this folder | Purpose |
|----------------|--------|
| **`config.toml`** | Replit run/build/deploy config (used only when you run `npm run replit:setup` on Replit). |
| **`vite-plugins.ts`** | Replit Vite plugins (error overlay, dev banner). Only active when `REPL_ID` is set (i.e. on Replit). |
| **`copy-config.mjs`** | Script that copies `config.toml` to root `.replit`. |
| **`REPLIT.md`** | This file. |

You can ignore the entire `replit/` folder when running locally. Root has no `.replit` file.

**To run without Replit:**

```bash
npm install
npm run dev
```

Set `DATABASE_URL` if you use the database. No Replit account or config is required.
