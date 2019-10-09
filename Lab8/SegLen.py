from math import *

def distance(x1,y1,x2,y2):
    return sqrt(pow(x2-x1,2) + pow(y2-y1,2))

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
print(distance(x1,y1,x2,y2))