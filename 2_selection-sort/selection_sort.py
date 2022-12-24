def findSmallest(arr): # value in array
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest_index = findSmallest(arr)
        newArr.append(arr.pop(smallest_index)) # remove item at index and add to end of list
    return newArr

def main():
    print(selectionSort([5, 3, 6, 2, 10]))

if __name__ == "__main__":
    main()
