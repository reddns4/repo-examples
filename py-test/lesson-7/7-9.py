# Условие
# Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т. д.). Если элементов нечетное число, то последний элемент остается на своем месте.

a = [int(i) for i in input().split()]

last_element = a[-1]

for i in range(1, len(a)):
    if (i % 2) != 0:
        print(a[i], a[i-1], end=' ')

if (len(a) % 2) != 0:
    print(last_element, end=' ')

