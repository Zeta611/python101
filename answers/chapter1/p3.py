import math

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
# Add here!
# (-b +- sqrt(b^2 - 4ac)) / 2a
det = b ** 2 - 4 * a * c
x1 = (-b + math.sqrt(det)) / (2 * a)
x2 = (-b - math.sqrt(det)) / (2 * a)
print("Solutions for the quadratic equation are ", x1, " and ", x2)
