n=5
for i in range(1,n+1):
    for j in range(i):
        print(j+1,end="")
    for j in range(2*n-2*i,0,-1):
        print(" ",end="")
    for j in range(i,0,-1):
        print(j,end="")
    print()