# 1
for row in range(3):
    for col in range(3):
        print("*", end=" ")
    print()

# 2
for row in range(3):
    for number in range(1, 4):
        print(number, end=" ")
    print()

# 3
for row in range(1, 4):
    for col in range(3):
        print(row, end=" ")
    print()

# 4
for row in range(1, 6):
    for col in range(row):
        print("*", end=" ")
    print()

# 5
for row in range(5, 0, -1):
    for col in range(row):
        print("*", end=" ")
    print()

# 6
for row in range(1, 6):
    for number in range(1, row + 1):
        print(number, end=" ")
    print()

# 7
for row in range(1, 6):
    for col in range(row):
        print(row, end=" ")
    print()

# 8
for table in range(1, 6):
    for number in range(1, 11):
        print(f"{table} x {number} = {table * number}")
    print()

# 9
for row in range(1, 4):
    for number in range(1, 6):
        print(row * number, end=" ")
    print()

# 10
for row in range(5):
    for number in range(1, 6):
        print(number ** 2, end=" ")
    print()

# 11
for row in range(1, 6):
    for letter in range(row):
        print(chr(65 + letter), end=" ")
    print()

# 12
for row in range(1, 6):
    for col in range(row):
        print(chr(64 + row), end=" ")
    print()

# 13
for row in range(1, 6):
    for number in range(1, row + 1):
        print(2 * number - 1, end=" ")
    print()

# 14
for row in range(1, 6):
    for number in range(1, row + 1):
        print(2 * number, end=" ")
    print()

# 15
for row in range(5):
    for col in range(5):
        print("*", end=" ")
    print()

# 16
for row in range(5):
    for number in range(1, 6):
        print(number, end=" ")
    print()

# 17
number = 1
for row in range(3):
    for col in range(3):
        print(number, end=" ")
        number += 1
    print()

# 18
number = 1
for row in range(4):
    for col in range(5):
        print(number, end=" ")
        number += 1
    print()

# 19
for first in range(1, 4):
    for second in range(1, 4):
        print(f"({first},{second})", end=" ")
    print()

# 20
for first in range(1, 4):
    for second in range(1, 4):
        print(first, second)

# 21
for row in range(1, 11):
    for col in range(1, 11):
        print(f"{row * col:4}", end="")
    print()

# 22
for number in range(1, 6):
    for col in range(number):
        print(number, end="")
    print()

# 23
for row in range(5, 0, -1):
    for number in range(1, row + 1):
        print(number, end="")
    print()

# 24
for row in range(5, 0, -1):
    for number in range(5, 5 - row, -1):
        print(number, end="")
    print()

# 25
for number in range(1, 6):
    for col in range(5):
        print(number, end="")
    print()