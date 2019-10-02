n = int(input())
counter = 1
i = 0
prev = 1
prevprev = 0
while i < n:
     i = prev + prevprev
     prevprev = prev
     prev = i
     counter += 1
if i == n:
    print(counter)
else:
    print(-1)