# Case Study II_ Evaluating the Efficiency of Bus Route Adjustments_ City bus No. 56

---

## Slide 1

### Case Study II: Evaluating the Efficiency of Bus Route Adjustments: City bus No. 56

GCAP3226 2026/02/04

‹#›

---

## Slide 2

### Structure of Case Study II

Background
Simulation design
Random component in the simulation
Results Interpretation
Enquiries (with Transport Department)
In-class Exercise

‹#›

---

## Slide 3

### Background

‹#›

---

## Slide 4

### Bus route planning programme

‹#›

---

## Slide 5

### Criteria for Increasing Bus Frequency

“For individual bus routes, if the passenger load factor reaches 90% during the busiest half-hour and 75% during the busiest hour of peak periods, or 60% during the busiest hour of off-peak periods, the department and the franchised bus company will consider increasing the service frequency.”

‹#›

Bus route planning program 2024-2025 for North District

(2024)

---

## Slide 6

### Questions

The passenger load factor of City Bus No. 56, as reported in the proposal, is 32% during the busiest hour (before adjustment). However, it is unclear:
How this passenger load factor is defined
When the busiest hour occurs
Whether the 32% represents an average across different stops and shifts
How an increase in bus frequency is justified given a passenger load factor of 32%

‹#›

---

## Slide 7

‹#›

Yan Po Rd.

---

## Slide 8

‹#›

---

## Slide 9

### Objectives

To develop and analyze a simulation of Bus Route 56 operations during the morning using field data and estimated arrival times (ETA) from https://data.gov.hk/en/.
To assess the justification for route and frequency adjustments to Bus No.56 by estimating the seat utilization rate via simulation.
To provide evidence-based policy enquiries.

‹#›

---

## Slide 10

### Recall simulation design

Simulation is about mimicking (complex) systems, normally over time, using logic, math and computers.
Simulation is an experimental process – run and rerun a model many times under different scenarios to predict system behaviour and evaluate performance under each scenario.

‹#›

https://poe.com/Bus56

---

## Slide 11

### Random components

To calculate the seat utilization rate, we need to count the passengers on bus at each stop.
The travel time between each pair of stops is random.
At each stop, the number of waiting passengers is random.
At each stop, the number of passengers getting off is random.

‹#›

---

## Slide 12

### Travel time

The bus travel time between each pair of stops is modelled as a random variable drawn from a normal distribution, with the mean and standard deviation estimated from sample data.
Using the API, we collected ETA at each stop for 30 trips of Bus No. 56.
We then calculated the mean and standard deviation of travel times between each pair of stops. For each simulation run, we sampled travel times from the corresponding normal distributions to represent the bus travel times between stops.

‹#›

---

## Slide 13

### Number of waiting passengers

The number of waiting passengers at each stop is modelled as a random variable drawn from a Poisson distribution.

‹#›

---

## Slide 14

### Number of passengers getting off

The number of passengers getting off at each stop is modelled as a random variable drawn from a Binomial distribution.

‹#›

---

## Slide 15

### SimPy

SimPy is a discrete-event simulation framework.
Each event represents a specific action (e.g., bus arrival, passenger boarding, bus departure after dwell time).
Events are processed in chronological order according to their scheduled time, and only when they occur.

‹#›

---

## Slide 16

### A typical SimPy structure

‹#›

Record the current time whenever an event happens env.now

---

## Slide 17

### Result - existing forward (after adjustment)

In 1000 simulations:
Median of seat utilization:
12% - 34%

‹#›

---

## Slide 18

### Result - existing return (after adjustment)

In 1000 simulations:
Median of seat utilization:
5% - 34%

‹#›

---

## Slide 19

### Result – forward, before adjustment

‹#›

In 1000 simulations:
Median of seat utilization:
18% - 56%, based on estimated passenger flow at the removed bus stops.

Passenger flow data based on assumptions

---

## Slide 20

### Result – return, before adjustment

‹#›

In 1000 simulations:
Median of seat utilization:
8% - 58%

Passenger flow data based on assumptions

---

## Slide 21

### Result - Summary

The adjustment appears to have reduced the overall seat utilization rate.
But the decision to increase bus frequency should also be analysed from the perspective of operating costs.

‹#›

---

## Slide 22

### Enquiry to Transport Department

1.	Operational and Passenger Flow Data:
What types of operational and passenger flow data (e.g., stop-level boarding and alighting, peak/off-peak passenger counts) were collected and analyzed when assessing the rerouting and schedule changes for Routes 56?
2.	Service Quality Evaluation:
What quantitative models or criteria were used to evaluate whether the service modifications would maintain or improve passenger service quality?
3. 	Data Accessibility:
Are the relevant operational datasets, consultation summaries, or evaluation models available for public or academic review? If so, how can these be accessed? If not, would the Transport Department consider releasing anonymized or summarized data in accordance with the Code on Access to Information?

‹#›

---
