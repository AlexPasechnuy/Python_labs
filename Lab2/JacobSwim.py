n = int(input())
m = int(input())
x = int(input())
y = int(input())
min = x
if(0 <= n - x < min):
    min = n - x
if(0 <= (y) < min):
    min = y
if(0 <= m - y < min):
    min = m - y
print(min)