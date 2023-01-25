import math


def intersect(x1, y1, r1, x2, y2, r2):
    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return r1 + r2 > d and abs(r2 - r1) < d


print(intersect(1, 1, 3, 5, 4, 2))
print(intersect(1, 1, 3, 4, 3, 2))
print(intersect(1, 1, 3, 2, 1, 2))
