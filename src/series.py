def fib_func(n):
    if n<2:
        return n
    return fib_func(n-2) + fib_func(n-1)