def sum_three_squares(a):
    bound = int(a ** 0.5) + 1
    for i in range(1, bound):
        for j in range(i + 1, bound):
            for k in range(j + 1, bound):
                if i ** 2 + j ** 2 + k ** 2 == a:
                    return True
    return False


for i in range(20, 31):
    print(i, sum_three_squares(i))
