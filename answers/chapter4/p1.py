def sum_squares(a):
    summ = 0
    for i in range(len(a)):
        summ += a[i] ** 2
    return summ


print(sum_squares([3, 5, 4]))  # 50
print(sum_squares([2, 5, 4, 0, 1, -1, 5, 1]))  # 73
