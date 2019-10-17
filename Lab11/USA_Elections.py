a = dict()
num = int(input())
for i in range(num):
    surn, num = [i for i in input().split()]
    if surn in a:
        a[surn] += int(num)
    else:
        a[surn] = int(num)

print(a)