#brute force
n=16
for i in range(2,n):
    if n%i==0:
        print(False)
        break
else:
    print(True)

#Optimal Approach
import math
n=16
for i in range(2,int(math.sqrt(n))+1):
    if n%i==0:
        print(False)
        break
else:
    print(True)