# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  for i in arr:
    if arr[i] == target:
      return i
  # TO-DO: add missing code

  return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1

  # TO-DO: add missing code
  middle = (low + high) // 2

  if target == arr[middle]:
    return middle
  elif target > arr[middle]:
    return binary_search(arr[middle:])
  else:
    return binary_search(arr[0 : middle - 1])

  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
