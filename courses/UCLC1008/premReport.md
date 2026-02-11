# UCLC1008 Codebase Structure Report

## Overview

The [`courses/UCLC1008`](courses/UCLC1008) directory contains a comprehensive collection of materials for **UCLC1008 (University English I)**, organized to support both teaching and AI-assisted student learning. The codebase is designed to showcase how **Gen AI agents** can help students with academic reading and writing, particularly for three major assessments: **AWQ** (Academic Writing Quiz), **ACE** (Argumentation Construction and Evaluation), and **CRAA** (Critical Reading and Argument Analysis).

**Purpose**: Selected materials for the **genAI2026** AI ambassador programme at HKBU, demonstrating AI-powered academic support for university English students.

---

## Directory Structure

### Root Level Files

- [`README.md`](courses/UCLC1008/README.md) — Main overview explaining how Gen AI agents can help students with tasks like understanding rubrics, drafting, revising, and practice
- [`start.md`](courses/UCLC1008/start.md) — Quick start guide pointing to key materials and overview
- [`simplifySolution.md`](courses/UCLC1008/simplifySolution.md) — Simplification strategies or solutions

---

## Major Subdirectories

### 1. [`RealMat/`](courses/UCLC1008/RealMat) — Organized Course Materials ⭐

**Purpose**: A curated, systematically organized copy of all course materials, structured by assessment type and content category.

**Key Features**:
- **Three-tier organization**: Area → Subfolder → (for AWQ: second layer)
- **Automated maintenance**: Python scripts manage file organization
- **Original paths preserved**: Existing prompts referencing old paths still work

#### Structure

```
RealMat/
├── INVENTORY.md              # Master list: source path → (Area, Subfolder)
├── README.md                 # Organization explanation
├── populate_from_inventory.py # Copies files from inventory into organized structure
├── AWQ/                      # Academic Writing Quiz (Weeks 1-6) — 109 files
│   ├── LAYER2_MAP.md        # Second-layer organization guide
│   ├── organize_layer2.py   # Sorts AWQ files into second layer
│   ├── README.md            # AWQ-specific navigation guide
│   ├── FromCourseTeam/
│   │   ├── Instructions/    # Quiz instructions, coordinator emails
│   │   ├── Modules/         # UE1 Module 1 & 2 (course content)
│   │   └── RubricsAndCalendar/ # Rubrics, academic calendar
│   ├── ExamTipsPractice/
│   │   ├── Samples/         # Sample AWQ papers and student answers
│   │   ├── StudyGuides/     # Study guides to AWQ
│   │   └── MockPractice/    # Practice tasks, word-count quiz
│   └── ConceptSkillLesson/
│       ├── skills4AWQ.md    # Main student reference for techniques
│       ├── README.md        # Points to skills and archive
│       └── archive/         # All original lesson materials
│           ├── LessonContent/      # week1-5, week1.1-5.3
│           ├── MoodleTasks/        # W3H1/W3H3 task HTML
│           ├── WeeklyPlans/        # plan_week*, planAWQ, plan15
│           ├── ReadingAndSynthesis/ # Reading demos, synthesis plans
│           └── Other/              # READMEs, samples
├── ACE/                      # Argumentation Construction & Evaluation (Weeks 6-9) — 9 files
│   ├── FromCourseTeam/      # ACE instructions, reflection guidelines
│   ├── ExamTipsPractice/    # Sample ACE drafts, study guides
│   └── ConceptSkillLesson/  # Lesson plans
└── CRAA/                     # Critical Reading & Argument Analysis (Weeks 10-13) — 5 files
    ├── FromCourseTeam/      # CRAA instructions, topics
    ├── ExamTipsPractice/    # Sample CRAA
    └── ConceptSkillLesson/  # Lesson plans
```

