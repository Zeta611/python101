def reverse(n):
    result = 0
    if n >= 1000:
        result += n % 10
        n //= 10
    if n >= 100:
        result *= 10
        result += n % 10
        n //= 10
    if n >= 10:
        result *= 10
        result += n % 10
        n //= 10
    if n >= 1:
        result *= 10
        result += n % 10
        n //= 10
    return result


print(reverse(3702))  # 2073
print(reverse(370))  # 73
print(reverse(37))  # 73
print(reverse(3))  # 3
