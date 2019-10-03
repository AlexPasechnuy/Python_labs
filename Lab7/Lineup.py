s=input()
a=[int(s) for s in s.split()]
pet = int(input())
for i in range(len(a)):
    if pet > a[i]:
        print(i+1)
        break