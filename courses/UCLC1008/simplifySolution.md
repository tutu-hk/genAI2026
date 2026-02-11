# UCLC1008 — Simplify: Too Many Folders and Materials

**Purpose:** Reduce clutter and duplication in `courses/UCLC1008` while keeping one clear path for (1) teaching, (2) AI agent demo, and (3) course-team materials.

---

## 1. Current situation (what exists)

| Top-level folder | What it holds | Rough size / overlap |
|------------------|----------------|----------------------|
| **AIagentDemo/** | Demo for genAI agent: focused reading, MockPractice (JumpWaterAgain, practice1), teacher materials (JumpIntoWater), StudyGuide, context/task docs | Many .md; **overlaps with RealMat** |
| **lessons/** | Mat (sample AWQ), Moodle_posts (week3–6 tasks), Plans (week3–6) | **Overlaps with RealMat archive** |
| **materials/** | course materials in MD (modules, Study Guide, sample AWQ), Week1-5_AWQ plans | **Overlaps with RealMat** |
| **RealMat/** | Curated copy by assessment (AWQ, ACE, CRAA) and type (FromCourseTeam, ExamTipsPractice, ConceptSkillLesson); AWQ has deep archive (LessonContent, MoodleTasks, ReadingAndSynthesis, WeeklyPlans, Other) | **Largest; contains copies of AIagentDemo + lessons + materials** |
| **SimonWebsite/** | Docs for student system, dashboard, integration | Separate concern |
| **studentHandsOn/** | Guides 01–06, generateGuides | Small, focused |
| **Week6AWQ/** | Study Guide PDF, email from coordinator, InputProcessOutputModel, OCR scripts | **Overlaps materials + RealMat** |

**Main issue:** The same content lives in 2–3 places (e.g. reading/synthesis and JumpWaterAgain in AIagentDemo *and* in RealMat/AWQ/ConceptSkillLesson/archive/ReadingAndSynthesis).

---

## 2. Simplified target structure

**Idea:** One “source of truth” per type of content; everything else is either a **single entry point** or **archived**.

```
UCLC1008/
├── README.md              # Keep: overview + link to this doc
├── start.md               # Keep: quick entry
├── simplifySolution.md    # This file
│
├── teaching/              # NEW: single place for teaching (merge lessons + materials)
│   ├── plans/             # Week 3–6 plans (from lessons/Plans)
│   ├── moodle/            # Moodle tasks HTML (from lessons/Moodle_posts)
│   ├── mat/               # Sample AWQ Mat (from lessons/Mat)
│   └── materials/         # Modules, Study Guide, sample AWQ (from materials/)
│
├── AIagentDemo/           # KEEP as-is for demo; trim duplicates only
│   ├── focusedReading/    # Keep
│   ├── MockPractice/      # Keep (practice1, JumpWaterAgain)
│   ├── teacherJumpIntoWater/  # Keep
│   └── *.md (context, task, StudyGuide)  # Keep
│
├── RealMat/               # KEEP but treat as generated/archive
│   └── (populate from INVENTORY from teaching/ + AIagentDemo only)
│
├── Week6AWQ/              # MERGE into teaching/materials or one subfolder
│   └── (Study Guide PDF, coordinator email, I/O model → teaching)
│
├── studentHandsOn/        # KEEP
└── SimonWebsite/          # KEEP (separate)
```

So: **teaching/** = canonical for lessons + materials; **AIagentDemo/** = canonical for agent demo; **RealMat** = populated from inventory, not hand-edited in parallel.

---

## 3. Overlap map (what to deduplicate)

| Content | Lives in | Action |
|---------|----------|--------|
| Study Guide AWQ | materials/, Week6AWQ (PDF), AIagentDemo/StudyGuideAWQ.md, RealMat | **Pick one:** e.g. `teaching/materials/StudyGuideAWQ.md` + PDF in same folder; remove from Week6AWQ root; RealMat copies from inventory |
| JumpWaterAgain / reading synthesis | AIagentDemo/MockPractice/JumpWaterAgain/, AIagentDemo/teacherJumpIntoWater/, RealMat/.../ReadingAndSynthesis/ | **Canonical:** AIagentDemo. RealMat only if INVENTORY points there |
| Week 3–6 plans | lessons/Plans/, RealMat/.../WeeklyPlans/ | **Canonical:** teaching/plans/; RealMat from inventory |
| Moodle tasks | lessons/Moodle_posts/, RealMat/.../MoodleTasks/ | **Canonical:** teaching/moodle/; RealMat from inventory |
| Course modules (MD) | materials/course materials in MD/, RealMat | **Canonical:** teaching/materials/; RealMat from inventory |
| Sample AWQ (Mat) | lessons/Mat/, RealMat | **Canonical:** teaching/mat/; RealMat from inventory |

---

## 4. Doc relevance: which are more vs. less relevant

**Goal:** Decide which docs to keep in the main workflow vs. archive or keep a single copy only.

### 4.1 Relevance criteria

| Level | Meaning | Where it should live |
|-------|--------|----------------------|
| **More relevant** | Used often for teaching or demo; current semester; student- or agent-facing | Prominent in `teaching/` or `AIagentDemo/`; one canonical copy |
| **Less relevant** | Historical, one-off, or duplicate; reference-only; older versions | Single copy in archive, or in RealMat only; or remove |

**Questions to decide:**
- Do I open this at least once per semester? → **More**
- Is it the official current version (e.g. Study Guide, coordinator email)? → **More**
- Is it a duplicate of something I already keep elsewhere? → **Less** (keep one)
- Is it a draft / iteration (e.g. detailedPlan, detailedPlan02, detailedPlan03)? → **Less** (keep latest or one summary)
- Is it only for scripts/inventory (e.g. INVENTORY.md, populate script)? → **More** for maintenance; **Less** for daily teaching

### 4.2 By purpose: more vs. less relevant

**Teaching (plans, Moodle, materials)**

| More relevant | Less relevant |
|---------------|----------------|
| Current week plans (e.g. week5, week6 AWQ prep) | Old weekly plans if superseded by one “master” plan |
| Moodle task HTML you actually post (week3–6) | Duplicate task files (e.g. task1.html vs task1_moodle.html → keep one) |
| Study Guide to AWQ (current version), AWQ Instructions, Modules 1 & 2 | Extra copies of same doc in materials vs. Week6AWQ vs. RealMat |
| Sample AWQ + Student Answer (Mat) | README_OPENING_FILES, README_W3H1_tasks (keep one if needed) |
| Coordinator email, InputProcessOutputModel | Multiple plan variants (plan15, planAWQ, week3, detailedLessons15) → keep the ones you use |

**AI agent demo**

| More relevant | Less relevant |
|---------------|----------------|
| context.md, understandTask.md, taskOrientation.md, focusReading.md | Duplicate logs (e.g. demo-Simon's MacBook Pro.log → .gitignore or delete) |
| StudyGuideAWQ.md (if agents use it) | extractFilterRef.md, Ho2025.md → **More** if core to demo; **Less** if only for one exercise |
| focusedReading/*.md (papers used in demo) | teacherJumpIntoWater vs. MockPractice/JumpWaterAgain: very similar content → treat one as canonical, other as duplicate |
| MockPractice: practice1.md, practice1-abridged.md, setQuestion.md | JumpWaterAgain: many iterations (detailedPlan, 02, 03; linearPoints, 02; prep, synthesisPlan) → keep **one** final version + maybe prep; archive the rest |

**RealMat**

| More relevant | Less relevant |
|---------------|----------------|
| INVENTORY.md, populate_from_inventory.py, organize_layer2.py | Everything under ConceptSkillLesson/**archive**/ (copies of AIagentDemo + lessons) |
| FromCourseTeam (official instructions, rubrics) | Multiple copies of same reading/synthesis docs in archive/ReadingAndSynthesis |

