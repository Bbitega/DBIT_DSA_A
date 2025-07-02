def find_min(lst):
    min_value = lst[0]
    for num in lst:
        if num < min_value:
            min_value = num
    return min_value


count = int(input("How many numbers do you want to enter? "))

numbers = []
for i in range(count):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

print("Minimum value:", find_min(numbers))