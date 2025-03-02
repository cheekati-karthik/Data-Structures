#brute force
n= 56784
c=0
while n>0:
    c+=1
    n=n//10
print(c)

#optimal
import math
k=89084
print(int(math.log(k,10)+1))