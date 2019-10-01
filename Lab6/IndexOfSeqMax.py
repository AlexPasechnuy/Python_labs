i = int(input())
max = i
counter = 0
maxCounter = 0
while i != 0:
    i = int(input())
    counter += 1
    if i > max:
        max = i
        maxCounter = counter
print(maxCounter)