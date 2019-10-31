def get_height(man):
    if man not in d:
        return 0
    else:
        return 1 + get_height(d[man])

n = int(input())
d = dict()
for i in range(n-1):
    son, father = input().split()
    d[son] = father

heights = {}
for i in set(d.keys()).union(set(d.values())):
    heights[i] = get_height(i)

for name, height in sorted(heights.items()):
    print(name, height)