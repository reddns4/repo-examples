# Условие
# Дана последовательность целых чисел, # заканчивающаяся числом 0.
# Выведите эту последовательность в обратном порядке.
# При решении этой задачи нельзя пользоваться массивами и 
# прочими динамическими структурами данных. Рекурсия вам поможет.

# Эту задачу невозможно решить самостоятельно. Обратитесь к 
# своему преподавателю за помощью.

# 1
# 2
# 3
# 0

# A:
# 0
# 3
# 2
# 1

def reverce():
    n = int(input())
    if n != 0:
        reverce()
    print(n)

reverce()
    