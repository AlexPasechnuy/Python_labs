n = int(input())
ethSum = 0
for i in range(1, n + 1):
    ethSum += i
realSum = 0
for i in range(1, n):
    a = int(input())
    realSum += a
print(ethSum - realSum)