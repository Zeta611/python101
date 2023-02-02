# BEWARE: This is NOT the best implementation out there!

def prime(p):
    for i in range(2, p // 2 + 1):
        if p % i == 0:
            return False
    return True


def count_composite(numbers):
    cnt = 0
    for i in range(len(numbers)):
        if not prime(numbers[i]):
            cnt += 1
    return cnt


numbers = [217, 287, 181, 143, 163, 319, 233, 399, 203]
print(count_composite(numbers))
