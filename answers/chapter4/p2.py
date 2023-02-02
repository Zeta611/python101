def compute_polynomial(a, x):
    summ = 0
    for i in range(len(a)):
        summ += a[i] * x ** i
    return summ


print(compute_polynomial([3, 5, 4], 5))  # 128
print(compute_polynomial([2, 0, 4, 0, 1, -1, 5, 1], 3))  # 5708
