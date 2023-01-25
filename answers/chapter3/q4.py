def pyth(x1, x2, y1, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


def acute(x1, y1, x2, y2, x3, y3):
    a = pyth(x1, x2, y1, y2)
    b = pyth(x2, x3, y2, y3)
    c = pyth(x3, x1, y3, y1)
    return a + b > c and b + c > a and c + a > b


print(acute(1, 2, 4, 3, 2, 7))
print(acute(1, 2, 4, 2, 5, 4))
print(acute(1, 2, 4, 2, 4, 3))
