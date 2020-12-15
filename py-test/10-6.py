# Условие
# Дан текст: в первой строке записано число строк,
# далее идут сами строки. Определите, сколько различных слов
# содержится в этом тексте.

# Словом считается последовательность непробельных символов
# идущих подряд, слова разделены одним или большим числом пробелов
# или символами конца строки.

# 4
# She sells sea shells on the sea shore;
# The shells that she sells are sea shells I'm sure.
# So if she sells sea shells on the sea shore,
# I'm sure that the shells are sea shore shells.

# A:
# 19

n = int(input())

a = [input().split() for i in range(n)]
t = set()

for i in range(len(a)):
    for j in range(len(a[i])):
        t.add(a[i][j])

print(len(t)) 