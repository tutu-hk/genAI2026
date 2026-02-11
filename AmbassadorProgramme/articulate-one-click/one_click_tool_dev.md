# One-Click Tool: Wrapping a Workflow

## Goal

- Turn a multi-step workflow (e.g. "improve poster from HTML via Poe → write betterPoster.md") into a **single action** the user can trigger with one click (or one shortcut).
- No need to open a terminal, `cd` into a folder, or remember command names.

---

## How it may work

### 1. One entry point

- **Single script or command** that runs the whole workflow.
- Example: "Poster improve" = read `poster.html` + call Poe + write `betterPoster.md` (and optionally refresh a screenshot). User runs one thing; all steps happen in order.
- Inputs and outputs are fixed or chosen by convention (e.g. input = `poster.html`, output = `betterPoster.md`), so the user doesn't configure anything for the common case.

### 2. What "one click" can mean

| Option | How it works | Best for |
|--------|----------------|----------|
| **IDE task** | VS Code / Cursor "Tasks": define a task that runs the script; user runs it from Command Palette (e.g. "Run Task" → "Poster: improve"). | People already in the editor. |
| **Shortcut / launcher** | Desktop shortcut or launcher app that runs a shell command or script (e.g. `npm run better` in PosterGen). | People who don't want to open the repo. |
| **Single shell script** | One script in the repo (e.g. `run-poster-improve.sh`) that `cd`s to the right folder, runs `npm run better`, and optionally opens the output file. User double-clicks the script or runs it from File Explorer. | Quick adoption with minimal tooling. |
| **Make / npm at repo root** | From repo root: `make poster-better` or `npm run poster-better` that invokes the PosterGen workflow. One place to discover all "one-click" workflows. | Teams that already use make/npm. |

### 3. Workflow contract (for developers)

To wrap any workflow as a one-click tool:

- **Inputs**: Clearly defined (e.g. which file(s) or folder the workflow reads).
- **Outputs**: Where results go (e.g. `betterPoster.md`, or `poster.jpg`).
- **One command**: One script or one `npm`/`make` target that runs from a known working directory and does not require extra arguments for the default case.
- **Idempotent / safe**: Running it again overwrites or updates the output in a predictable way; no surprise side effects.

### 4. Example: Poster improve as a one-click tool

- **Input**: `AmbassadorProgramme/PosterGen/poster.html` (and Poe key in `LLM/poeKey.md`).
- **Action**: Call Poe with the poster prompt; write summary and suggestions to `betterPoster.md`.
- **One command today**: From `PosterGen`, `npm run better`.  
- **One-click wrap**:  
  - Add a task in Cursor/VS Code that runs `npm run better` with `cwd` set to `PosterGen`, **or**  
  - Add at repo root a script `run-poster-improve.sh` (or `run-poster-improve.cmd` on Windows) that does `cd AmbassadorProgramme/PosterGen && npm run better` and optionally `open betterPoster.md`.  
  User then has "one click" = run that task or double-click that script.

### 5. Adding more one-click tools

- Same pattern: one workflow → one script or one task → one name ("Poster: improve", "Screenshot poster", "Draft issue from brief", etc.).
- Keep a small **menu** in a single doc (e.g. "One-click tools") listing: name, what it does, how to run it (task name or script path). That way non-programmers see exactly what's available and how to trigger it.

---

## Summary

- **One-click tool** = one entry point (script or IDE task) that runs a full workflow with fixed inputs/outputs.
- **Implementation**: Define the workflow's input/output and single command; then expose that command via a Cursor/VS Code task, a launcher script at repo root, or a desktop shortcut.
- **Scaling**: Each new workflow becomes one more named task or script and one line in the "One-click tools" menu.
