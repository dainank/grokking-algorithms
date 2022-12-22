# Chapter 1 - Introduction to Algorithms
*__An algorithm__ is a set of instructions for accomplishing a task.*

- foundation of book
- search algorithm (binary search)
- running time of algorithm (Big O notation)
- designing algorithms (recursion)

## Binary Search
*__Binary search__ is an algorithm whereby its input is a sorted list of elements.*

**Binary search** is required to solve a common search problem whereby a large list of data needs to be searched but it would not be efficient to search from the start of the data list (which is known as **simple search**).

Any list of **n** will take **log(2)n** steps to run in worst case (with **binary search**), while it would take **n** steps to run with **simple search**.
> log(10)100 = 2 (*“How many 10s do we multiply together to get 100?”*) - essentially *the flip of exponentials*