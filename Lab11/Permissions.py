n = int(input())
a = dict()
for i in range (n):
    str , *perm = input().split()
    a[str] = perm

n = int(input())
for i in range (n):
    perm, file = input().split()
    if perm == "read" and 'R' in a[file]:
        print("OK")
    elif perm == "write" and 'W' in a[file]:
        print("OK")
    elif perm == "execute" and 'X' in a[file]:
        print("OK")
    else:
        print("Access denied")