import pytest


from tuples import functions


@pytest.mark.parametrize("the_tuple, expected", [
    ((1, 2, 3, 4), (10, 24)),
])
def test_functions_sum_product(the_tuple, expected):
    result = functions.sum_product(the_tuple)
    assert result == expected


@pytest.mark.parametrize("tuple1, tuple2, expected", [
    ((1, 2, 3), (4, 5, 6), (5, 7, 9)),
])
def test_functions_sum_elemetwise(tuple1, tuple2, expected):
    result = functions.sum_elementwise(tuple1, tuple2)
    assert result == expected


@pytest.mark.parametrize("the_tuple, value, expected", [
    ((2, 3, 4), 1, (1, 2, 3, 4))
])
def test_functions_insert_value_front(the_tuple, value, expected):
    result = functions.insert_value_front(the_tuple, value)
    assert result == expected


@pytest.mark.parametrize("the_tuple, expected", [
    (("Hello", "world", "from", "Python"), "Hello world from Python"),
])
def test_functions_concatenate_strings(the_tuple, expected):
    result = functions.concatenate_strings(the_tuple)
    assert result == expected


@pytest.mark.parametrize("the_tuple, expected", [
    (((1, 2, 3), (4, 5, 6), (7, 8, 9)), (1, 5, 9)),
    (((3, 7, 9), (4, 5, 1), (1, 7, 3)), (3, 5, 3)),
])
def test_functions_get_diagonal(the_tuple, expected):
    result = functions.get_diagonal(the_tuple)
    assert result == expected


@pytest.mark.parametrize("tuple1, tuple2, expected", [
    ((1, 2, 3, 4, 5), (4, 5, 6, 7, 8), (4, 5)),
])
def test_functions_common_elements(tuple1, tuple2, expected):
    result = functions.common_elements(tuple1, tuple2)
    assert result == expected
