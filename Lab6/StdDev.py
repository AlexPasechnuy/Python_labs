from math import sqrt

partSum = 0
partSumSquares = 0
x_i = int(input())
n = 0
while x_i != 0:
    n += 1
    partSum += x_i
    partSumSquares += x_i ** 2
    x_i = int(input())
print(sqrt((partSumSquares - partSum ** 2 / n) / (n - 1)))
