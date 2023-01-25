def d(n):
    result = 0
    for m in range(1, n):
        if n % m == 0:
            result += m
    return result


def is_amicable(n):
    a = d(n)
    return d(a) == n and n != a


def sum_amicable(n):
    summ = 0
    for m in range(1, n):
        if is_amicable(m):
            summ += m
    return summ


print(sum_amicable(10000))
