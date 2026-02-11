# Week 4 Learning Guide: Simulation and Random Variables
## GCAP 3226: Empowering Citizens Through Data

---

## 📋 Overview

This week (Week 3-4 in the schedule) focuses on **discrete event simulation** using Python's SimPy library and **random variable generation** with NumPy. You'll learn these skills to eventually model real-world policy scenarios, such as evaluating bus route efficiency.

**Week Goals:**
- Understand random number generation from statistical distributions
- Learn the 4-step structure for creating simulations with SimPy
- Apply these concepts to analyze bus operations
- Complete In-class Exercise 2 (part of 10% assessment)

---

## 🧠 Lecture Highlights (Feb 4)

For a full summary, see `lectureNotes.md` in the same folder.

**Key points from the lecture:**
- **Data source scrutiny:** headline claims must be traced to the underlying dataset (job market example from the Joint Institution Job Information System).
- **Week 3 recap:** perceived government responsiveness + policy fairness explained ~61% of support; forward/backward regression gave the same predictors.
- **Visualization guidance:** for **categorical** variables, use **bar charts** instead of scatterplots.
- **Bus 56 case study:** frequency changes despite a 32% load factor; clarified questions about definitions, peak hour timing, and averaging.
- **Simulation design:** Normal (travel time), Poisson (boarding), Binomial (alighting) + 4‑step SimPy structure.
- **Evidence-based inquiries:** ask TD about data used, evaluation criteria, and public data release.

---

## 🎯 What You're Learning

### 1. **Random Variable Generation with NumPy**
   - Generate random numbers from probability distributions (Normal, Poisson)
   - Use random seeds for reproducible results
   - Visualize distributions with histograms and box plots
   - Calculate descriptive statistics (mean, std, min, max, quartiles)

### 2. **Discrete Event Simulation with SimPy**
   - Understand the 4-step SimPy structure
   - Model time-based processes (like bus trips)
   - Use generator functions with `yield`
   - Track simulation time with `env.now`
   - Process events in chronological order

### 3. **Real-World Application: Bus Route 56 Analysis**
   - Model actual HK bus operations with multiple stops
   - Incorporate **three types of randomness:**
     - Travel time (Normal distribution)
     - Passenger boarding (Poisson distribution)
     - Passenger alighting (Binomial distribution)
   - Run 1,000+ simulations for statistical reliability
   - Calculate seat utilization rates to evaluate policy
   - Question government decisions with evidence

---

## 📚 Step-by-Step Learning Path

### **Step 1: Review the Demo Notebook** 
📂 File: `GCAP3226_week4_demo.ipynb`

**What to do:**
1. Open the notebook in VS Code
2. Read through each cell carefully
3. Run each code cell one by one (Shift+Enter)
4. Observe the outputs and visualizations

**Key Concepts to Understand:**

#### Part A: Random Variable Generation
```python
import numpy as np
np.random.seed(43)  # For reproducible results
random_values = np.random.normal(loc=3.0, scale=0.3, size=100)
```

**Learn:**
- `np.random.normal()` generates values from a normal distribution
- `loc` = mean (average value)
- `scale` = standard deviation (spread of values)
- `size` = how many random numbers to generate
- Setting a seed makes results reproducible

**Visualizations:**
- **Histogram**: Shows frequency distribution of values
- **Box and Whisker Plot**: Shows median, quartiles, and outliers

#### Part B: The 4-Step SimPy Structure

This is **CRITICAL** to understand:

```python
# Step 1: Create a SimPy Environment
env = simpy.Environment()

# Step 2: Define a Generator Function
def bus_trip(env):
    departure_time = env.now
    yield env.timeout(3)  # Pause for 3 time units
    arrival_time = env.now

# Step 3: Add the Generator Function to Environment
env.process(bus_trip(env))

# Step 4: Run the Simulation
env.run()
```

**Key Points:**
- `simpy.Environment()`: Creates the simulation world
- Generator function: Defines what happens during the simulation
- `yield env.timeout(x)`: Makes time pass in the simulation
- `env.now`: Current simulation time
- `env.process()`: Registers a process to run
- `env.run()`: Executes all events

#### Part C: Multiple Simulation Runs

The demo shows running 100 simulations with random travel times. This teaches you:
- How to run repeated simulations
- How to store results in a list
- How randomness affects outcomes
- Statistical analysis of simulation results

