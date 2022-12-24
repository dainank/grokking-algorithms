def binary_search(sorted_array, input_item):
    # return item position if in array (otherwise None)
    low_position_in_array = 0
    high_position_in_array = len(sorted_array) - 1

    while low_position_in_array <= high_position_in_array:
        mid_position_in_array = (low_position_in_array + high_position_in_array) # rounded down automatically (Python)
        guessed_item = sorted_array[mid_position_in_array]
        
        if guessed_item == input_item:
            return mid_position_in_array

        if guessed_item > input_item:
            high_position_in_array = mid_position_in_array - 1
        else:
            low_position_in_array = mid_position_in_array + 1
    return None # https://stackoverflow.com/questions/21095654/what-is-a-nonetype-object

def main():
    test_list = [1, 3, 5, 7, 9]
    print(binary_search(test_list, 3)) # exists
    print(binary_search(test_list, 4)) # does not exist

if __name__ == "__main__":
    main()