### 4.3 Suggested “keep one, archive rest” list

Use this to tick decisions as you go:

| Doc or group | Suggestion | Your decision |
|--------------|------------|---------------|
| Study Guide AWQ | Keep **one** (e.g. teaching/materials/ + PDF); remove from Week6AWQ root, AIagentDemo duplicate | ☐ |
| detailedPlan / detailedPlan02 / detailedPlan03 (teacher + JumpWaterAgain) | Keep **latest** (03?) or one synthesis doc; archive 01, 02 | ☐ |
| linearPoints vs linearPoints02 | Keep both only if both used; else keep 02, archive linearPoints | ☐ |
| demo.log vs demo-Simon's MacBook Pro.log | Keep one; .gitignore or delete the other | ☐ |
| task1.html vs task1_moodle.html | Keep the version you post (likely moodle); archive or delete the other | ☐ |
| practice1.md vs practice1-abridged.md | Keep both if both used; else keep one | ☐ |
| RealMat archive/ (LessonContent, MoodleTasks, ReadingAndSynthesis, WeeklyPlans, Other) | Keep as **read-only** copy from INVENTORY; don’t edit there | ☐ |
| Week1-5_AWQ: plan15, planAWQ, week3, detailedLessons15 | Keep the 1–2 you actually use for planning; archive the rest | ☐ |

