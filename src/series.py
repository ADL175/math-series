def fib_func(n):
    """Return fib value"""
    if n == 1:
        return 1
    elif n == 0:
        return 0
    return fib_func(n - 2) + fib_func(n - 1)


def lucas_func(n):
    """Return lucus value."""
    if n == 1:
        return 1
    elif n == 0:
        return 2
    return lucas_func(n - 2) + lucas_func(n - 1)


def sum_series(n, x=0, y=1):
    """Return sum series return value."""
    if n == 1:
        return y
    elif n == 0:
        return x
    return sum_series(n - 2, x, y) + sum_series(n - 1, x, y)


if __name__ == "__main__":
    sum_series(4)
