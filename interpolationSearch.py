# Assuming the array is sorted.
def interpolationSearch(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high and arr[low] <= target <= arr[high]:
        pos = low + ((high - low) * (target - arr[low])) // (arr[high] - arr[low])
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1

# Example usage:
arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
target = 80
result = interpolationSearch(arr, target)
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print("Element not Found!")