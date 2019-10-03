s=input()
a=[int(s) for s in s.split()]
for i in range(0, len(a)//2*2-1, 2):
    temp = a[i]
    a[i] = a[i+1]
    a[i+1] = temp
print(a)