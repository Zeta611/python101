def within_rect(top, bottom, left, right, x, y):
    return left <= x <= right and bottom <= y <= top


print(within_rect(2, -4, -5, 6, -5, 2))
print(within_rect(2, -4, -5, 6, 6, -1))
print(within_rect(2, -4, -5, 6, 0, 1))
print(within_rect(2, -4, -5, 6, -6, 0))
print(within_rect(2, -4, -5, 6, 0, 3))


def count_within_rect(top, bottom, left, right, points):
    cnt = 0
    for i in range(len(points)):
        if within_rect(top, bottom, left, right, points[i][0], points[i][1]):
            cnt += 1
    return cnt


points = [
    [2, 1], [7, 5], [-5, 2], [-3, 5], [-7, 4], [-2, -1],
    [-2, -4], [-4, -2], [-6, -4], [4, -4], [6, -2],
]
print(count_within_rect(2, -4, -5, 6, points))
