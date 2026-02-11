# Past project work — Bus Stop Merge (Fall 2025, Team 6)

Summary of GCAP 3226 Fall 2025 Team 6 work on bus stop merge and optimization, for reuse and adaptation in Spring 2026.

---

## Core research question (Fall 2025)

**To what extent does the Hong Kong Transport Department use data-driven approaches in bus stop placement, merging decisions, and urban transportation optimization?**

Focus areas: bus stop placement efficiency, merge candidate identification, passenger accessibility, service level maintenance.

---

## What the team did

### 1. Government enquiry (Code on Access to Information)

- **Recipient:** Access to Information Officer, Transport Department.
- **Sample requests:**
  - Quantitative data used for bus stop placement and merging (e.g. ridership, passenger flow, accessibility metrics).
  - Public reports or SOPs for bus stop optimization and accessibility maintenance.
  - Data-driven criteria for evaluating effectiveness and future optimization.

### 2. Real-time API data and analysis

- **Data:** Hong Kong Government Open Data APIs for real-time bus tracking; rush hours (7–9 AM, 5–7 PM).
- **Deliverables included:** Queue analysis reports, rush-hour statistics, long-gap and arrival CSVs, cluster analysis, simulation HTML.
- **Methods:** Real-time bus movement tracking, spatial proximity of nearby stops, coordination opportunity analysis.

### 3. Mathematical and simulation framework

- **Simulation:** Spatial optimization (objective: minimise weighted distance + cost; constraints: accessibility, service coverage, max distance for merged stops). Passenger flow dynamics and service efficiency metrics (wait time, travel time, frequency, capacity utilisation).
- **Scenarios:** Baseline; conservative merging (e.g. within 100 m, 95% coverage); aggressive (e.g. 200 m, 90% coverage); hybrid by passenger flow.
- **Technical:** Python, discrete-event simulation, queuing theory, KMB Open Data API; Jupyter notebooks.
- **Case study:** St. Martin Road and Chong San Road stations (52 m apart) — merger optimization and trade-offs.

### 4. Report structure (outline v3)

- Introduction (research context, objectives, questions, significance).
- Real-time API data collection and analysis (API strategy, rush-hour patterns, nearby-stop coordination).
- TD decision-making process evaluation (how placement/merging decisions are made).
- Bus stop placement principles framework (evidence-based principles for TD and operators).
- Mathematical models and simulation (integration of API data with optimization).
- Recommendations and conclusion.

---

## Reusable elements for Spring 2026

| Element | Use |
|--------|-----|
| **Government enquiry template** | Adapt for Transport Department request (Code on Access to Information). |
| **Simulation framework** | Spatial optimization, passenger flow, efficiency metrics (see math note). |
| **API strategy** | data.gov.hk / real-time bus APIs; rush-hour focus; nearby-stop spatial analysis. |
| **Scenario design** | Baseline vs conservative / aggressive / hybrid merging; sensitivity by peak hour and demographics. |
| **Report outline** | Structure for “real-time data + TD process + placement principles + recommendations”. |

---

## Key deliverables (Fall 2025)

- Project roadmap (weeks 5–13): planning, fieldwork, model choice (regression vs simulation), reporting.
- Math note: simulation framework (objectives, constraints, flow dynamics, KPIs, scenarios).
- Bus-Stop-Optimization case: St. Martin / Chong San Road, Python simulation, four scenarios.
- Project report outlines v1–v3; queue analysis reports; rush-hour statistics; simulation.html.

---

## Data and tools

- **Primary:** Transport Department data (Code on Access to Information); ridership by stop; origin–destination patterns.
- **Secondary:** data.gov.hk; Transport Department annual reports; literature on urban transport optimization.
- **Models:** Regression (ridership prediction) or simulation (bus stop optimization, passenger flow).
- **Tech:** Python, Jupyter, real-time APIs, GIS/spatial analysis, discrete-event simulation.

---

*Source: GCAP 3226 Fall 2025 Team 6 (Team6_BusStopMerge). Use this as reference only; adapt to your own scope and data.*
