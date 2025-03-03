def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
def rotate_right(arr, k):
    n = len(arr)
    k %= n 
    if k == 0:
        return
    reverse(arr, 0, n - k - 1)
    reverse(arr, n - k, n - 1)
    reverse(arr, 0, n - 1)
arr = [1, 2, 3, 4, 5, 6, 7]
k = 2
rotate_right(arr, k)

print("After Rotating the k elements to right:", arr)