def d(n):
    result = 0
    for m in range(1, n):
        if n % m == 0:
            result += m
    return result


def is_amicable(b):
    a = d(b)
    return d(a) == b and b != a


def sum_amicable(n):
    summ = 0
    for m in range(1, n):
        if is_amicable(m):
            summ += m
    return summ


print(sum_amicable(10000))
