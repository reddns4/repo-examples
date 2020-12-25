# Условие
# Дан текст: в первой строке задано число строк, далее идут сами строки.
# Выведите слово, которое в этом тексте встречается чаще всего. 
# Если таких слов несколько, выведите то, которое меньше в лексикографическом 
# порядке.

# 3
# q w e r t y u i o p
# a s d f g h j k l
# z x c v b n m

# A:
# a

d = {}

for _ in range(int(input())):
    for word in input().split():
        d[word] = d.get(word, 0) + 1
        
max = max(d.values())

for k, v in sorted(d.items()):
    if v == max:
        print(k)
        break