i = int(input())
max = i
numMax = 1
while i != 0:
    i = int(input())
    if i == max:
       numMax += 1
    elif i > max:
        max = i
        numMax = 1
print(numMax)