**Maintenance Workflow**:
1. Edit [`INVENTORY.md`](courses/UCLC1008/RealMat/INVENTORY.md) to add/move/remove items
2. Run [`populate_from_inventory.py`](courses/UCLC1008/RealMat/populate_from_inventory.py) to refresh copies
3. For AWQ: Run [`organize_layer2.py`](courses/UCLC1008/RealMat/AWQ/organize_layer2.py) to sort into second layer

---

### 2. [`AIagentDemo/`](courses/UCLC1008/AIagentDemo) — AI Agent Demonstrations

**Purpose**: Showcases practical AI agent workflows for helping students prepare for assessments.

#### Subdirectories

**[`focusedReading/`](courses/UCLC1008/AIagentDemo/focusedReading)**
- Academic paper summaries and analyses
- Files: [`Ho2025.md`](courses/UCLC1008/AIagentDemo/focusedReading/Ho2025.md), [`Laestadius2022.md`](courses/UCLC1008/AIagentDemo/focusedReading/Laestadius2022.md), [`LiZhang2024.md`](courses/UCLC1008/AIagentDemo/focusedReading/LiZhang2024.md), [`Skjuve2021.md`](courses/UCLC1008/AIagentDemo/focusedReading/Skjuve2021.md), [`Xie2023.md`](courses/UCLC1008/AIagentDemo/focusedReading/Xie2023.md), [`XiePentina2022.md`](courses/UCLC1008/AIagentDemo/focusedReading/XiePentina2022.md)
- [`focusReading.md`](courses/UCLC1008/AIagentDemo/focusedReading/focusReading.md) — Guide for focused reading strategies

**[`MockPractice/`](courses/UCLC1008/AIagentDemo/MockPractice)**
- Complete mock AWQ practice workflow
- Key files:
  - [`context.md`](courses/UCLC1008/AIagentDemo/MockPractice/context.md) — Teaching context (quiz date: Feb 27, topic: AI chatbots impact)
  - [`ExcerptsOnly.md`](courses/UCLC1008/AIagentDemo/MockPractice/ExcerptsOnly.md) — Extracted excerpts for practice
  - [`generateOutline.md`](courses/UCLC1008/AIagentDemo/MockPractice/generateOutline.md), [`newOutline.md`](courses/UCLC1008/AIagentDemo/MockPractice/newOutline.md), [`outline4twoexcerpts.md`](courses/UCLC1008/AIagentDemo/MockPractice/outline4twoexcerpts.md) — Outline generation
  - [`rubrics.md`](courses/UCLC1008/AIagentDemo/MockPractice/rubrics.md) — Assessment rubrics
  - [`StudyGuideAWQ.md`](courses/UCLC1008/AIagentDemo/MockPractice/StudyGuideAWQ.md) — Study guide
  - [`taskOrientation.md`](courses/UCLC1008/AIagentDemo/MockPractice/taskOrientation.md) — Task understanding
  - [`task_answer_sheet_edit.md`](courses/UCLC1008/AIagentDemo/MockPractice/task_answer_sheet_edit.md) — Answer sheet editing
  - [`one-side-answer-sheet.pdf`](courses/UCLC1008/AIagentDemo/MockPractice/one-side-answer-sheet.pdf) — PDF answer sheet

**[`answerSheet/`](courses/UCLC1008/AIagentDemo/MockPractice/answerSheet)**
- Python tooling for generating answer sheets
- [`create_two_sided.py`](courses/UCLC1008/AIagentDemo/MockPractice/answerSheet/create_two_sided.py) — Script to create two-sided PDFs
- [`requirements.txt`](courses/UCLC1008/AIagentDemo/MockPractice/answerSheet/requirements.txt) — Python dependencies
- [`process.log`](courses/UCLC1008/AIagentDemo/MockPractice/answerSheet/process.log) — Processing logs
- PDFs: [`one-side-answer-sheet.pdf`](courses/UCLC1008/AIagentDemo/MockPractice/answerSheet/one-side-answer-sheet.pdf), [`two-side-answer-sheet.pdf`](courses/UCLC1008/AIagentDemo/MockPractice/answerSheet/two-side-answer-sheet.pdf)
- Images: [`centered_page.png`](courses/UCLC1008/AIagentDemo/MockPractice/answerSheet/centered_page.png), [`page_preview.png`](courses/UCLC1008/AIagentDemo/MockPractice/answerSheet/page_preview.png)

