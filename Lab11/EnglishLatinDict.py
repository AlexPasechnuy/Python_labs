from collections import defaultdict

d = defaultdict(list)

for i in range(int(input())):
    english, latins = input().split(' - ')
    latin = latins.split(', ')
    d[english] = []
    for i in latin:
        d[i].append(english)

print(len(d))

for latin, english in sorted(d.items()):
    print(latin + ' - ' + ', '.join(english))