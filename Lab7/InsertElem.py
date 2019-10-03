s=input()
a=[int(s) for s in s.split()]
k = int(input())
c = int(input())
a.append(a[len(a) - 1])
for i in range(k + 1, len(a) - 2, -1):
    a[i] = a[i-1]
a[k] = c
print(a)