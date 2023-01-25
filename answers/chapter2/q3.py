import math


def gaussian(mu, sigma, x):
    coeff = 1 / (sigma * math.sqrt(2 * math.pi))
    expon = - 1 / 2 * ((x - mu) / sigma) ** 2
    return coeff * math.exp(expon)


print(gaussian(0, 1, 0))                # 0.3989422804014327
print(gaussian(-2, math.sqrt(0.5), 0))  # 0.010333492677046037
