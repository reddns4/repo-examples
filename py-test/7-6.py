# Условие
# Дан список чисел. Выведите значение наибольшего элемента в списке, а затем индекс этого элемента в списке. Если наибольших элементов несколько, выведите индекс первого из них.

# -5 -4 -3 -2 -1
# -1 4

# 3 2 1
# 3 0

a = [int(i) for i in input().split()]

max_val = a[0]
index = 0

for i in range(0, len(a)):
    if (a[i] > max_val):
        max_val = a[i]
        index = i

print(max_val, index)