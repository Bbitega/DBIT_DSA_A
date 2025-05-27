def head_recursion(num):
    if num == 0:
        return 0
    head_recursion(num - 1)
    print(f"{num} Head recursion")
    return None

head_recursion(12)