n, m = [int(i) for i in input().split()]
a = set()
b = set()
for i in range (n):
    a.add(int(input()))
for i in range (m):
    b.add(int(input()))

print(len(a&b), '\n', *[str(item) for item in sorted(a&b)])
print(len(a-b), '\n', *[str(item) for item in sorted(a-b)])
print(len(b-a), '\n', *[str(item) for item in sorted(b-a)])
