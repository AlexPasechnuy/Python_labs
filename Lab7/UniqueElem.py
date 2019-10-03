a = [int(s) for s in input().split()]
counter = 0
for i in range(len(a)):
    rep = 0
    for j in range(len(a)):
        if a[i] == a[j]:
            rep += 1
    if rep == 1:
        print(a[i])