max = int(input())
possible = set(range(1,max+1))
res = possible
while True:
    arr = input()
    if arr == 'HELP':
        break
    arr = {int(i) for i in arr.split()}
    if len(res&arr)>len(res)/2:
        print("YES")
        res &= arr
    else:
        print("NO")
        res &= possible - arr
print(*[str(item) for item in sorted(res)])