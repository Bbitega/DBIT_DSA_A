def recursion(num):
    print(num)
    num += 1
    # num = num + 1
    return recursion(num)


recursion(1)