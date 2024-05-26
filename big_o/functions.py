

def find_element():
    # logarithm since it is visiting only some elements
    _array = [1, 2, 3, 4, 4]
    for i in range(0, len(_array), 3):
        print(_array[i])


def print_items(n):
    # eliminate constants: as n -> oo, a constant added to the algorithm doesn't influence to much
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)


def print_items_n_n(n):
    """
    This code complexity is O(n^2), since we have a nested loop
    """
    for i in range(n):
        for j in range(n):
            print(i, j)
    # very inefficient code


def recursive_sum(n):
    """
    recursive functions adds n executions to the memory BEFORE starts to produce results

    recursive_sum(3)
        implies: recursive_sum(3) -> recursive_sum(2) -> recursive_sum(1)
    """
    if n <= 0:
        return 0
    return n + recursive_sum(n - 1)

    # be careful with this kind of functions
