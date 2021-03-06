# Условие

# Известно, что на доске 8×8 можно расставить 8 ферзей так, 
# чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске,
# определите, есть ли среди них пара бьющих друг друга.

# Программа получает на вход восемь пар чисел, каждое число 
# от 1 до 8 — координаты 8 ферзей. Если ферзи не бьют друг друга,
# выведите слово NO, иначе выведите YES.

# X Yif 
# 1 7
# 2 4
# 3 2
# 4 8
# 5 6
# 6 1
# 7 3
# 8 5
# A: NO

# 3 4
# 7 6
# 6 8
# 4 7
# 4 1
# 2 2
# 1 5
# 5 3
# A: YES

x, y = [], []
t1, t2 = 0, 0
deb = 0
res = 'NO'
n = 8

for i in range(n):
    t1, t2 = [int(i) for i in input().split()]
    x.append(t1)
    y.append(t2)

if deb:
    print(x)
    print(y)
    
#-------------------------------    
for i in range(n):
    for j in range(n):
        if i != j:
            
            # Проверить песечение координат по X 
            if x[i] == x[j]:
                res = 'YES'
                break
            
            # Проверить песечение координат по Y
            if y[i] == y[j]:
                res = 'YES'
                break
            
            # Проверить песечение координат по диагонал
            if x[i] == x[j] or y[i] == y[j]:
                res = 'YES'
                break
            elif (x[i] + y[i]) == (x[j] + y[j]):
                res = 'YES'
                break
            elif (x[i] - y[i]) == (x[j] - y[j]):
                res = 'YES'
                break

print(res)
