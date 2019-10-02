n = int(input())
if(n == 0):
    print(0)
elif(n == 1):
    print(1)
else:
    i = 2
    prev = 1
    prevprev = 0
    while i <= n:
        this = prev + prevprev
        prevprev = prev
        prev = this
        i += 1
    print(prev)