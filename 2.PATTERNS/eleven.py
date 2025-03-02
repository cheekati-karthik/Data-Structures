n=5
for i in range(1,2*n+1):
    if i<=n:
        for j in range(i):
            print("*",end="")
        for j in range(2*(n-i)):
            print(" ",end="")
        for j in range(i):
            print("*",end="")
    else:
        for j in range(2*n-i):
            print("*",end="")
        for j in range((i-n)*2):
            print(" ",end="")
        for j in range(2*n-i):
            print("*",end="")
        
    print()