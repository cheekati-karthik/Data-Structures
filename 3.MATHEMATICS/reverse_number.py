n=56784
p=0
while n>0:
    p=p*10+n%10
    n=n//10
print(p)
