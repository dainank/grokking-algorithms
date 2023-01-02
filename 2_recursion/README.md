# Recursion
- a coding technique used in many algorithms
- involves calling up the current method within the method itself
- useful if it allows the solution to be clearer

> “*Loops may achieve a performance gain for your program. Recursion may achieve a performance gain for your programmer. Choose which is more important in your situation!*” - Leigh Caldwell

## The Two Parts (avoiding infinite loops)
Each *recursive function* is made up of two parts:
- the _base_ case: **when the function does not call itself**
- the _recursive_ case: **when the function calls itself**

Below is a simple example:
```python
def countdown(i):
    print(i)
    if i <= 1:          # base case
        return
    else:
        countdown(i-1)  # recursive case
```

## The Stack
- *push*: add item to top
- *pop*: remove topmost item and read it
The computer uses a call stack, below is an example:
```python
def second_greet(name): # STACK 2 -> off stack
    print("how are you, " + name + "?")

def bye(): # STACK 2 -> off stack
    print("ok bye!")

def greet(name): # STACK 1 -> eventually off stack too
    print("Hello " + name)
    second_greet(name)
    print("getting ready to say bye...")
    bye()

greet("Ben")
```

It is important to note that when you call another function within a function, the current function is partially completed, thus is temporarily paused (all variables still stored).

There is **one cost to using stack** and recursion; it can **take up a lot of memory**. Alternate options include:
- rewrite code to use loop instead
- you can utilize *tail recursian* (only supported by some languages)

### Exercises
#### 3.1
- greet method was called first
- greet2 method was called from within greet function

---
#### 3.2
Eventually the stack will be so large that all memory of the computer is used and no more functions can be called up and added to the stack. The program will exit with a stack-overflow error.

---