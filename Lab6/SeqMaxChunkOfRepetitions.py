i = int(input())
prev = i
counter = 1
maxCounter = 1
while i != 0:
     i = int(input())
     if(i == prev):
         counter += 1
     else:
         if(counter > maxCounter):
             maxCounter = counter
         counter = 1
     prev = i
print(maxCounter)