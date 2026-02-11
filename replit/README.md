# Replit-specific code

This folder contains **all** Replit-related files so the project root has no Replit-specific docs or scripts.

- **`config.toml`** — Replit run/build/deploy config. On Replit, run `npm run replit:setup` once to copy it to root as `.replit`.
- **`vite-plugins.ts`** — Replit Vite plugins; root `vite.config.ts` imports from here.
- **`copy-config.mjs`** — Script that copies `config.toml` to root `.replit` (run via `npm run replit:setup`).
- **`REPLIT.md`** — Full Replit docs and live project link.
