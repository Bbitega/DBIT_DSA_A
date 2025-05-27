def funB(num):
    print(f"Function B {num}")
    if num > 0:
        return funA(num - 1)
    return None


def funA(num):
    print(f"Function A {num}")
    if num > 0:
        return funB(num-1)
    return None

funB(5)