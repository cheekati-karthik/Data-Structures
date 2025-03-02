n=5
def test(n):
    if n==0:
        return
    else:
        print("recursion ",n)
        n-=1
        test(n)
test(n)