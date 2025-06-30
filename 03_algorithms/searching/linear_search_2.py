def linear_search(values):
    target = int(input("Enter values to search : "))
    for index, item in enumerate(values):
        if item == target:
            return index
        
    return -1

values = [-1,9,8,7,6,5,4,3,-2,1]
print(f"List of values {values}")

ans = linear_search(values)

if ans != -1:
    print(f"{values[ans]} found at index {ans}")
else:
    print("Not Found")