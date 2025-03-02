n=5
for i in range(1,n+1):
    if i%2==0:
        k=1
    else:
        k=0
    for j in range(i):
        k=1-k
        print(k,end="")
    print()
