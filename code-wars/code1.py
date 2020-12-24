# in: 
# 9119

# out:
# 811181

def square_digits(num):
    res = ''
    for c in str(num):
        res += str(int(c) ** 2)
    return int(res)

print(square_digits(9119))