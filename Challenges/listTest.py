numbers = [0, 1, 2, 3, 4, 5, 6]
print(numbers)
print(len(numbers))

del numbers[1]
print(numbers)

if 3 in numbers:
    print("3 znajduje się w liście numbers")

for num in numbers:
    print(num)
    numbers = [num * 2]
    print(numbers)