### 4.4 Summary rule

- **More relevant** = one canonical place, easy to find (teaching/ or AIagentDemo/), current and actively used.
- **Less relevant** = one copy in archive or RealMat, or delete duplicates; don’t keep 2–3 copies in different folders.

---

## 5. Step-by-step simplification (manageable sub-tasks)

### Step 1 — Create `teaching/` and move (no delete yet)
- Create `teaching/plans/`, `teaching/moodle/`, `teaching/mat/`, `teaching/materials/`.
- Move:
  - `lessons/Plans/**` → `teaching/plans/`
  - `lessons/Moodle_posts/**` → `teaching/moodle/`
  - `lessons/Mat/**` → `teaching/mat/`
  - `materials/course materials in MD/*` → `teaching/materials/`
  - `materials/Week1-5_AWQ/*` → e.g. `teaching/plans/Week1-5_AWQ/` (or keep under materials if you prefer)
- **Checkpoint:** Run a quick check: links in README/start.md still work or update them. Then get your feedback before Step 2.

### Step 2 — Merge Week6AWQ into teaching
- Move Week6AWQ Study Guide PDF, coordinator email, InputProcessOutputModel into `teaching/materials/` (or a `teaching/materials/Week6/` subfolder).
- Optionally keep `Week6AWQ/OCR/` as `teaching/Week6AWQ-OCR/` if you still use it; else archive.
- **Checkpoint:** Confirm nothing else references `Week6AWQ/` by path; then get your feedback.

### Step 3 — Treat RealMat as single derived copy
- Update RealMat **INVENTORY.md** so sources point to `teaching/` and `AIagentDemo/` (not `lessons/`, `materials/`, `Week6AWQ/`).
- Run `populate_from_inventory.py` (and AWQ `organize_layer2.py` if you use layer2).
- **Checkpoint:** Spot-check a few key files in RealMat; then get your feedback.

### Step 4 — Remove or archive old top-level folders
- After you’re happy with `teaching/` and RealMat:
  - Delete or archive `lessons/` and `materials/` (content now in `teaching/`).
  - Remove or archive empty or redundant `Week6AWQ/` (content in `teaching/`).
- **Checkpoint:** Final check that all links and scripts (e.g. organize_layer2.py, INVENTORY) use new paths.

### Step 5 — Trim AIagentDemo (optional)
- If you want to reduce AIagentDemo size: remove duplicate or obsolete .md/.log (e.g. keep one `demo.log`; drop `demo-Simon's MacBook Pro.log` from repo or add to .gitignore). No need to remove entire subfolders if they’re the canonical source for reading/synthesis and MockPractice.

---

## 6. “Minimum you need” summary

- **For teaching:** Use only **teaching/** (plans, moodle, mat, materials). Ignore RealMat for day-to-day teaching prep.
- **For AI agent demo:** Use only **AIagentDemo/** (focusedReading, MockPractice, teacherJumpIntoWater, key .md). Point agents at this folder.
- **For course-team / rubrics / official stuff:** Keep in **RealMat/FromCourseTeam** (or under teaching if you prefer one tree) and update INVENTORY accordingly.
- **For student-facing guides:** **studentHandsOn/** and **SimonWebsite/** stay as they are.

---

## 7. Quick reference after simplification

| I want to… | Look here |
|------------|-----------|
| Edit week plans or Moodle tasks | `teaching/plans/`, `teaching/moodle/` |
| Use course modules / Study Guide / sample AWQ | `teaching/materials/` |
| Run or edit AI agent demo materials | `AIagentDemo/` |
| Regenerate RealMat from canonical sources | Edit `RealMat/INVENTORY.md`, run `populate_from_inventory.py` (+ `organize_layer2.py`) |
| Student hands-on guides | `studentHandsOn/` |
| Student system / dashboard docs | `SimonWebsite/` |

---

*Created to reduce folder and material overload in UCLC1008. Do Step 1, then review and decide whether to continue with Steps 2–5.*
