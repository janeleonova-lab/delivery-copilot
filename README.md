# 🚦 Delivery Copilot

**AI-powered delivery planning: predicts task timelines, recommends owners,
and simulates launch dates with Monte Carlo scenarios.**

🔗 Live demo: [your Streamlit URL here]

## The problem
Delivery planning runs on optimistic estimates, gut-feel assignments, and a
single launch date that's outdated the moment it's spoken. The cost isn't just
missed dates — it's eroded trust between product, engineering, and leadership.

## What it does
1. **Timeline prediction** — learns the estimate-vs-actual overrun ratio for
   each task type × complexity segment from historical data, and corrects new
   estimates accordingly (e.g. high-complexity mobile work historically runs ×1.8).
2. **Owner recommendation** — scores team members on skill fit (70%) and free
   capacity (30%). Flags when no qualified person has bandwidth — an early
   warning, not just a matcher. The PM always makes the final call.
3. **Launch simulation** — runs 5,000 Monte Carlo scenarios with asymmetric
   uncertainty (delays have longer tails than early finishes) and reports P50/P90
   dates plus the probability of hitting a target — shifting the conversation
   from "when will it ship?" to "how confident are we?"

## Key design decisions
- **Explainable over sophisticated.** With 40 sample tasks, a complex model would
  overfit — and worse, engineers wouldn't trust it. "Your segment historically
  runs ×1.8" is an argument a team can engage with.
- **Decision support, not automation.** Assignments affect people; the AI
  proposes, the human decides.
- **Conservative simulation.** Sequential execution and a fat-tailed delay
  distribution — better to under-promise on a v1 planning tool.

## Limitations & v2 roadmap
- Self-created dummy data → connect to **Jira/Linear** so the model retrains
  continuously as tasks complete.
- Sequential task model → model the **dependency graph** for parallel tracks
  and true critical-path analysis.
- Static skill tags → infer skills and velocity from **actual delivery history**.
- Add **scenario levers**: "what if we add one backend engineer?" or
  "what if we cut scope by 20%?" — simulate trade-offs before making them.

## Stack
Streamlit · pandas · NumPy · self-created dataset (no confidential data).
Built in ~60 minutes as part of the Careem PM assignment.
