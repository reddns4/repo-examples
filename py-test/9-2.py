# Условие
# Дано нечетное число n. Создайте двумерный массив из n×n элементов,
# заполнив его символами "." (каждый элемент массива является строкой
# из одного символа). Затем заполните символами "*" среднюю строку массива,
# средний столбец массива, главную диагональ и побочную диагональ. 
# В результате единицы в массиве должны образовывать изображение звездочки.
# Выведите полученный массив на экран, разделяя элементы массива пробелами.

# 7
# A:
# * . . * . . *
# . * .3 * . * .
# . . * * * . .
# * * * * * * *
# . . * * * . .
# . * . * . * .
# * . . * . . *

# А потом и цыкл с 1 до 100 с этими снежынками


n = int(input())

m = [['.' for j in range(n)] for i in range(n)]

# Заполнение *
for i in range(n):
    for j in range(n):
        if (i == j) or i == (n // 2) or j == (n // 2) or (i + j == (n - 1)):
            m[i][j] = '*'

# Вывод
for i in range(n):
    for j in range(n):
        print(m[i][j], end=' ')
    print()
