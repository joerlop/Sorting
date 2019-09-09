# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
             



        # TO-DO: swap




    return arr


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

    return arr

arr = [2, 4, 10, 1, 15, 2, 30, 3, 55, 5, 89, 2000]

print(bubble_sort(arr))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr