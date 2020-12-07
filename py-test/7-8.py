# Условие
# Дан список, упорядоченный по неубыванию элементов в нем. Определите, сколько в нем различных элементов.

a = [int(i) for i in input().split()]

count = 0

for i in range(0, len(a)):
    if a[i-1] != a[i]:
        count += 1
        
if count == 0:
    count += 1


print(count)