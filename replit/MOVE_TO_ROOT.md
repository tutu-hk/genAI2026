# Move these back to project root

The **main app** should live at the **project root**, not inside `replit/`. Only Replit-specific files belong in this folder.

## Move these to the project root (one level up)

Move the following from `replit/` to the project root (so they sit beside the `replit/` folder):

| Move to root | Notes |
|--------------|--------|
| **`client/`** | Frontend app |
| **`server/`** | Backend (routes, static, vite dev) |
| **`shared/`** | Shared schema/types |
| **`script/`** | Build script |
| **`package.json`** | Already has `replit:setup` pointing to `replit/copy-config.mjs` |
| **`package-lock.json`** | Lockfile |
| **`tsconfig.json`** | TypeScript config |
| **`tailwind.config.ts`** | Tailwind theme |
| **`drizzle.config.ts`** | Drizzle/DB config |
| **`postcss.config.js`** | PostCSS (Tailwind) |
| **`components.json`** | shadcn/ui config |
| **`basicSetup.md`** | Docs |
| **`idea.md`** | Docs |
| **`plan.md`** | Docs |

After moving, **delete** from `replit/` (root now has the canonical versions):

- **`replit/vite.config.ts`** — root already has `vite.config.ts` that imports from `./replit/vite-plugins`.

## Keep in `replit/` (do not move)

| Keep here | Purpose |
|-----------|--------|
| **`config.toml`** | Replit run/deploy config; source for root `.replit` |
| **`copy-config.mjs`** | Copies this to root `.replit` (`npm run replit:setup`) |
| **`vite-plugins.ts`** | Replit Vite plugins |
| **`REPLIT.md`** | Replit docs and live link |
| **`README.md`** | This folder’s readme |
| **`MOVE_TO_ROOT.md`** | This file |

## Root already has

- **`vite.config.ts`** — uses paths for root `client/` and `shared/`, imports `./replit/vite-plugins`.
- **`.gitignore`** — includes `.replit` and standard ignores.

After you finish moving, run from the **project root**: `npm install` and `npm run dev`.
