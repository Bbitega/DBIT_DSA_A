def numbers(n):
    if n > 0:
        print(n)
        numbers(n-1)
    
    
numbers(12)