# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    for i in range(len(merged_arr)):

        if len(arrA) == 0:
            for item in arrB:
                merged_arr[i] = item
            break
        elif len(arrB) == 0:
            for item in arrA:
                merged_arr[i] = item
            break

        if arrA[0] <= arrB[0]:
            merged_arr[i] = arrA[0]
            arrA.pop(0)
        else:
            merged_arr[i] = arrB[0]
            arrB.pop(0)

    return merged_arr

print(f"merge: {merge([1, 2, 100], [0, 5, 7, 99])}")

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

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
