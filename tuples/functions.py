

def sum_product(the_tuple) -> tuple:
    """
    This function calculates the sum and product of all elements
    in a tuple of numbers
    :param the_tuple:
    :return:
    """
    sum_ = 0
    product = 1
    for num in the_tuple:
        sum_ += num
        if num > 0:
            product *= num

    return sum_, product


def sum_elementwise(tuple1, tuple2) -> tuple:
    """
    This function takes two tuples and returns a tuple
    containing the element-wise sum of the input tuples
    :param tuple1:
    :param tuple2:
    :return:
    """
    if len(tuple1) != len(tuple2):
        raise ValueError("Input tuples must have the same length")
    result = tuple(a + b for a, b in zip(tuple1, tuple2))
    return result
    # clever suolution
    # return tuple(map(sum, zip(tuple1, tuple2)))


def insert_value_front(the_tuple, value) -> tuple:
    """
    This function takes a tuple and a value as parameters and returns a new
    tuple with the value inserted at the beginning of the original tuple.
    :param the_tuple:
    :param value:
    :return:
    """
    list_ = list(the_tuple)
    list_.insert(0, value)
    return tuple(list_)

    # clever solution
    # return (value,) + the_tuple


def concatenate_strings(the_tuple) -> str:
    """
    This function take a tuple of strings and concatenate them, separating
    each string with space
    :param the_tuple:
    :return:
    """
    text = " ".join(the_tuple)
    return text


def get_diagonal(the_tuple) -> tuple:
    """
    This function takes a tuple of tuples and returns a tuple containing the
    diagonal elements of the input.
    :param the_tuple:
    :return:
    """
    diag = []
    elem = 0
    for row in the_tuple:
        diag.append(row[elem])
        elem += 1
    return tuple(diag)

    # clever solution
    # return tuple(input_tuple[i][i] for i in range(len(input_tuple)))


def common_elements(tuple1, tuple2) -> tuple:
    """
    This function takes two tuples and returns a tuple containing the common
    elements of the input tuples.
    :param tuple1:
    :param tuple2:
    :return:
    """
    set_ = set(tuple1)
    return tuple(set_.intersection(set(tuple2)))

    # clever solution
    # return tuple( set(tuple1) & set(tuple2) )

