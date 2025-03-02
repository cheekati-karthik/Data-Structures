def quick_sort_inplace(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort_inplace(arr, low, pivot_index - 1)
        quick_sort_inplace(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  
    i = low - 1  

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  
    return i + 1  

arr = [5, 3, 8, 6, 2, 7, 4, 1]
quick_sort_inplace(arr, 0, len(arr) - 1)
print(arr)  
