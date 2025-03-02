#brute force
def reverseArray(arr):
    n=len(arr)
    ans = [0] * n
    for i in range(n - 1, -1, -1):
        ans[n - i - 1] = arr[i]
    return (ans)
print(reverseArray([1,2,3,4,5]))

# optimal approach
def reverseArray(arr):
    n=len(arr)
    p1 = 0
    p2 = n - 1
    while p1 < p2:
        arr[p1], arr[p2] = arr[p2], arr[p1]
        p1 += 1
        p2 -= 1
    return arr
print(reverseArray([1,2,3,4,5]))

#recursion
def reverseArray(arr, start, end):
    if start < end:
        arr[start], arr[end] = arr[end], arr[start]
        reverseArray(arr, start + 1, end - 1)
arr=[1,2,3,4,5]
reverseArray(arr,0,4)
print(arr)
