# Why some Markdown files cannot open (and how we fixed GenReport.md)

## What you may see

When you try to open certain `.md` files in Cursor or VS Code, you get:

- **"Unable to open 'GenReport.md'"** (or the filename you clicked)
- **"Assertion Failed: Argument is `undefined` or `null`."**

The file exists and is not corrupted; the problem is how the editor (or an extension) handles it.

---

## Why it happens

### 1. First line looks like a path or URL

If the **first line** of the file is a path or URL with no heading (e.g. `courses/gcap3056/week1/week1.vtt` or `https://...`), some code in the editor or in a Markdown/workspace extension may assume:

- The document has a "title" or a proper `#` heading, or
- The first line is a valid document start.

When that expectation fails, it can pass `undefined` or `null` into an assertion and trigger the error. So the **content** of the file (especially the first line) can cause the bug, not the file system.

### 2. OneDrive or cloud-synced paths

If the file lives under **OneDrive** (or similar) cloud storage:

- Path resolution can be delayed or different while files are syncing.
- The editor may receive an invalid or unresolved path in some code paths and then hit an assertion that expects a valid value.

So the same file might open when stored in a local (non-synced) folder and fail when under OneDrive.

### 3. Extension behaviour

Markdown preview, workspace helpers, or other extensions sometimes:

- Parse the file to build a preview or outline.
- Expect a certain structure (e.g. a heading at the top).

If the file does not match that structure, the extension’s logic can throw or assert with `undefined`/`null`, and the "Unable to open" dialog appears even though the file is readable on disk.

---

## How we fixed GenReport.md

**Before:** The file started with a path and instructions with no heading:

```
courses/gcap3056/week1/week1.vtt

review the transcript above and fetch pages and info from ...
```

**After:** We changed it so that:

1. **The first line is a proper Markdown heading:** `# Generate Week 1 Report (instructions)`  
   This gives the document a clear "title" and a valid first line that editors and extensions expect.

2. **The rest is structured** with bold labels (e.g. **Input**, **Output**) and bullet points, so the file is clearly a normal Markdown document, not a raw path or URL.

3. **Only plain ASCII** is used in the first line and key structure (no special Unicode characters that could confuse parsing).

With these changes, the file should open normally. The **instruction content** is unchanged; only the format and first line were fixed to avoid triggering the assertion.

---

## What to do if another file won’t open

1. **Add a heading at the top**  
   Make the first line a level-1 heading, e.g. `# Document title`. Avoid starting the file with a path, URL, or blank line.

2. **Open by path**  
   Use **File → Open File** (Cmd+O) and choose the file explicitly. Sometimes this avoids the bug that occurs when opening from the tree or from a link.

3. **Check OneDrive**  
   If the project is under OneDrive, try copying the file to a folder outside OneDrive and opening that copy. If it opens there, the issue is likely path/sync related.

4. **Temporarily disable extensions**  
   Disable Markdown-related (or all) extensions and try opening again. If it works, re-enable extensions one by one to find which one causes the error.

5. **Reopen the workspace**  
   **File → Close Folder**, then **File → Open Folder** and open the project again. This clears some in-memory state that might be holding a bad path.

---

*This file was added after fixing GenReport.md so you have a written explanation and a reference for future "Unable to open" issues.*