**[`archive/`](courses/UCLC1008/AIagentDemo/MockPractice/archive)**
- Historical iterations and experiments
- Subfolders: [`JumpWaterAgain/`](courses/UCLC1008/AIagentDemo/MockPractice/archive/JumpWaterAgain), [`teacherJumpIntoWater/`](courses/UCLC1008/AIagentDemo/MockPractice/archive/teacherJumpIntoWater)
- Contains: detailed plans, linear points, synthesis plans, practice materials, conversion scripts

---

### 3. [`lessons/`](courses/UCLC1008/lessons) — Lesson Materials

**Purpose**: Teaching materials including lesson plans, Moodle posts, and sample materials.

#### Structure

**[`Mat/`](courses/UCLC1008/lessons/Mat)**
- Sample AWQ materials in multiple formats
- [`UCLC1008 (2526a) Sample AWQ (Student).md`](courses/UCLC1008/lessons/Mat/UCLC1008 (2526a) Sample AWQ (Student).md)
- [`UCLC1008_2526a_Sample_AWQ_Student.md`](courses/UCLC1008/lessons/Mat/UCLC1008_2526a_Sample_AWQ_Student.md)
- [`README_OPENING_FILES.md`](courses/UCLC1008/lessons/Mat/README_OPENING_FILES.md)

**[`Moodle_posts/`](courses/UCLC1008/lessons/Moodle_posts)**
- HTML content for Moodle forum tasks
- Root: [`task1.html`](courses/UCLC1008/lessons/Moodle_posts/task1.html), [`task2.html`](courses/UCLC1008/lessons/Moodle_posts/task2.html), [`task1_moodle.html`](courses/UCLC1008/lessons/Moodle_posts/task1_moodle.html), [`task2_moodle.html`](courses/UCLC1008/lessons/Moodle_posts/task2_moodle.html)
- **[`week3/`](courses/UCLC1008/lessons/Moodle_posts/week3)** — 10 tasks covering:
  - Title analysis, abstract structure, purpose statements, section headings, topic sentences
  - Paraphrasing strategies, avoiding plagiarism, summarising, avoiding personal bias, main idea coverage
  - READMEs: [`README_W3H1_tasks.md`](courses/UCLC1008/lessons/Moodle_posts/week3/README_W3H1_tasks.md), [`README_W3H3_tasks.md`](courses/UCLC1008/lessons/Moodle_posts/week3/README_W3H3_tasks.md)
- **[`week4/`](courses/UCLC1008/lessons/Moodle_posts/week4)**, **[`week5/`](courses/UCLC1008/lessons/Moodle_posts/week5)**, **[`week6/`](courses/UCLC1008/lessons/Moodle_posts/week6)** — Each with [`README.md`](courses/UCLC1008/lessons/Moodle_posts/week4/README.md)

**[`Plans/`](courses/UCLC1008/lessons/Plans)**
- Weekly lesson plans organized by week
- **[`week3/`](courses/UCLC1008/lessons/Plans/week3)**: [`plan_week3_week4_Mat_Mod1Mod2.md`](courses/UCLC1008/lessons/Plans/week3/plan_week3_week4_Mat_Mod1Mod2.md)
- **[`week4/`](courses/UCLC1008/lessons/Plans/week4)**: [`plan_week4_Mod2Mod3.md`](courses/UCLC1008/lessons/Plans/week4/plan_week4_Mod2Mod3.md), [`README.md`](courses/UCLC1008/lessons/Plans/week4/README.md)
- **[`week5/`](courses/UCLC1008/lessons/Plans/week5)**: [`plan_week5_AWQ_argumentation.md`](courses/UCLC1008/lessons/Plans/week5/plan_week5_AWQ_argumentation.md), [`README.md`](courses/UCLC1008/lessons/Plans/week5/README.md)
- **[`week6/`](courses/UCLC1008/lessons/Plans/week6)**: [`plan_week6_H1_AWQ_prep.md`](courses/UCLC1008/lessons/Plans/week6/plan_week6_H1_AWQ_prep.md), [`README.md`](courses/UCLC1008/lessons/Plans/week6/README.md)

