def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high

    while i < j:
        while i <= high - 1 and arr[i] <= pivot:
            i += 1
        while j >= low + 1 and arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]
    return j

def qs(arr, low, high):
    if low < high:
        p_index = partition(arr, low, high)
        qs(arr, low, p_index - 1)
        qs(arr, p_index + 1, high)

def quick_sort(arr):
    qs(arr, 0, len(arr) - 1)
    return arr

# Example usage
arr = [4, 6, 2, 5, 7, 9, 1, 3]
print("Before Using Quick Sort:", arr)
arr = quick_sort(arr)
print("After Using Quick Sort:", arr)
