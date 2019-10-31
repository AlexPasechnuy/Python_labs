def parents(child):
    result = []
    result.append(child)
    while child in d:
        child = d[child]
        result.append(child)
    return result

d = dict()
for i in range(int(input())-1):
    son, father = input().split()
    d[son] = father

for i in range(int(input())):
    ch1, ch2 = input().split()
    parents_1 = parents(ch1)
    for parents_2 in parents(ch2):
        if parents_2 in parents_1:
            print(parents_2)
            break