# Breadth-First Search
*Allows you to find the shortest distance between two targets.*
examples include:
- a checkers AI to calculate the fewest moves to victory
- a spellchecker to calculate fewest misspellings to real word
- for finding a doctor closest to you in your network

## Introduction
**Shortest-path Problem**: *trying to find the shortest path to something*

The BFS algorithm can solve this problem:
1. Model the problem as graph.
2. Solve problem using breadth-first search.

## Graphs
*A graph models a set of connections with **nodes** and **connections**.*

## Breadth First Search
*Keep searching until case is met.* First degree targets are prioritized.
provides detail on:
- is there path from Node A => Node B
- what is shortest path from Noda A => Nody B

**Queue**, is a data structure that makes sure the order of the list is dependent on the order nodes were added:
- *enqueue*: add item to end of queue (aka push)
- *dequeue*: remove item from start of queue (aka pop)

This is known as a **FIFO** structure. A stack on the otherhand is **LIFO**.

## Implementing Graph
A *hash table* is perfect for expressing relationships in graphs; you can map nodes to their neighbours.

- *directed graph*: relationship is only one way
- *undirected graph*: both nodes are each other's neighbours

## Questions
---
#### 6.1
2

---
#### 6.2
2

---
#### 6.3
A: Invalid (breakfast)
B: Valid
C: Invalid (shower)

------
#### 6.4
1. Wake Up
2. Pack Lunch
3. Brush Teeth
4. Eat Breakfast
5. Exercise
6. Shower
7. Get Dressed
------
#### 6.5
A & C