test_array = [10, 5, 2, 3, 3]

def quicksort(array):
    if len(array) < 2:
        return array # base case
    
    pivot = array[0]
    less_array = [i for i in array[1:] if i <= pivot]
    larger_array = [i for i in array[1:] if i > pivot]

    return quicksort(less_array) + [pivot] + quicksort(larger_array)

print(quicksort(test_array))