---

### 4. [`materials/`](courses/UCLC1008/materials) — Course Materials

**Purpose**: Core course content including modules, instructions, and study guides.

**[`course materials in MD/`](courses/UCLC1008/materials/course materials in MD)**
- [`Academic Writing Quiz Instructions.md`](courses/UCLC1008/materials/course materials in MD/Academic Writing Quiz Instructions.md)
- [`Sample Academic Writing Quiz.md`](courses/UCLC1008/materials/course materials in MD/Sample Academic Writing Quiz.md)
- [`Sample Academic Writing Quiz (Student_Answer).md`](courses/UCLC1008/materials/course materials in MD/Sample Academic Writing Quiz (Student_Answer).md)
- [`Study Guide to Academic Writing Quiz.md`](courses/UCLC1008/materials/course materials in MD/Study Guide to Academic Writing Quiz.md)
- [`StudyGuideAWQ.md`](courses/UCLC1008/materials/course materials in MD/StudyGuideAWQ.md)
- [`UE1 (2526B) Module 1 (v2_20251216).md`](courses/UCLC1008/materials/course materials in MD/UE1 (2526B) Module 1 (v2_20251216).md) — Components of academic articles
- [`UE1 (2526B) Module 2 (v1_20251214).md`](courses/UCLC1008/materials/course materials in MD/UE1 (2526B) Module 2 (v1_20251214).md) — Paraphrasing, summarising, synthesising

**[`Week1-5_AWQ/`](courses/UCLC1008/materials/Week1-5_AWQ)**
- [`plan15.md`](courses/UCLC1008/materials/Week1-5_AWQ/plan15.md) — 15-lesson plan
- [`planAWQ.md`](courses/UCLC1008/materials/Week1-5_AWQ/planAWQ.md) — AWQ preparation plan
- [`week3.md`](courses/UCLC1008/materials/Week1-5_AWQ/week3.md) — Week 3 specific content

---

### 5. [`SimonWebsite/`](courses/UCLC1008/SimonWebsite) — Student-Facing Materials

**Purpose**: Content fetched from https://github.com/tesolchina/uclc1008 for student use.

**[`MD/`](courses/UCLC1008/SimonWebsite/MD)** — All official documents (30+ files)
- Instructions: AWQ, ACE, CRAA, Pre-course Writing, Reflective Learning Portfolio
- Samples: Sample AWQ, Sample ACE Draft, Sample CRAA (with student answers)
- Study Guides: Study Guide to AWQ, Study Guide to ACE Draft
- Course Content: UE1 Module 1 & 2, Rubrics, Academic Calendar
- Reflection: Reflection on AI Use in ACE Final

