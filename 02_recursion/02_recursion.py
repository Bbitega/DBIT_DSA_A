def recursion(num):
    print(num)
    # base case
    if num <= 3:
        return 1
    else:
        # recursive case
        return recursion(num // 2)

num = int(input("Enter a number: "))
recursion(num)