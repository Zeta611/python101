import time

start = time.time()
for i in range(1, 3):
    for j in range(1, 3):
        print(i * j, end=" ")
    print()

end = time.time()
print(f"Took {end - start}s")
