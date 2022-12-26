# Hash Tables
- useful basic data structure
- the internals:
    - implementation
    - collisions
    - hash function

*Hash functions are functions where you can input a string and get back a number.* => **maps strings to numbers**

Requirements:
- needs to be consistent (same results with same inputs)
- different strings should always map different numbers

Essentially, a hash function defines exactly where data is stored within an array, thus no search is required. It is also important to note that the hash functions knows how big the array is and therefore only returns valid indexes.

Alternative names include:
- hash maps
- maps
- dictionaries
- associative arrays

## Use Cases
- for lookups (**searching**)
    - example: phonebooks, DNS resolutions
    - when mapping one thing to another
    - looking up something
- checking for duplicates (**filtering**)
- caching (**memorizing data**)
    - web page loads faster
    - less work for servers hosting site

## Collisions
*Two inputs that map to the same output.*

A solution includes putting individual linked lists in every hash slot for duplicate mappings.

## Performance
Hash tables in the ideal case are O(1) *constant time*.
In worst case, they can be slowest and seaching and inserts/deletes. To avoid collisions, the following is required:
- low load factor
    - can be calculated: # of items in table / # of available slots
    - best practice is to resize (by double) whenever load factor > 0.7
- good hash function
    - *distributes values evenly in an array*

## Questions
---
#### 5.1
True

---
#### 5.2
False

---
#### 5.3
False

---
#### 5.4
True

---
#### 5.5
(C || D)

---
#### 5.6
(B || D)

---
#### 5.7
(B || C || D)

---