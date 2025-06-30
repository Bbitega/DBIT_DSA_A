def linear_search(values):
<<<<<<< HEAD
    target = int(input("Enter values to search: "))
=======
    target = int(input("Enter values to search : "))
>>>>>>> 759625314e38a56a3464974f94aad0d92232ccdc
    for item in values:
        if item == target:
            return item
        
<<<<<<< HEAD
    return "item not found"

values = [9,8,7,6,5,4,3,2,1]
print(f"List of values {values}")
ans = linear_search(values)
print(ans)
=======
    return "Item not found"

values = [9,8,7,6,5,4,3,2,1]
print(f"List of values {values}")

ans = linear_search(values)
print(ans)
>>>>>>> 759625314e38a56a3464974f94aad0d92232ccdc
