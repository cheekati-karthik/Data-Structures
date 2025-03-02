a=153
k=0
while a>0:
    k+=(a%10)**3
    a=a//10
if a==k:
    print(True)
else:
    print(False)
