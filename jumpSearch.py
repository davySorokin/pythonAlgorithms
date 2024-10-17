import math

# Assuming array is sorted.
def jumpSearch(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while arr[min(step, n)-1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1
    if arr[prev] == target:
        return prev
    return -1

# Example Usage
arr = [1,2,3,4,5,6,7,8,9,10]
target = 10
result = jumpSearch(arr, target)
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print("element not found!")