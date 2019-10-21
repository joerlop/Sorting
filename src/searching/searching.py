# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  for i in range(len(arr)):
    if arr[i] == target:
      return i
  # TO-DO: add missing code

  return -1   # not found

# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
  
  for i in arr:
    middle = len(arr) // 2

    if target == arr[middle]:
      return middle

  return -1 # not found



# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
  if target == arr[middle]:
    return middle
  elif target > arr[middle]:
    return binary_search_recursive(arr, target, middle + 1, len(arr) - 1)
  else:
    return binary_search_recursive(arr, target, 0, middle)

  return -1 # not found

arr = [1, 10, 30, 40, 50, 60, 70, 80, 90, 99]

print(binary_search_recursive(arr, 40, 0, len(arr) - 1))
