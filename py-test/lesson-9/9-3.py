# Условие
# Даны два числа n и m. Создайте двумерный массив размером n×m и 
# заполните его символами "." и "*" в шахматном порядке. В левом 
# верхнем углу должна стоять точка.

# 3 4

# . * . *
# * . * .
# . * . *

n, m = [int(j) for j in input().split()]
a = [['.' for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        if ((j % 2 != 0) and ((i+1) % 2 != 0)) or ((i % 2 != 0) and ((j+1) % 2 != 0)):
            a[i][j] = '*'

for row in a:
    print(' '.join(row))