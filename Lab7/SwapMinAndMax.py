s=input()
a=[int(s) for s in s.split()]
minInd = 0
maxInd = 0
for i in range(len(a)):
    if a[i] > a[maxInd]:
        maxInd = i
    if a[i] < a[minInd]:
        minInd = i
temp = a[minInd]
a[minInd] = a[maxInd]
a[maxInd] = temp
print(a)