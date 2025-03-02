#brute force
a=5
b=10
k=0
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        k=i
print(k)

#better
a=5
b=10
k=0
for i in range(min(a,b),0,-1):
    k=max(k,i)
print(k)

#optimal
a=5
b=10
while a>0 and b>0:
    if a>b:
        a=a-b
    else:
        b=b-a
if a>b:
    print(a)
else:
    print(b)