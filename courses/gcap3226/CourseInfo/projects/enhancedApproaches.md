# Enhanced Project Approaches — GCAP 3226

*Based on [Approaches.md](Approaches.md) and aligned with [Week 1–3](genAI2026/courses/gcap3226/week1-3) content.*

---

## Core question

**To what extent did HK government staff make their decisions informed by data?**

---

## Project workflow (7 steps) — with actionable insights

### Step 1: Identify a government decision

- **Action:** Choose one or more decisions that are **concrete and specific** (e.g. a named policy, programme, or implementation detail).
- **Insight:** Use the [course project topics](README.md) (flu shot, colorectal screening, road safety, eMPF, CDCC, rodent control, bus stop merge) to anchor your choice. Align with SDGs and course themes (data governance, transparency).
- **Tool:** Government and Legco websites; AI agent can help search **Legco.gov.hk** and **gov.hk** for decisions and meeting minutes.

### Step 2: Review the decision — room for improvement

- **Action:** Ask: *In what ways is this decision controversial or disputable?* Document gaps (e.g. lack of data, unclear criteria, inconsistent implementation).
- **Insight:** Controversy or dispute is your entry point for asking for data and for recommending change. Frame it as “room for improvement” to keep the tone constructive.
- **Resource:** [Curating public data](https://gcap3226.hkbu.tech/spring-2026/resources/curating-public-data) — focus on **decision-making process** and **how data is managed**.

### Step 3: Search and curate public information

- **Action:** Systematically collect government and Legco documents (reports, meeting minutes, press releases). Focus on: *How was the decision made? What data was used? How is data managed?*
- **Insight:** Use the **government telephone directory** (not only 1823) to identify named staff; this supports targeted information requests later.
- **Tool:** AI agent to search Legco.gov.hk / gov.hk; organise findings in a shared folder (e.g. GitHub repo or Moodle) so the group can reference the same sources.

### Step 4: Raise questions under the Code on Access to Information

- **Action:** Draft a clear, specific request to the relevant department. State: (1) the decision or policy you are asking about, (2) what information or data you need, (3) why it matters for understanding data-informed decision-making. Cite the **Code on Access to Information** where helpful.
- **Timeline:** Expect **about 3 weeks** for a response; allow up to **7 weeks** in planning.
- **Resource:** [Government information requests](https://gcap3226.hkbu.tech/spring-2026/resources/government-info-requests).
- **Insight:** Send early (e.g. in Weeks 3–4) so responses can inform your analysis and fieldwork.

### Step 5: Collect community data (in parallel)

- **Action:** Design a small-scale data collection (e.g. survey, site observations, counts) to better understand the problem and data management on the ground. Use the **fieldwork allowance** (HK$300 per student; submit by Week 6).
- **Insight:** This data does not need to be nationally representative. Its value is to **shed light** on the issue and complement government data — e.g. uptake rates, local conditions, user experience.

### Step 6: Analyse data and make recommendations

- **Action:** Use **math tools** and **visualization tools** (from Weeks 1–2) to analyse:
  - Data you collected (Step 5)
  - Information received from government (Step 4)
  - Curated public documents (Step 3)
- **Output:** Clear recommendations on how decision-making could become **more data-driven** (e.g. what data to collect, how to publish it, how to use it in decisions).
- **Insight:** Link every chart or number to a **clear question** (e.g. “What does this survey show about uptake?”) so the report is persuasive to lawmakers.

### Step 7: Present to Legco via the Redress System

- **Action:** Prepare the **group report** (~3,000 words) and **poster**; rehearse and deliver **two presentations**. Frame the submission as a **complaint** about government data governance under the Legco Redress System.
- **Resource:** [Handling cases under the Redress System](https://www.legco.gov.hk/en/legco-business/redress-system/handling-cases-received-under-redress-system.html).

---

## Suggested math and analytical tools

*(Aligned with Week 1–3: optimization, regression, simulation, data visualization.)*

| Tool / concept | Use in your project | When to use it |
|----------------|---------------------|----------------|
| **Optimization** (e.g. minimise cost, maximise uptake, shortest path) | Bus stop placement, route design; resource allocation (e.g. vaccination sites); rodent control resource allocation. | When a decision has a clear objective (e.g. “minimise waiting time”) and constraints (e.g. budget, locations). |
| **Simulation** | Test “what if” scenarios (e.g. different flu campaign strategies, different screening schedules) without real-world experimentation. | When you want to explore outcomes under different assumptions before making recommendations. |
| **Linear regression** | Relate one variable to another (e.g. uptake vs. publicity spend; accidents vs. road design). | When you have numeric data and want to quantify relationships for your report. |
| **Data visualization** (e.g. Python + pandas/matplotlib in Jupyter) | Turn CSV/survey data and government statistics into charts (bar, line, scatter) that support your narrative. | Throughout analysis; use **vibe coding** (Ask then Agent mode) to generate and refine code. |
| **Descriptive statistics** (mean, median, rates, proportions) | Summarise survey results, participation rates, incident counts by district or time. | First step in analysing any dataset; often combined with visualizations. |
| **Comparison across groups** (e.g. by district, by year) | Compare uptake, accidents, or complaints across areas or time periods to identify inequities or trends. | When you have categorical or time-based data and want to show variation. |

**Practical tip:** Use **VS Code + Jupyter + Python** (Week 2 setup). Keep CSV and notebook in the **same folder**; use AI to write and fix code. Start with **Ask mode** to learn, then **Agent mode** for speed.

---

## Checklist (Weeks 3–4)

- [ ] Group formed; policy area and specific decision(s) agreed.
- [ ] First information request drafted and sent (Code on Access to Information).
- [ ] Public sources (Legco, gov.hk) curated and stored in a shared place.
- [ ] Technical setup complete (VS Code, GitHub, Jupyter, Python) for data work.
- [ ] At least one simple visualization produced from a CSV (e.g. Week 2 task).

---

## References

- [Approaches.md](Approaches.md) — original 7-step workflow  
- [Week 1 summary](genAI2026/courses/gcap3226/week1-3/week1-summary.md) — course identity, Code on Access to Information, math types  
- [Week 2 summary](genAI2026/courses/gcap3226/week1-3/week2-summary.md) — vibe coding, data visualization, CSV + Jupyter  
- [Week 3 summary](genAI2026/courses/gcap3226/week1-3/week3-summary.md) — group formation, topic selection, first outreach  
- [Project README](README.md) — topics, requirements, fieldwork allowance  
