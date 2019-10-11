n, m = [int(i) for i in input().split()]

a = [['.'] * m for i in range(n)]

for i in range(n):
    for j in range(m):
        if (i + j) % 2 != 0:
            a[i][j] = '*'

print('\n'.join([' '.join([str(i) for i in row]) for row in a]))