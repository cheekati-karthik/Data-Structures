#brute force
n=12
divisors = []
for i in range(1, n + 1):
    if n % i == 0:
        divisors.append(i)
print(divisors)

#optimal
import math
n=12
divisors=[]
for i in range(1,int(math.sqrt(n))+1):
    if n%i==0:
        divisors.append(i)
        if i != n // i:  
            divisors.append(n // i)
print(divisors)