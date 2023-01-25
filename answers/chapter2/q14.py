def area_triangle(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(b) * abs(b / a) / 2


print(area_triangle(1, 1))  # 0.5
print(area_triangle(0, 10))  # 0
print(area_triangle(-2, -2))  # 1.0
