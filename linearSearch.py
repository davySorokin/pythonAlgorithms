def linearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i #Return the index of the target element
    return -1

# Example Usage:
arr = [5,3,8,2,7]
target = 8
result = linearSearch(arr, target)
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print("element not found!")