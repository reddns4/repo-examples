a = [int(i) for i in input().split()]

cur_val = a[0]
prev_val = 0

for i in range(1, len(a)):

    cur_val, prev_val = a[i], cur_val
    if cur_val > prev_val:
        print(cur_val, end=' ')
