# Strengths of the AI Agent Approach (AmbassadorProgramme)

## What this approach is

- **File-based workflow**: Briefs (e.g. `prepPoster.md`) → artefacts (e.g. `poster.html`) → scripts call an LLM (Poe API) to produce suggestions or revised copy (e.g. `betterPoster.md`).
- **Agent in the loop**: You use Cursor (or similar) so an AI agent can read your files, run commands, and edit content. Scripts (e.g. `genBetterPoster.js`) send content to Poe and write results back to the repo.
- **Single source of truth**: Content lives in the repo; iterations are traceable and reusable.

---

## Strengths of this approach

- **Clear separation of roles**: You own the brief and the final call; the agent suggests and drafts. No "black box" that edits without you seeing the diff.
- **Reproducible and auditable**: Same brief + same (or updated) prompt can be re-run. You can version prompts and compare outputs.
- **Fits real workflows**: Poster, issue drafts, and messaging (e.g. Level 1) all follow: human writes brief/context → agent proposes → human revises. That matches how many people already work.
- **Leverages existing tools**: Poe API is OpenAI-compatible; one key, optional model switch (e.g. `POE_POSTER_MODEL=Claude-Sonnet-4`). Cursor uses the same key file for agent access without pasting keys in chat.
- **Scales to new tasks**: Once the pattern is in place (brief → script → LLM → output file), you can add new "agent tasks" (e.g. summarise feedback, draft emails) by new scripts or Cursor instructions, without changing the rest of the setup.

---

## Making it easier for people with no programming background

- **Reduce reliance on the terminal**: Provide a small set of fixed commands (e.g. "run poster improvement") and document them in one place. Consider a single script or shortcut that runs `npm run better` (or the like) so users don't need to understand `npm` or `cd`.
- **Pre-pack the environment**: One-time setup (e.g. Node, `npm install`, Poe key in `LLM/poeKey.md`) documented in a single "Setup" page. Optional: provide a ready-made environment (e.g. dev container or cloud project) so users only open and run.
- **Lean on Cursor (or similar) for the "agent" part**: Non-programmers can describe the task in natural language ("improve the poster copy from this brief") and the agent can run the script and show the result. The value is "tell the agent what you want" rather than "write code."
- **Point to no-code/low-code options for similar ideas**: People who prefer not to touch scripts at all can use visual AI workflow tools (e.g. Zapier AI, Power Automate, or open-source Dify/Langflow) to get "brief in → improved text out" with no code. Your materials can acknowledge this and position the repo as the "code-friendly" path that keeps everything in one place and version-controlled.

---

## Summary

- **Strengths**: Transparent, reproducible, file-based workflow that fits content iteration and scales to new tasks; uses one API key and familiar tools.
- **Easier for non-programmers**: Fewer commands, one clear setup doc, and emphasis on "talk to the agent" (Cursor) or on no-code alternatives for the same workflow idea.

---

## Background and further reading (web search)

- **AI agents for content**: Capabilities, use cases, benefits – [Medium](https://medium.com/@aiteacher/ai-agents-for-content-generation-capabilities-key-components-use-cases-and-applications-4cfccb680f68).  
  Summary: AI agents can handle research, drafting, and optimisation; they work with context and tone and free creators for higher-level decisions.

- **Transformative power of AI agents in content creation** – [AI Agents List](https://aiagentslist.com/blog/the-transformative-power-of-ai-agents-in-content-creation).  
  Summary: Focus on how agents support end-to-end content workflows and quality.

- **Collaborating with AI agents (teamwork, productivity)** – [arXiv](https://arxiv.org/html/2503.18238v1).  
  Summary: Field experiments on human–AI teams; productivity and communication gains when agents are used in structured workflows.

- **No-code / low-code AI tools (2025)** – [htdocs.dev](https://htdocs.dev/posts/top-7-open-source-ai-lowno-code-tools-in-2025-a-comprehensive-analysis-of-leading-platforms).  
  Summary: Overview of platforms like Dify, Langflow, Flowise, n8n with visual builders so non-programmers can build AI workflows.

- **AI workflow automation tools** – [Gumloop](https://gumloop.com/blog/best-ai-workflow-automation-tools).  
  Summary: Examples of tools that add AI steps into workflows with minimal coding.

- **Power Automate – AI capabilities** – [Microsoft Power Platform](https://www.microsoft.com/en-us/power-platform/blog/2024/09/19/advancing-automation-with-new-ai-capabilities-in-power-automate/).  
  Summary: "Record with Copilot" and "Create from Description" for building automations with natural language.

- **Zapier AI** – [Zapier](https://zapier.com/blog/ai-by-zapier-guide/).  
  Summary: Adding AI steps (e.g. summarisation, extraction) into Zapier workflows without separate AI accounts.
