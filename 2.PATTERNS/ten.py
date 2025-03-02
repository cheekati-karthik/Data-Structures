n=5
for i in range(1,2*n+1):
    if i<=n:
        for j in range(n-i+1,0,-1):
            print("*",end="")
        
        for j in range(2*(i-1)):
            print(" ",end="")

        for j in range(n-i+1,0,-1):
            print("*",end="")    
    else:
        for j in range(i-n):
            print("*",end="")
        for j in range(2*(2*n-i)):
            print(" ",end="")

        for j in range(i-n):
            print("*",end="")
        
    print()
