# Условие
# Дан двумерный массив и два числа: i и j. 
# Поменяйте в массиве столбцы с номерами i и j и выведите результат.

# Программа получает на вход размеры массива n и m, 
# затем элементы массива, затем числа i и j.

# Решение оформите в виде функции swap_columns(a, i, j).

# 3 4
# 11 12 13 14
# 21 22 23 24
# 31 32 33 34
# 0 1

# A:
# 12 11 13 14
# 22 21 23 24
# 32 31 33 34

# deb 0 0 77
# deb 0 1 88
# deb 0 2 13
# deb 0 3 14
# deb 1 0 77
# deb 1 1 88
# deb 1 2 23
# deb 1 3 24
# deb 2 0 77
# deb 2 1 88
# deb 2 2 33
# deb 2 3 34
# 77 88 13 14
# 77 88 23 24
# 77 88 33 34

def swap_columns(a, c1, c2): 
    for i in range(len(a)):
        a[i][c1], a[i][c2] = a[i][c2], a[i][c1]
    return a

# Read n, m
n, m = [int(j) for j in input().split()]

# Init
a = []

# Read array
for i in range(n):
    a.append([int(j) for j in input().split()])

# Read i j
i, j = [int(j) for j in input().split()]

# So some
a = swap_columns(a, i, j)

# Print
for row in a:
    print(' '.join([str(e) for e in row]))

