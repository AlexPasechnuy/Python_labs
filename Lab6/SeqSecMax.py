i = int(input())
max = i
prevMax = 0
while i != 0:
    i = int(input())
    if i > prevMax and i < max:
        prevMax = i
    elif i > max:
        prevMax = max
        max = i
print(prevMax)