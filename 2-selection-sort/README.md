# Selection Sort
*Selection sort* is a basic sorting algorithm, being a stepping stone to *quicksort*.

## Arrays
**Great for jumping around and reading random elements; inefficient for reading one at a time.**
Cheaper reading, more expensive inserting.
- predetermined size
- items need to be together in memory
- if another item is added beyond the original size, all items in array most likely need to moved to another address

## Linked Lists
**Great for reading items one a a time; terrible for reading items all over the place.**
Cheaper inserting, more expensive reading.
- items can be anywhere in memory
- each item references where the next item in list is

| - | Arrays | Lists |
| ----------- | ----------- | ----------- |
| Reading | O(1) | O(n) |
| Insertion | O(n) | O(1) |
| Deletion | O(n) | O(1) |

### Exercises
#### 2.1
List (linked)

---
