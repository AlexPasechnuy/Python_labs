def swap_columns(a,i,j):
    for c in range(len(a)):
        temp = a[c][i]
        a[c][i] = a[c][j]
        a[c][j] = temp

n, m = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
i, j = [int(i) for i in input().split()]
swap_columns(a, i, j)
print('\n'.join([' '.join([str(i) for i in row]) for row in a]))