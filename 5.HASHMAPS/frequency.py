def Frequency(arr):
    n=len(arr)
    mp = {}
    for i in range(n):
        if arr[i] in mp:
            mp[arr[i]] += 1
        else:
            mp[arr[i]] = 1
    for x in mp:
        print(x, mp[x])

arr = [10, 5, 10, 15, 10, 5]
Frequency(arr)