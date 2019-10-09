def power(a,n):
    res = 1
    for i in range(abs(n)):
        res = res*a
    if n < 0:
        res = 1/res
    return res

a = int(input())
n = int(input())
print(power(a,n))