def within_circ(r):
    cnt = 0
    for i in range(-r, r+1):
        for j in range(-r, r+1):
            if i ** 2 + j ** 2 <= r ** 2:
                cnt += 1
    return cnt


def calculate_pi(r):
    return within_circ(r) / (r ** 2)


print(calculate_pi(100))
print(calculate_pi(1000))
