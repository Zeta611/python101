def f(a, b, c, x):
    return a * x ** 2 + b * x + c


def extremum(a, b, c):
    # 2ax + b = 0
    x = -b / (2 * a)
    return f(a, b, c, x)


print(extremum(1, 5, 10))  # 3.75
print(extremum(1, -5, 10))  # 3.75
print(extremum(3, 7, 5))  # 0.916666666667
