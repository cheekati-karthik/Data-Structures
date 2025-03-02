def insertion(arr):
    n=len(arr)
    for i in range(n):
        j=i
        while j>0 and arr[j-1]>arr[j]:
            arr[j],arr[j-1]=arr[j-1],arr[j]
            j-=1
arr=[5,7,9,8,1,3,4,6]
insertion(arr)
print(arr)

