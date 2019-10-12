n = int(input())
a = set()

for i in range (n):
    s = [i for i in input().split()]
    for word in s:
        a.add(word)
print(len(a))