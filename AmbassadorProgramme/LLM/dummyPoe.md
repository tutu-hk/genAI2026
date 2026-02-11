# Poe API key setup

This folder is used by local scripts or AI agents that call **Poe** (OpenAI-compatible API). The real key is stored in a file that is **not** committed to the repo.

## Why two files?

- **`poeKey.md`** – Your actual API key. It is listed in the repo’s `.gitignore`, so it stays only on your machine and is never pushed to GitHub. Your local AI agent can still read it when you reference it.
- **`dummyPoe.md`** (this file) – Instructions and documentation. Safe to commit and share.

## How to set up your key

1. **Get a Poe API key**
   - Go to [Poe for developers](https://creator.poe.com/docs/external-applications/openai-compatible-api).
   - Sign in or create an account, then create an API key in the Poe creator dashboard.

2. **Create the key file on your machine**
   - In this folder (`AmbassadorProgramme/LLM/`), create a file named **`poeKey.md`**.
   - Put your API key on the **first line** (no label, no quotes).
   - You can add the docs URL on a later line if you want, for reference.

   **Example `poeKey.md` (do not commit this file):**

   ```text
   your-api-key-here

   https://creator.poe.com/docs/external-applications/openai-compatible-api
   ```

3. **Confirm it’s ignored**
   - `poeKey.md` is in the project’s `.gitignore`. After creating it, run `git status` and ensure `poeKey.md` does **not** appear as an untracked file. If it does, the `.gitignore` entry may need to be fixed.

## Using the key locally

- Scripts or agents that need the key should read it from `AmbassadorProgramme/LLM/poeKey.md` (or the full path on your machine).
- In Cursor you can reference the file with `@AmbassadorProgramme/LLM/poeKey.md` so the agent can use the key without you pasting it into the chat.

## Reference

- [Poe – OpenAI-compatible API](https://creator.poe.com/docs/external-applications/openai-compatible-api)
