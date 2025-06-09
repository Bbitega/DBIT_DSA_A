def numbers(n):
    if n > 0:
        print(f"{n}")
        numbers(n-1)


numbers(12)