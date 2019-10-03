s=input()
a=[int(s) for s in s.split()]
dif = 1
for i in range(len(a)-1):
    if a[i] != a[i+1]:
        dif += 1
print(dif)