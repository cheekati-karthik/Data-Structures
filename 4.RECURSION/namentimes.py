i=0
n=5
def test(i,n):
    if i==n:
        return
    else:
        print("recursion ",i)
        i+=1
        test(i,n)
test(i,n)