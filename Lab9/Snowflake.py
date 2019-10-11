n = int(input())

a = [['.'] * n for i in range(n)]

for i in range (n):
    a[n//2][i] = '*'
    a[i][n//2] = '*'
    a[i][i] = '*'
    a[i][n - 1 -i] = '*'

print('\n'.join([' '.join([str(i) for i in row]) for row in a]))