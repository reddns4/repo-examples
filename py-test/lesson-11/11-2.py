# Условие
# Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом 
# к парному ему слову. Все слова в словаре различны.

# Для слова из словаря, записанного в последней строке, определите его синоним.

# 3
# Hello Hi
# Bye Goodbye
# List Array
# Goodbye

# A: 
# Bye

d = dict()
for i in range(int(input())):
    first, second = input().split()
    d[first] = second
    d[second] = first
print(d[input()])

