# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    for i in range(len(merged_arr)):

        if len(arrA) == 0:
            merged_arr[i] = arrB[0]
            arrB.pop(0)

        elif len(arrB) == 0:
            merged_arr[i] = arrA[0]
            arrA.pop(0)

        elif arrA[0] <= arrB[0]:
            merged_arr[i] = arrA[0]
            arrA.pop(0)

        else:
            merged_arr[i] = arrB[0]
            arrB.pop(0)

    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # 1. While your data set contains more than one item, split it in half
    # 2. Once you have gotten down to a single element, you have also *sorted* that element 
    # (a single element cannot be "out of order")
    if len(arr) > 1:
        middle = len(arr) // 2

        left_arr = merge_sort(arr[0:middle])

        right_arr = merge_sort(arr[middle:])
    # 3. Start merging your single lists of one element together into larger, sorted sets
        arr = merge(left_arr, right_arr)
    # 4. Repeat step 3 until the entire data set has been reassembled
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
