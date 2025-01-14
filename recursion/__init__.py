

def factorial(n):
    if n < 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    """

    n: int - the nth number in the fibonacci sequence
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
