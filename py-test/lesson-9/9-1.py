# Условие
# Найдите индексы первого вхождения максимального элемента. 
# Выведите два числа: номер строки и номер столбца, в которых 
# стоит наибольший элемент в двумерном массиве. Если таких 
# элементов несколько, то выводится тот, у которого меньше 
# номер строки, а если номера строк равны то тот, у которого 
# меньше номер столбца.

# Программа получает на вход размеры массива n и m, 
# затем n строк по m чисел в каждой.

# 3 4
# 0 3 2 4
# 2 3 5 5
# 5 1 2 3

# A:
# 1 2

a = []
n, m = 0, 0
max_val = 0
max_col = 0
max_row = 0

n, m = [int(j) for j in input().split()]

for i in range(n):
    a.append([int(j) for j in input().split()])

max_val = a[0][0]

for i in range(n):
    for j in range(m):
        if a[i][j] > max_val:
            max_val = a[i][j]
            max_col = i
            max_row = j
            
print(max_col, max_row)