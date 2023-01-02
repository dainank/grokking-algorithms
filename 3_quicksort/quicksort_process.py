# Questions From Chapter 4
test_list = [2, 5, 3, 7, 9, 8]

# Q4.1

def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])

# Q4.2

def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])

# Q4.3 (?)

def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max

print(max(test_list))