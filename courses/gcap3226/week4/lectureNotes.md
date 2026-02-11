# Week 4 Lecture Notes — Simulation & Random Variables
## GCAP 3226 (Feb 4, 2026)

## Snapshot
- **Core theme:** Use data responsibly; question claims, trace data sources, and design evidence-based policy inquiries.
- **Methods:** Random variables + discrete-event simulation (SimPy).
- **Case study:** City Bus Route 56 — route adjustment and seat utilization.

---

## 1) Data literacy warm‑up: “Fewer jobs for graduates” article
- The headline claims a **55% drop** in jobs for graduates.
- The data source is the **Joint Institution Job Information System** (for 8 publicly funded universities).
- Key critique: this dataset **does not represent all graduates** (self‑financed institutions, overseas returnees, other job platforms).
- Takeaway: **always ask “Where is the data? Who is included/excluded?”** before drawing policy conclusions.

---

## 2) Recap: Week 3 regression & visualization feedback
- Last week’s case: **municipal solid waste charging** survey.
- **Key predictors of support** for the policy:
  - Perceived **government responsiveness** (~0.5 coefficient)
  - Perceived **policy fairness**
  - Together explain ~**61%** of variance in support.
- Forward vs. backward regression: **same final predictors**.
- Visualization lesson: **categorical variables** (Likert 1–5) are better shown with **bar charts** than scatterplots.
  - Scatterplots hide stacked counts.
  - Bar charts can show the % support/oppose at each fairness level.

---

## 3) Case study: Bus Route 56 adjustment (North District)
### Policy workflow (Transport Department)
1. Bus companies submit **annual route planning** proposals.
2. Transport Department reviews + consults **District Councils**.
3. Adjustments can run **temporarily (up to 24 months)**.
4. Permanent changes require **legislative procedures**.

### Service frequency criteria (TD document)
- **90%** load factor during busiest half-hour (peak)
- **75%** load factor during busiest hour (peak)
- **60%** load factor during busiest hour (off‑peak)

### The puzzle
- For Route 56, reported **load factor = 32%**, far below criteria.
- Yet **frequency was increased** and the **route changed**.

### Four policy questions to ask
1. **How is “passenger load factor” defined?**
2. **When is the “busiest hour”?**
3. **Is 32% an average across stops or a typical stop?**
4. **What evidence justifies more frequency given low utilization?**

---

## 4) Simulation design (what we model)
### Goal
Estimate **seat utilization** using simulation and test if increased frequency is justified.

### Data sources
- **Field observation:** passenger flows by stop.
- **ETA data (data.gov.hk API):** travel times between stops.

### Three random components
1. **Travel time** between stops → Normal distribution (mean & SD from ETA samples).
2. **Passenger arrivals** at stops → Poisson distribution (rate estimated from observations).
3. **Passenger alighting** → Binomial distribution (probability estimated from observations).

### Why simulation?
- Real systems have **uncertainty** (traffic, arrivals, alighting).
- Multiple runs (e.g., **100–1,000** simulations) reveal distributions, not just single outcomes.

---

## 5) Key results (from the Bus 56 case)
- **After adjustment:** median seat utilization ~**12–34%** (forward); **5–34%** (return).
- **Before adjustment:** higher medians (e.g., **18–56%** forward; **8–58%** return).
- **Conclusion:** frequency increase **reduced utilization**, raising cost‑effectiveness concerns.

---

## 6) SimPy structure (4 steps)
1. **Create environment:** `env = simpy.Environment()`
2. **Define generator function:** `def busTrip(env, ...): yield env.timeout(...)`
3. **Register process:** `env.process(busTrip(env))`
4. **Run simulation:** `env.run()`

Important idea: **`yield env.timeout()`** advances time during travel (no “action” event).

---

## 7) Demo notebook walkthrough (Week 4)
- Found on Moodle → Week 4 → zip → `GCAP3226_week4_demo.ipynb`.
- Two parts:
  1. **Random number generation** (Normal distribution + visualization)
  2. **SimPy 4‑step structure** + multiple runs with random travel times
- **Reproducibility:** set random **seed** before generating values.

### Visualization guidance
- **Continuous variables:** histogram + box‑and‑whisker plot.
- **Box plot concepts:** median, Q1, Q3, IQR, outliers (1.5×IQR rule).

---

## 8) In‑class Exercise 2 (brief)
- **3 tasks:**
  1. Poisson random numbers (λ = 5, seed = 48, n = 20).
  2. Add **boarding time** to a bus simulation.
  3. Visualize arrival times (histogram + box plot).
- Use **GitHub Copilot** for code assistance but **review logic** carefully.

---

## 9) Policy inquiries to Transport Department (from the case)
1. What **operational/passenger flow data** were collected and analyzed?
2. What **quantitative criteria** were used to evaluate service quality?
3. Can the **datasets be released** for public/academic review?

---

## Actionable takeaways
- Always test headline claims by **checking the data source and population coverage**.
- Match visualization to **variable type** (categorical vs. continuous).
- Use simulation to explore **policy outcomes under uncertainty**.
- Frame findings as **clear, data‑driven questions** to government agencies.
