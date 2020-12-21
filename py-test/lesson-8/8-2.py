# Условие
# Дано действительное положительное число a и целоe число n.
# Вычислите an. Решение оформите в виде функции power(a, n).
# Стандартной функцией возведения в степень пользоваться нельзя.

# 2
# -3

# A: 0.125

def power(a, n):
    res = 1
    
    for i in range(abs(n)):
        res *= a

    if n >= 0:
        return res
    else:
        return 1 / res

a, n = float(input()) , int(input())

print(power(a, n))
