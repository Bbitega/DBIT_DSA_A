def linear_search(values, target):
    for index in range(len(values)):
        if values[index] == target:
            return index
    return -1

# Example:
values = [9, 8, 7, 6, 5, 4, 3, 2, 1]
target = int(input("Enter value to search for: "))
result = linear_search(values, target)
print("Index:", result)

