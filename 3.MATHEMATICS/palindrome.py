n=56765
k=n
p=0
while n>0:
    p=p*10+n%10
    n=n//10
print(p)
if k==p:print(True) 
else: print(False)
