n = int(input())

a = [[0] * n for i in range(n)]

for i in range(n):
    a[i][n - 1 - i] = 1
    for j in range(n - i, n):
        a[i][j] = 2

print('\n'.join([' '.join([str(i) for i in row]) for row in a]))