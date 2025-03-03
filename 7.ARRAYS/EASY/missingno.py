a=[1,2,3,5,6,7]
N=len(a)+1
summation = (N * (N + 1)) // 2
s2 = sum(a)
missingNum = summation - s2
print(missingNum)

N=len(a)
xor1 = 0
xor2 = 0
for i in range(N - 1):
    xor2 = xor2 ^ a[i]  # XOR of array elements
    xor1 = xor1 ^ (i + 1)  # XOR up to [1...N-1]
    xor1 = xor1 ^ N  # XOR up to [1...N]
print(xor1 ^ xor2)