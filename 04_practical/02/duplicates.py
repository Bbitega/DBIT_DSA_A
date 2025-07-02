def has_duplicates(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return True
    return False


count = int(input("How many numbers do you want to enter? "))

numbers = []

for i in range(count):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

if has_duplicates(numbers):
    print("There are duplicates in the list.")
else:
    print("There are no duplicates in the list.")