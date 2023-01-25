def count_coins(n):
    cnt = n // 500
    n %= 500
    cnt += n // 100
    n %= 100
    cnt += n // 50
    n %= 50
    cnt += n // 10
    n %= 10
    return cnt


print(count_coins(730))  # 6
print(count_coins(790))  # 8
print(count_coins(260))  # 4
print(count_coins(70))  # 3
