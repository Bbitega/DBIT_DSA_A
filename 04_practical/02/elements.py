def sum_of_elements(list):
    total = 0
    for num in list:
        total += num
    return total


count = int(input("How many numbers do you want to add? "))

numbers = []
for i in range(count):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

print("Sum:", sum_of_elements(numbers))