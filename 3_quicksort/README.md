# Quicksort
Quicksort uses divide-and-conquer strategy (a recursive technique):
1. Determine *base* case (the easiest case)
2. Divide/decrease problem until it becomes the base case

It is musch faster than selection sort.

## Quicksort In Detail
1. Select an element, known as the *pivot*.
2. Find elements smaller than *pivot*. [**partioning**]
3. Find elements larger than *pivot*. [**partioning**]
4. Sort the two partioned arrays [**recursion**]
5. Combine as follows: [left_arr] + [pivot] + [right_arr]

## Inductive Proofs
> A method to prove that an algorithm works.
- **base case**: *first step*
- **inductive case**: *step that allows next step*

## Examples
### Examples 1
We have array of numbers: `[2, 4, 6]`

**Non-recursive Function:**
```py
def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total

print sum([1, 2, 3, 4])
```

- Base Case: Array with 0 items.

**Recursive Approach:**
```py
def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])
```

### Questions

---
#### 4.4
Base case is 1 data point.
Recursion is division of two of all data points.

---
#### 4.5
O(n)

---
#### 4.6
O(n)

---
#### 4.7
O(1)

---
#### 4.8
O(n**2)

---