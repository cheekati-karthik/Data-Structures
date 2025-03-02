def nsum(n):
    if n==1:
        return 1
    else:
        return n + nsum(n-1) 

n=5
print(nsum(n))

#optimal
print(n*(n+1)//2)