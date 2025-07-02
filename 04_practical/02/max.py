def find_max(lst):
    max_value = lst[0]
    for num in lst:
        if num > max_value:
            max_value = num
    return max_value


count = int(input("How many numbers do you want to enter? "))

numbers = []

for i in range(count):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

print("Maximum value:", find_max(numbers))