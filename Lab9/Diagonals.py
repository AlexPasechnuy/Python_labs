n = int(input())

a = [[0] * n for i in range(n)]

for i in  range(1, n):
    for j in range(n-i):
        a[j][j+i]=i
        a[j+i][j]=i

print('\n'.join([' '.join([str(i) for i in row]) for row in a]))