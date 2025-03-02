arr=[5,2,1,8,4,7,6]
for i in range(1,len(arr)-1):
    k=i-1
    for j in range(i,len(arr)):
        if arr[j]<arr[k]:
            k=j
    arr[k],arr[i-1]=arr[i-1],arr[k]
print(arr)