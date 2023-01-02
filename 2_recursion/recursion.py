# NOTE; THIS IS PSEUDOCODE, PROBABLY CAN'T BE RAN

# -- 1 -- (NO RECURSION)
def look_for_key(main_box):
    empty = 0
    pile = main_box.make_a_pile_to_look_through()
    while pile is not empty:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print("Key Found!")

# -- 2 -- (RECURSION)
def look_for_key_recursion(box):
    for item in box:
        if item.is_a_box():
            look_for_key_recursion(item)  # recursion occurs here
        elif item.is_a_key():
            print("Key Found!")

# -- 3 -- (FACTORIAL RECURSION)
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)
