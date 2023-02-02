def prime(p):
    for i in range(2, p // 2 + 1):
        if p % i == 0:
            return False
    return True


def sum_two_prime_squares(n):
    for i_sqrt in range(2, int(n ** 0.5) + 1):
        j = n - i_sqrt ** 2
        j_sqrt = int(j ** 0.5)
        if j_sqrt ** 2 == j and prime(i_sqrt) and prime(j_sqrt):
            return True
    return False


for n in range(50, 61):
    print(n, sum_two_prime_squares(n))
