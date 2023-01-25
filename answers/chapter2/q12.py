def ceil(x):
    if x == int(x):
        return x
    if x > 0:
        return int(x) + 1
    else:
        return int(x)


print(ceil(4.3))  # 5
print(ceil(-0.3))  # 0
print(ceil(0.01))  # 1
