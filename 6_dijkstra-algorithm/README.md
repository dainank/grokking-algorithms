# Dijkstra's Algorithm
*This algorithm can be used for when the fastest path needs to be find with known time-frames on every segment/edge.*

1. Find *cheapest* node (least amount of time) from starting point.
2. Check if there is cheaper path to neighbours of this node:
    - go to all edges from node
    - calculate costs from start to those locations compared to new costs through node
3. Repeat step 1-2 for every node in graph.
4. Calculate final path.

It is worthwhile to note down a table when calculating the above (headers):
- Node
- Cost
- Parent

## Terminology
- *weights*: **number associated with edges on graph**
    - graphs can be without *weights* (BFS is better for this)

Dijkstra's algorithm only works on graphs with no cycles (directed graphs).

**See implementation in Python file for proper explanation.**

## Exercises
7.1:

A. **8**
B. **4(Θ) - 2**
C. **4**