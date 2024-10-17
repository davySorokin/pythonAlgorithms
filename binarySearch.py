# Assuming the array is sorted.
def binarySearch(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid # Return the index of the target element.
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return - 1 #Return -1 if target is Not Found.

# Example Usage
arr = [2,3,4,5,6,7]
target = 5
result = binarySearch(arr, target)
if result != -1:
    print(f"Element {target} found at Index {result}")
else:
    print("Element not found!")