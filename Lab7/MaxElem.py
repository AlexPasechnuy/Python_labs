s=input()
a=[int(s) for s in s.split()]
maxInd = 0
for i in range(1, len(a) - 1):
    if a[i] > a[maxInd]:
        maxInd = i
print(a[maxInd], maxInd)