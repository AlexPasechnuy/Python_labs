s=input()
a=[int(s) for s in s.split()]
counter = 0
for i in range(1, len(a) - 1):
    if(a[i] > a[i-1] and a[i] > a[i+1]):
        counter += 1
print(counter)