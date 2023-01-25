def least(a, b, c):
    if a <= b and a <= c:
        return a
    if b <= a and b <= c:
        return b
    return c


print(least(1, 2, 3))  # 1
print(least(2, 1, 3))  # 1
print(least(1, 1, 2))  # 1