---

### **Step 2: Complete Exercise 2**
📂 File: `Exercise_2_student.ipynb`

This is your **in-class assessment** (counts toward 10% of final grade).

#### **Task 1: Generate Poisson Random Numbers**

**What you need to do:**
```python
# Set seed to 48 for reproducible results
# Generate 20 values from Poisson distribution with lambda = 5
```

**Background:**
- **Poisson distribution** models count data (e.g., number of passengers)
- `λ (lambda) = 5` means average of 5 passengers
- You'll get integers like 3, 6, 4, 7, 5, etc.
- **Real-world use:** In the Bus 56 case study, Poisson distribution models waiting passengers at each stop

**Hints:**
- Use `np.random.seed(48)` first
- Use `np.random.poisson(lam=5, size=20)`
- Store results in a variable

#### **Task 2: Modified Bus Simulation**

**What you need to do:**
1. Use the random numbers from Task 1 as passengers boarding at Stop A
2. Each passenger takes 3 seconds to board
3. Run the simulation 20 times
4. Record arrival time at Stop B for each run

**Modified generator function should:**
- Take the number of boarding passengers as input
- Calculate boarding time: `passengers × 3 seconds`
- Add boarding time to the bus trip
- Use `yield env.timeout(boarding_time)` for boarding
- Use `yield env.timeout(travel_time)` for travel

**Question to answer:** How is the modified function different from the original?

**Key differences:**
1. **Input parameter**: Original has none; modified takes `num_passengers`
2. **Additional timeout**: Original only travels; modified adds boarding time
3. **Variable delay**: Original is fixed 3 min; modified varies by passengers
4. **Multiple yields**: Original has 1 yield; modified has 2 (boarding + travel)

#### **Task 3: Visualize Results**

**What you need to do:**
- Create side-by-side plots (histogram and box plot)
- Show distribution of bus arrival times at Stop B
- Include appropriate labels and titles

**Hints:**
- Use `plt.subplots(1, 2, figsize=(12, 5))`
- Extract arrival times from your simulation results
- Follow the visualization pattern from the demo notebook

---

### **Step 3: Understand the Case Study Context**
📂 Files: 
- `Case Study II: Evaluating the Efficiency of Bus Route Adjustments: City bus No. 56.md`
- Original slides (converted to markdown)

**Real-World Policy Investigation:**

This case study demonstrates how students used simulation to question a government decision about City Bus Route 56 in Hong Kong's North District.

#### **The Policy Problem:**

**Government's Criteria for Increasing Bus Frequency:**
- 90% load factor during busiest half-hour (peak)
- 75% load factor during busiest hour (peak)  
- 60% load factor during busiest hour (off-peak)

**The Paradox:**
Bus Route 56 had only **32% passenger load factor** during the busiest hour, yet:
- The government increased frequency
- The route was adjusted

**Critical Questions Raised:**
- How is "passenger load factor" defined?
- When is the "busiest hour"?
- Is 32% an average across stops and shifts?
- How is increased frequency justified with only 32% load?

#### **The Simulation Approach:**

**Objectives:**
1. Develop a simulation of Bus Route 56 morning operations
2. Use real field data and ETA from https://data.gov.hk/en/
3. Estimate actual seat utilization rate via simulation
4. Provide evidence for policy enquiries to Transport Department

**Data Collection:**
- Collected ETA data for 30 trips of Bus No. 56
- Calculated travel time statistics between each pair of stops
- Estimated passenger flows at each stop

**Three Random Components Modeled:**

1. **Travel Time** (Normal Distribution):
   - Mean and SD calculated from 30 sample trips
   - Each stop-to-stop segment has its own distribution
   - Represents traffic variability

2. **Waiting Passengers** (Poisson Distribution):
   - Random number boarding at each stop
   - Poisson models count data well
   - Reflects unpredictable passenger arrivals

3. **Alighting Passengers** (Binomial Distribution):
   - Random number getting off at each stop
   - Success/failure for each passenger: get off or stay on
   - Accounts for different destinations

**Simulation Scale:**
- Ran **1,000 simulations** for statistical reliability
- Used SimPy discrete-event simulation framework
- Tracked seat utilization at every stop

#### **The Shocking Results:**

