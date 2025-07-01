# comment
def linear_search(values):
    target = int(input("Enter values to search : "))
    for item in values:
        if item == target:
            return item
        
    return "Item not found"

values = [9,8,7,6,5,4,3,2,1]
print(f"List of values {values}")

ans = linear_search(values)
print(ans)