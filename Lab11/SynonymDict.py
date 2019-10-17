num = int(input())
a = dict()
for i in range(num):
    w1, w2 = [i for i in input().split()]
    a[w1] = w2
    a[w2] = w1
print (a[input()])