**After Adjustment (Current Route):**
- Forward direction: 12% - 34% seat utilization
- Return direction: 5% - 34% seat utilization

**Before Adjustment (Estimated):**
- Forward direction: 18% - 56% seat utilization  
- Return direction: 8% - 58% seat utilization

**Conclusion:** 
> **The adjustment appears to have REDUCED overall seat utilization!**

#### **Evidence-Based Advocacy:**

Students prepared formal enquiries to the Transport Department:

1. **Operational Data Request:**
   - What stop-level boarding/alighting data was collected?
   - What are peak vs. off-peak passenger counts?

2. **Methodology Transparency:**
   - What quantitative models were used to evaluate the changes?
   - What criteria assessed service quality?

3. **Data Accessibility:**
   - Are these datasets publicly available?
   - Can data be released under the Code on Access to Information?

**Connection to course objectives:**
- **Data-driven policy**: Evaluating HK government transportation decisions
- **Government transparency**: Requesting data and methodology
- **Advocacy**: Using simulation to challenge questionable policy
- **Experiential learning**: Real policy problem with real impact
- **SDG alignment**: Sustainable cities and transportation (SDG 11)

**Critical Thinking Questions:**
- Why would the government increase frequency despite low utilization?
- What data might they have that students didn't?
- How could operating costs justify the decision?
- What would you ask the Transport Department?
- How would you present these findings to the Legislative Council?

---

## 🔧 Technical Setup

### Required Libraries
```python
import numpy as np          # Random number generation
import simpy               # Discrete event simulation
import matplotlib.pyplot as plt  # Visualization
```

### Installation (if needed)
If you get import errors, install with:
```bash
pip install numpy simpy matplotlib
```

Or use AI assistance:
- Ask GitHub Copilot to help install packages
- Use "vibe coding" approach – describe what you want to do

---

## 💡 AI-Assisted Learning Tips

Remember: This is a **"vibe coding"** course. You don't need to be a programming expert!

### How to use GitHub Copilot:
1. **Describe what you want**: Write a comment explaining your goal
   ```python
   # Generate 20 random numbers from Poisson distribution with lambda=5 and seed=48
   ```

2. **Let Copilot suggest**: It will offer code completions

3. **Review and test**: Run the code and check if it works

4. **Ask questions**: Use Copilot Chat to explain concepts
   - "What does yield do in Python?"
   - "How does Poisson distribution work?"
   - "Why do we set a random seed?"

### Debugging strategy:
1. Read error messages carefully
2. Check variable names and spelling
3. Ensure you ran previous cells first
4. Ask Copilot: "Why am I getting this error?"

---

## 📊 Assessment Checklist

For **In-class Exercise 2** (10% of final grade):

### Task 1:
- [ ] Set random seed to 48
- [ ] Generate 20 Poisson random numbers with λ=5
- [ ] Store results in a variable
- [ ] Display/print the results

### Task 2:
- [ ] Create modified bus trip generator function
- [ ] Include passenger boarding time (passengers × 3 seconds)
- [ ] Run simulation 20 times using Task 1 random numbers
- [ ] Record arrival times for each run
- [ ] Answer: How is modified function different from original?

### Task 3:
- [ ] Create histogram of arrival times
- [ ] Create box and whisker plot of arrival times
- [ ] Display plots side by side
- [ ] Include labels and titles
- [ ] Show distribution clearly

---

## 🌟 Connecting to the Big Picture

### Why This Matters for Policy Analysis

**Course Goal**: Advocate for evidence-based policy using data

**This week's skills enable you to:**
1. **Model uncertainty**: Real-world data isn't fixed (passengers vary, times fluctuate)
2. **Test scenarios**: Simulate "what if" before implementing policy changes
3. **Quantify impact**: Use numbers to show efficiency gains/losses
4. **Visualize findings**: Communicate complex data to policymakers

**Example application to your group projects:**
- **Flu Shot project**: Simulate clinic wait times with varying patient arrivals (Poisson)
- **Road Safety project**: Model accident probability with random traffic conditions (Normal)
- **MPF project**: Simulate retirement outcomes under different investment scenarios
- **Bus routes (this case)**: Evaluate seat utilization with three types of randomness
- **Fire Service**: Model emergency response times with variable call volumes
- **Healthcare Screening**: Simulate patient flow through screening programs

