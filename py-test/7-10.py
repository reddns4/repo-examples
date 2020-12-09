# Условие
# В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.

# 3 4 5 2 1

# A:
# 3 4 1 2 5

a = [int(i) for i in input().split()]

max_val = a[0] 
min_val = a[0] 
max_index = 0
min_index = 0

for i in range(0, len(a)):
    if max_val <= a[i]:
        max_val = a[i]
        max_index = i
    
    if min_val >= a[i]:
        min_val = a[i]
        min_index = i 
        
a[max_index], a[min_index] = a[min_index], a[max_index]

print(' '.join([str(i) for i in a]))
