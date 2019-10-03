n , k = [int(s) for s in input().split()]
a = ["I"]*n
for i in range (k):
    li, ri = [int(s) for s in input().split()]
    for i in range(li - 1, ri):
        a[i] = "."
print(a)