**[`Week1-5_AWQ/`](courses/UCLC1008/SimonWebsite/Week1-5_AWQ)**
- Weekly materials: [`week1.md`](courses/UCLC1008/SimonWebsite/Week1-5_AWQ/week1.md) through [`week5.md`](courses/UCLC1008/SimonWebsite/Week1-5_AWQ/week5.md)
- Plans: [`planAWQ.md`](courses/UCLC1008/SimonWebsite/Week1-5_AWQ/planAWQ.md), [`plan15.md`](courses/UCLC1008/SimonWebsite/Week1-5_AWQ/plan15.md), [`originalPlanAWQ.md`](courses/UCLC1008/SimonWebsite/Week1-5_AWQ/originalPlanAWQ.md), [`revisePlan.md`](courses/UCLC1008/SimonWebsite/Week1-5_AWQ/revisePlan.md)
- Detailed lessons: [`detailedLessons15.md`](courses/UCLC1008/SimonWebsite/Week1-5_AWQ/detailedLessons15.md), [`sampleLessonbuild.md`](courses/UCLC1008/SimonWebsite/Week1-5_AWQ/sampleLessonbuild.md)
- [`sample_paraphrasing.html`](courses/UCLC1008/SimonWebsite/Week1-5_AWQ/sample_paraphrasing.html)
- **[`lesson15/`](courses/UCLC1008/SimonWebsite/Week1-5_AWQ/lesson15)** — 15 individual lessons (week1.1 through week5.3)

**[`week6-9_ACE/`](courses/UCLC1008/SimonWebsite/week6-9_ACE)**
- [`plan.md`](courses/UCLC1008/SimonWebsite/week6-9_ACE/plan.md) — ACE lesson plan

**[`week10-13_CRAA/`](courses/UCLC1008/SimonWebsite/week10-13_CRAA)**
- [`plan.md`](courses/UCLC1008/SimonWebsite/week10-13_CRAA/plan.md) — CRAA lesson plan

**[`docs/student-system/`](courses/UCLC1008/SimonWebsite/docs/student-system)**
- Technical documentation for student system integration
- [`README.md`](courses/UCLC1008/SimonWebsite/docs/student-system/README.md), [`database-schema.md`](courses/UCLC1008/SimonWebsite/docs/student-system/database-schema.md), [`integration-guide.md`](courses/UCLC1008/SimonWebsite/docs/student-system/integration-guide.md), [`student-dashboard-module.md`](courses/UCLC1008/SimonWebsite/docs/student-system/student-dashboard-module.md), [`student-id-module.md`](courses/UCLC1008/SimonWebsite/docs/student-system/student-id-module.md)

**[`fetch.md`](courses/UCLC1008/SimonWebsite/fetch.md)** — Documentation on fetching process

---

### 6. [`studentHandsOn/`](courses/UCLC1008/studentHandsOn) — Student Practice Guides

**Purpose**: Hands-on guides for students to explore AI agent use cases for AWQ preparation.

**Files**:
- [`generateGuides.md`](courses/UCLC1008/studentHandsOn/generateGuides.md) — Instructions for generating student guides
- [`guide01.md`](courses/UCLC1008/studentHandsOn/guide01.md) through [`guide06.md`](courses/UCLC1008/studentHandsOn/guide06.md) — Six different use case guides

**Purpose** (from generateGuides.md): Guide students to explore different use cases of using AI agents to prepare for AWQ, playing the role of a creative human coach.

---

### 7. [`Week6AWQ/`](courses/UCLC1008/Week6AWQ) — Week 6 Specific Materials

- [`emailFromCourseCoordinator.md`](courses/UCLC1008/Week6AWQ/emailFromCourseCoordinator.md) — Communication from course coordinator

---

## Key Design Principles

