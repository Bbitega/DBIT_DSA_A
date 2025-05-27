def recursion(num):
    print(num)
    if num == 0:
        return None
    return recursion(num//2)


recursion(5_000_000_000)