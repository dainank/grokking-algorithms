# Greedy Algorithms
*At each step you pick the locally optimal solution.*

**NP-Complete**: *you calculate every possible solution and pick smallest/shortest one.*
Common indicators:
- runs-quickly with handful of items but slows down significantly with larger sizes.
- 'all combinations of X' point to NP-complete problem.
- you can't break the problem down into sub-problems
- problems involving sequences (travelling salesman)
- hard to solve problems with sets

Set terms:
- **union**: *combine both sets*
- **intersection**: *find items that are present in both sets*
- **difference**: *subtract items from one set off of another*

## Radio Station Example
### Accurate Solution
1. List every possible subset of stations (**power set**).
2. Pick the set with the smallest number of stations.

### Realistic Solution
Using greedy algorithms (an **approximation algorithm**):
1. Pick station that covers most states that havn't been covered yet (some duplicate states is fine).
2. Repeat until all states are covered.

## Exercises
Q8.1
Picking smallest boxes first, thus not greedy strategy.

---
Q8.2
Divide point value with time takes. Pick largest net values first, thus no greedy strategy.

---
Q8.3
Not Greedy

---
Q8.4
Not Greedy

---
Q8.5
Yes Greedy

---
Q8.6
Yes

---
Q8.7
Yes

---
Q8.8
Yes

