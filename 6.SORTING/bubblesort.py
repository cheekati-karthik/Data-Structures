def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # Track if a swap is made
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:  # Swap if the element is greater than the next
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # If no swaps occurred, array is sorted
            break
    return arr

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)