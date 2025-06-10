def sum_to_n(n, acc=0):
    if n == 0:
        return acc
    return sum_to_n(n - 1, acc + n)

print("Sum up to 5:", sum_to_n(5))