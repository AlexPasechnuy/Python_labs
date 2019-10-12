max = int(input())
possible = set(range(1,max+1))
res = possible
while True:
    arr = input()
    if arr == 'HELP':
        break
    arr = {int(i) for i in arr.split()}
    answ = input()
    if answ == "YES":
        res &= arr
    else:
        res &= possible - arr
print(*[str(item) for item in sorted(res)])