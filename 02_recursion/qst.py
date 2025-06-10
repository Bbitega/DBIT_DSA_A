def new_func(n):
<<<<<<< HEAD

    if n  == 0:
        #print("Stop")
        return 0
    else:
        print(f"Value of n is {n}")
        new_func(n-1) #function calling itself

=======
    # new_func(n)
    if n == 0:
        # print("Stop")
        return 0
    else:
        print(f"Value of n is {n}")
        new_func(n - 1)  # function calling itself 
    
>>>>>>> 58f25af5173a03204e85e3810f5fb62b2a19640c
new_func(5)