import math


def f(a, b, c, x):
    return a * x ** 2 + b * x + c


def min_x(a, b, c):
    x = -b / (2 * a)
    if x == int(x):
        return x

    x1 = math.floor(x)
    y1 = f(a, b, c, x1)
    x2 = x1 + 1
    y2 = f(a, b, c, x2)
    if y1 < y2:
        return x1
    elif y1 == y2 and x1 < x2:
        return x1
    else:
        return x2


print(min_x(1, -9, 2))    # 4
print(min_x(9, -5, 0))  # 0
print(min_x(9, -15, 0))  # 1
print(min_x(7, -13, 3))  # 1
