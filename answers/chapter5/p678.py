def all_distinct(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(i + 1, n):
            if numbers[i] == numbers[j]:
                return False
    return True


print(all_distinct([1,3,2,5,2,1]))
print(all_distinct([1,0,2,5,3,4]))


def all_within_range(numbers, lower, upper):
    for i in range(len(numbers)):
        if not (lower <= numbers[i] <= upper):
            return False
    return True


print(all_within_range([1,0,2,6,3,4],0,5))
print(all_within_range([1,0,2,5,3,4],0,5))


def permutation(n):
    return all_distinct(n) and all_within_range(n, 0, len(n) - 1)


print(permutation([1,3,2,5,2,1]))
print(permutation([1,0,2,5,3,4]))
print(permutation([1,0,2,6,3,4]))
