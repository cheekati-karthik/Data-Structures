arr=[2,5,9,6,1,3]
n=len(arr)
ma = arr[0]
for i in range(0, n):
    if (ma < arr[i]):
        ma = arr[i]
print(ma)