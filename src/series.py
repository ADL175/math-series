def fib_func(n):
    if n<2:
        return n
    return fib_func(n-2) + fib_func(n-1)

def lucas_func(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    return lucas_func(n -1) + lucas_func(n -2)
