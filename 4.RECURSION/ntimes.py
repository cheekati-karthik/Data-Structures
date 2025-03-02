n=0
def test(n):
    if n==3:
        return
    else:
        print("recursion ",n)
        n+=1
        test(n)
test(n)
