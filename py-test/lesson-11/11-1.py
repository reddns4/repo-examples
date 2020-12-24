# Условие
# В единственной строке записан текст. Для каждого слова из данного текста 
# подсчитайте, сколько раз оно встречалось в этом тексте ранее.

# Словом считается последовательность непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов или символами конца строки.

# one one tho three one one
# 0 1 0 0 2 3

# a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36

# bfs dejkstra bubble sort floid kmp z-function kormen bfs dejkstra bubble sort qsort merge sort heap sort genetic algorythm
# 0 0 0 0 0 0 0 0 1 1 1 1 0 0 2 0 3 0 0

# a b a c a b a
# 0 0 1 0 2 1 3

line = str(input()).split()
d = dict()

for word in line:
    d[word] = d.get(word, -1) + 1
    print(d[word], end=' ')
