def harmonic_mean(a):
    n = len(a)
    summ = 0
    for i in range(n):
        summ += 1 / a[i]
    return n / summ


def geometric_mean(a):
    n = len(a)
    prod = 1
    for i in range(n):
        prod *= a[i]
    return prod ** (1 / n)


numbers = [2, 4, 3, 10, 7, 2, 5, 6]
print(harmonic_mean(numbers))  # 3.64820846906
print(geometric_mean(numbers))  # 4.22116731332
