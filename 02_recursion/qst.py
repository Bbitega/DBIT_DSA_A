def new_func(n):
    # new_func(n)
    if n == 0:
        # print("Stop")
        return 0
    else:
        print(f"Value of n is {n}")
        new_func(n - 1)  # function calling itself 
    
new_func(5)