i = int(input())
prev = i
num = 0
while i != 0:
    i = int(input())
    if i > prev:
        num += 1
    prev = i
print(num)