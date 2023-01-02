# Dynamic Programming
*A technique used to solve hard problem by breaking it into sup-problems.*

- useful when trying to optimize something, given a constraint
- useful when problem can be broken into discrete subproblems (that don't depend on each other)

## Tips
- every dynamic-programming solution involves a grid
- values in cell are what you are trying to optimize
- each cell represents subproblem (figure out how to divide problem into subproblems)

You can ask the following questions when constructing the grid:
- what are the values of cells
- how do you divide problem into sub-problems
- what are axes of the grid

## Examples
### The Knapsack Problem
Describe the problem in an intial grid:
- one row for every available option
- one column for every variable size

Fill every cell with the total 'value' possible with the constraints.
The next row you can use previous row constraint and the new row constraint.
**Note that you can combine items for higher total values.**

### Items That Depend On Each Other
*Dynamic programming only works when each subproblem is discrete—when it doesn’t depend on other subproblems.*

## Exercises
Q9.1:
No

---
Q9.2:
2x Water

---