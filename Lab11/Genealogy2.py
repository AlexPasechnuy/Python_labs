def isparent(son, father):
    if son == father:
        return True
    if d[son] not in d:
        return False
    elif d[son] == father:
        return True
    else:
        return isparent(d[son], father)

n = int(input())
d = dict()
for i in range(n-1):
    son, father = input().split()
    d[son] = father

d['Peter_I'] = 'Nan'

for i in range(int(input())):
    name1, name2 = input().split()
    if isparent(name2, name1):
        print(1)
    elif isparent(name1, name2):
        print(2)
    else:
        print(0)