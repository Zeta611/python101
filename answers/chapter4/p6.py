def area(p):
    n = len(p)
    area = 0
    for i in range(n):
        xi = p[i][0]
        dy = p[(i + 1) % n][1] - p[(i - 1) % n][1]
        area += xi * dy
    return abs(area) / 2


def perimeter(p):
    n = len(p)
    perimeter = 0
    for i in range(n):
        dx = p[i % n][0] - p[(i + 1) % n][0]
        dy = p[i % n][1] - p[(i + 1) % n][1]
        perimeter += (dx ** 2 + dy ** 2) ** 0.5
    return perimeter


points = [[3, 1], [6, 3], [4, 4], [7, 6], [2, 7], [0, 5], [2, 3], [1, 2]]
print(perimeter(points))