### Beyond Simple Models: The Bus 56 Case Study Shows

**Multiple Random Components:**
The real Bus 56 simulation combined:
1. **Normal distribution** for travel times (continuous variable)
2. **Poisson distribution** for boarding passengers (count data)
3. **Binomial distribution** for alighting passengers (success/failure)

**Large-Scale Simulation:**
- Ran 1,000 simulations (not just 20-100)
- Multiple stops (entire route, not just A→B)
- Real data from government API (30 trips for parameter estimation)

**Policy Impact:**
- Results challenged government decision
- Led to formal enquiries to Transport Department  
- Demonstrated reduced seat utilization after route adjustment
- Example of evidence-based advocacy

### Skills for Legislative Council Submission

By Week 11-12, you'll present findings to stakeholders. This week teaches you:
- ✅ Statistical rigor: Your recommendations backed by simulation
- ✅ Visualization: Clear charts that non-experts can understand
- ✅ Reproducibility: Others can verify your analysis
- ✅ Quantification: Move from opinions to evidence

---

## 📝 Reflection Questions

After completing the notebooks and exercise, reflect on:

1. **Understanding randomness**: 
   - How does randomness affect simulation outcomes?
   - Why run multiple simulations instead of just one?
   - In Bus 56 study: Why run 1,000 times vs. 100 times?

2. **SimPy structure**:
   - What happens when you call `yield env.timeout()`?
   - How does SimPy track time automatically?
   - How can you model complex sequences of events?

3. **Policy implications**:
   - How could simulation improve government decision-making?
   - What data would you need from the Transport Department?
   - Why did Bus 56 adjustment reduce seat utilization?
   - Should cost considerations override efficiency metrics?

4. **Your project**:
   - Could simulation help your group project?
   - What random variables exist in your policy area?
   - What government data would you request?
   - How would you use simulation results in your advocacy?

5. **Statistical distributions**:
   - Why use Normal distribution for travel times?
   - Why use Poisson for passenger arrivals?
   - Why use Binomial for passenger exits?
   - What distributions fit your project data?

---

## 🆘 Getting Help

### During class:
- Ask Dr. Wu or Dr. Wang
- Work with your group members
- Use GitHub Copilot Chat

### Resources:
- [SimPy Documentation](https://simpy.readthedocs.io/)
- [NumPy Random Documentation](https://numpy.org/doc/stable/reference/random/index.html)
- Course Moodle for additional materials
- Office hours with instructors

### Common questions:
- **"I get an import error"**: Check if packages are installed
- **"My random numbers don't match others"**: Check your seed value
- **"Simulation doesn't run"**: Make sure you called `env.run()`
- **"Not sure what to visualize"**: Look at the demo notebook examples

---

## ✅ Next Steps

After completing Week 4:

1. **Week 5 (Feb 11)**: Data collection planning
   - Write to government departments
   - Plan fieldwork strategy
   - Receive HK$300 fieldwork allowance

2. **Week 6 (Feb 25)**: Field work
   - Collect primary data
   - No in-class session

3. **Your group project**:
   - Apply simulation skills to your topic
   - Start thinking about what data you need
   - Consider using AI tools for analysis

---

## 🎓 Learning Outcomes

By the end of this week, you should be able to:

✅ Generate random numbers from probability distributions  
✅ Explain what the numbers represent in context  
✅ Create visualizations (histogram, box plot) of distributions  
✅ Set up and run a SimPy discrete event simulation  
✅ Modify generator functions to model different scenarios  
✅ Run multiple simulations and analyze results  
✅ Connect simulation concepts to policy evaluation  
✅ Use AI tools (Copilot) to assist with coding tasks  

---

## 📌 Key Takeaways

1. **Math is accessible**: AI tools make complex modeling approachable for non-math majors

2. **Simulation is powerful**: Test policies before implementation – save money and improve outcomes

3. **Randomness matters**: Real world has uncertainty; models should too

4. **Data drives decisions**: Better data + better models = better policies

5. **You can make a difference**: These tools will help you advocate for evidence-based policy changes in Hong Kong

---

**Remember**: This is experiential learning. Don't just read – **run the code**, **experiment**, **make mistakes**, and **learn by doing**! 

Good luck with Exercise 2! 🚀
