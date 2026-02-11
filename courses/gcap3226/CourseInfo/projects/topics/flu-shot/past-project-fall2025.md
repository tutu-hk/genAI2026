# Past project work — Flu Shot (Fall 2025, Team 1)

Summary of GCAP 3226 Fall 2025 Team 1 work on flu vaccination campaigns and data-driven policy, for reuse and adaptation in Spring 2026.

---

## Core research question (Fall 2025)

**To what extent does the Hong Kong government use data-driven approaches in flu vaccination campaign planning and resource allocation?**

Focus areas: vaccination coverage by demographics, campaign effectiveness, resource allocation, policy impact assessment, predictive modelling.

---

## What the team did

### 1. Government enquiries (Code on Access to Information)

- **Department of Health** (main): School flu vaccination participation rates (2022–23, 2023–24, 2024–25); data collection methods; eHealth integration. Contact: enquiry_chpweb@dh.gov.hk.
- **Education Bureau:** School-level engagement and data (e.g. for report cards).
- **Health Bureau:** eHealth team linkage for vaccination records and enrolment.
- **Draft template:** Concise, focused request: specific data points (participation by season, age breakdown, collection methods, eHealth tracking). Request connection to eHealth team for enrolment stats and data integration.

### 2. Data requirements for modelling

- **Surveillance:** ILI rates (sentinel, age-stratified, by district); hospital admissions; lab-confirmed cases and strains; mortality.
- **Demographics:** Age distribution, district, socioeconomic factors, healthcare utilisation.
- **Vaccination:** Coverage by age/group, vaccine distribution, timing, effectiveness.
- **Environmental/seasonal:** Temperature, humidity, school calendars, holidays.
- **Sources in HK:** CHP (weekly surveillance, lab, mortality), Hospital Authority, Census and Statistics Department.
- **Modelling use:** Regression (uptake vs demographics, accessibility, campaign timing) or simulation (campaign scenarios, resource allocation).

### 3. School vaccination report card (actionable outline)

- **Goal:** Pressure principals via transparent comparison of vaccination performance and URTI-related absenteeism.
- **Math:** Linear/log-linear regression `URTI_absence = β0 + β1 * vaccination_rate`; school leaderboard by vaccination %, absenteeism, composite “Protection Score”; quartile badges (Gold/Silver/Amber/Red).
- **Data needed:** Weekly vaccination % by class; daily absenteeism by reason (URTI/flu); outreach logs; eHealth enrolment to verify vaccination.
- **Governance:** Standardised school uploads; DH/eHealth confirmation feeds; dashboards for principals and EDB; link to SDA reviews, principal appraisal, funding.
- **Evidence base:** Leung et al. 2017 school surveillance; synthetic datasets for methodology and visuals.

### 4. Vaccine effectiveness (eHealth-enabled)

- **Goal:** Estimate vaccine effectiveness (VE) using eHealth + school data (test-negative design).
- **Model:** Conditional logistic regression: vaccination status (eHealth-verified), lab-confirmed flu vs negative tests, demographics, school-level coverage. Outputs: VE by strain and age; sensitivity by time since vaccination.
- **Evidence base:** Lee et al. 2024, Cowling et al. 2021.
- **Governance:** Health Bureau–led data exchange; consent for linking eHealth with school IDs; DH dashboards for EDB/principals.

### 5. Report structure and deliverables

- Outlines v1–v4; actionable outline (report card + VE + data governance gap analysis).
- School report card methodology; synthetic data and figures (vaccination vs absence, leaderboard, promo regression).
- Literature review (e.g. Leung 2017, Ali et al. 2021, Lee 2024); government enquiry drafts and published letters.

---

## Reusable elements for Spring 2026

| Element | Use |
|--------|-----|
| **DoH email template** | Concise request for school vaccination participation, eHealth integration, CHP data. |
| **Data requirement list** | Checklist for CHP, HA, Census; surveillance, demographics, vaccination, environmental. |
| **Report card idea** | Regression (vaccination → absenteeism); leaderboard; accountability levers (EDB, SDA). |
| **VE / test-negative** | Protocol for eHealth-based VE analysis (if data access is secured). |
| **Roadmap** | Weeks 8–13: send enquiry early; collect secondary data and run surveys while waiting; model choice (regression/simulation); integrate government response; recommendations. |

---

## Key deliverables (Fall 2025)

- Project roadmap: government enquiry by week 8; expected response ~3 weeks; model development with secondary data in parallel.
- Department of Health email draft v2 (school vaccination + eHealth).
- Data requirement document (flu outbreak modelling: surveillance, demographics, healthcare, policy).
- Actionable outline: report card, VE, ideal data governance vs gaps.
- Project report outlines v1–v4; methodology memos; synthetic datasets and figures.

---

## Data and tools

- **Primary:** DoH vaccination records (Code on Access to Information); Census demographics; data.gov.hk; eHealth (if access agreed).
- **Secondary:** CHP reports and press releases; academic literature (Leung 2017, Lee 2024, etc.); government annual reports.
- **Models:** Regression (uptake vs demographics, campaign factors) or simulation (campaign scenarios, resource allocation).
- **Tech:** Python/Jupyter for analysis and visuals; survey for fieldwork.

---

*Source: GCAP 3226 Fall 2025 Team 1 (Team1_FluShot). Use this as reference only; adapt to your own scope and data.*
