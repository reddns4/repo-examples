# Условие
# Дан список. Выведите те его элементы, которые встречаются в списке только один раз. Элементы нужно выводить в том порядке, в котором они встречаются в списке.

# 4 3 5 2 5 1 3 5
# A: 4 2 1

a = [int(i) for i in input().split()]

found = 0

for i in range(len(a)):
    found = 0
    for j in range(len(a)):
        if (i != j) and (a[i] == a[j]):
            found = 1
            break
        
    if (found == 0):
        print(a[i], end=' ')
