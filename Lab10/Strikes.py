n, k = [int(i) for i in input().split()]

days = set()

for i in range (k):
    a, b = [int(i) for i in input().split()]
    while a <= n:
        if a%7!=0 and (a+1)%7!=0:
           days.add(a)
        a+=b

print(len(days))