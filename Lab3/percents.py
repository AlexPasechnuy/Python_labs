p = int(input())
x = int(input())
y = int(input())
y += x*100
y = int(y + y*p/100)
print(y//100, y%100)