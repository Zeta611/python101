def prime(p):
    for i in range(2, p // 2 + 1):
        if p % i == 0:
            return False
    return True


def sum_two_primes(n):
    for i in range(2, n // 2 + 1):
        if prime(i) and prime(n - i):
            return True
    return False


for n in range(20, 31):
    print(n, sum_two_primes(n))
