# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for i in range(cur_index + 1, len(arr)):
            if arr[i] < arr[cur_index]:
                temp = arr[i]
                arr[i] = arr[cur_index]
                arr[cur_index] = temp
        print(f"arr: {arr}")
        # TO-DO: swap

    return arr

arr = [1, 10, 5, 20, 2, 25, 5, 4, 3, 10]

print(selection_sort(arr))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    swaps = 1

    while swaps > 0:
        swaps = 0
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                temp = arr[i]
                arr[i] = arr[i - 1]
                arr[i - 1] = temp
                swaps += 1
        print(f"arr1: {arr}")
    return arr

arr1 = [1, 10, 5, 20, 2, 25, 5, 4, 3, 10]

print(bubble_sort(arr1))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr