import math

EPSILON_0 = 8.854187817E-12
GRAVITY_G = 6.67408E-11

def coulomb(q1, q2, r):
    coeff = 1 / (4 * math.pi * EPSILON_0)
    return coeff * q1 * q2 / (r ** 2)



def gravity(m1, m2, r):
    return GRAVITY_G * m1 * m2 / (r ** 2)


def total_force(q1, q2, m1, m2, r):
    return -coulomb(q1, q2, r) + gravity(m1, m2, r)


e_c = -1.6021766208e-19
e_m = 9.10938356e-31
p_c = -e_c
p_m = 1.672621898e-27
a_0 = 5.2917721067e-11
print(coulomb(e_c, p_c, a_0))
print(gravity(e_m, p_m, a_0))
print(total_force(e_c, p_c, e_m, p_m, a_0))