### 1. **Dual Organization System**
- **Original folders** remain unchanged for backward compatibility
- **RealMat/** provides organized, curated copies for easier navigation
- Automated scripts maintain synchronization

### 2. **Assessment-Centric Structure**
Materials organized around three major assessments:
- **AWQ** (Academic Writing Quiz) — Weeks 1-6, most extensive (109 files)
- **ACE** (Argumentation Construction & Evaluation) — Weeks 6-9
- **CRAA** (Critical Reading & Argument Analysis) — Weeks 10-13

### 3. **Three-Category Classification**
Each assessment area contains:
- **FromCourseTeam** — Official instructions, rubrics, modules
- **ExamTipsPractice** — Samples, study guides, mock practice
- **ConceptSkillLesson** — Lesson plans, weekly content, Moodle tasks

### 4. **AI Agent Integration**
- Demonstrates practical AI workflows through [`AIagentDemo/`](courses/UCLC1008/AIagentDemo)
- Provides context for AI-assisted learning
- Includes student hands-on guides for self-directed AI exploration

### 5. **Multi-Format Support**
- Markdown (.md) for easy editing and version control
- HTML for Moodle integration
- PDF for printable materials
- Python scripts for automation

---

## Technical Components

### Python Scripts

1. **[`populate_from_inventory.py`](courses/UCLC1008/RealMat/populate_from_inventory.py)**
   - Parses [`INVENTORY.md`](courses/UCLC1008/RealMat/INVENTORY.md)
   - Copies files from source locations to organized structure
   - Handles duplicate basenames with path-based prefixes
   - Ignores "Unclassified" section

2. **[`organize_layer2.py`](courses/UCLC1008/RealMat/AWQ/organize_layer2.py)**
   - Sorts AWQ files into second-layer subfolders
   - Provides finer-grained organization for the largest assessment area

3. **[`create_two_sided.py`](courses/UCLC1008/AIagentDemo/MockPractice/answerSheet/create_two_sided.py)**
   - Generates two-sided PDF answer sheets
   - Supports mock practice workflow

---

## Content Statistics

- **Total files**: 200+ files across all directories
- **AWQ materials**: 109 files (most extensive)
- **ACE materials**: 9 files
- **CRAA materials**: 5 files
- **AI demos**: 50+ files in AIagentDemo/
- **Student guides**: 6 hands-on guides
- **Lesson plans**: 10+ weekly plans
- **Moodle tasks**: 10+ HTML task files

---

## Use Cases for AI Agents

Based on [`README.md`](courses/UCLC1008/README.md), AI agents can help students with:

1. **Understanding tasks**: Explain requirements using plans and Moodle task HTML (e.g., "synthesise both sources," "no personal bias," "APA citations")

2. **Using rubrics**: Reference AWQ rubric criteria (Summary Accuracy, Synthesis, Paraphrasing, Academic Tone, In-text Citations) when reviewing drafts

3. **Drafting and revising**: Suggest structure using Module 1 & 2 and Sample AWQ (thesis, topic sentences, conclusion, paraphrasing, synthesis language)

4. **Practice**: Direct students to relevant Moodle tasks and materials for targeted skill development

---

## Maintenance Workflow

1. **Adding new materials**:
   - Add source path and classification to [`INVENTORY.md`](courses/UCLC1008/RealMat/INVENTORY.md)
   - Run `python3 populate_from_inventory.py`
   - For AWQ: Run `python3 organize_layer2.py`

2. **Updating existing materials**:
   - Edit files in original locations
   - Re-run population scripts to sync to RealMat/

3. **Reorganizing**:
   - Update [`INVENTORY.md`](courses/UCLC1008/RealMat/INVENTORY.md) classifications
   - Re-run scripts to reflect new organization

---

## Integration Points

- **Moodle**: HTML files in [`lessons/Moodle_posts/`](courses/UCLC1008/lessons/Moodle_posts) ready for forum posting
- **GitHub**: Content sourced from https://github.com/tesolchina/uclc1008
- **Student website**: Materials in [`SimonWebsite/`](courses/UCLC1008/SimonWebsite) for student access
- **AI systems**: Structured markdown enables easy parsing and context provision for AI agents

---

## Summary

The UCLC1008 codebase is a well-organized, multi-layered repository designed to support both traditional teaching and AI-enhanced learning. Its dual organization system (original + curated), assessment-centric structure, and comprehensive automation make it an effective platform for demonstrating AI agent capabilities in academic support. The extensive AWQ materials, practical AI demonstrations, and student-facing guides provide a complete ecosystem for teaching academic writing with AI assistance.
