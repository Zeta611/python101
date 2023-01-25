n = int(input("Enter n: "))

sum_squares = n * (n + 1) * (2 * n + 1) // 6
sum_cubes = (n * (n + 1) // 2) ** 2
print(sum_cubes - sum_squares)
