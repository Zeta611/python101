lst = [[1, 2], [3, 4]]
lst2 = []
for i in range(len(lst)):
    lst2.append([])
    for j in range(len(lst[i])):
        lst2[i].append(lst[i][j])

print(lst)
print(lst2)

lst[0][0] = 0
print(lst)
print(lst2)
