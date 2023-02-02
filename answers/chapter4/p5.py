def fibonacci(n):
    result = []
    fi, fj = 1, 1
    for _ in range(n):
        result.append(fi)
        fi, fj = fj, fi + fj
    return result


print(fibonacci(10))
