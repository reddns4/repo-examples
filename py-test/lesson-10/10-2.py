# Условие
# Даны два списка чисел. Посчитайте, сколько чисел содержится 
# одновременно как в первом списке, так и во втором.

# Примечание. Эту задачу на Питоне можно решить в одну строчку.

# 1 3 2
# 4 3 2

# A:
# 2

print(len(set(input().split()) & set(input().split())))
