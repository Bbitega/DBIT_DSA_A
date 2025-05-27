def getFactorial(n):
    print(n)
    if n == 0 or n == 1:
        return 1
    return n * getFactorial(n - 1)


fact = getFactorial(5)
print(fact)