import pytest

from arrays import functions


@pytest.mark.parametrize("arr, value, expected", [
    ([1, 2, 3, 4, 5], 4, 3),
    ([1, 2, 3, 4, 4], 100, -1),
])
def test_search_elem(arr, value, expected):
    result = functions.search_elem(arr, value)
    assert result == expected


@pytest.mark.parametrize("arr, n, expected", [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13], 13, 11),
    ([1, 2, 4, 5, 6], 6, 3),
])
def test_missing_number(arr, n, expected):

    result = functions.missing_number(arr, n)
    assert result == expected


@pytest.mark.parametrize("arr, target, expected", [
    ([1, 2, 3, 4, 5], 7, [[1, 4], [2, 3]]),
    ([1, 2, 3, 4, 5, 99, 1, 100], 100, [[0, 5], [5, 6]]),
])
def test_integer_pairs(arr, target, expected):
    result = functions.integer_pairs(arr, target)
    assert result == expected


@pytest.mark.parametrize("arr, expected", [
    ([1, 3, 3, 8, 9, 6], 72),
])
def test_max_product(arr, expected):
    result = functions.max_product(arr)
    assert result == expected


@pytest.mark.parametrize("arr, expected", [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 15),
    ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 34),
    # ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], 18),  # not square matrix
])
def test_diagonal_sum(arr, expected):
    result = functions.diagonal_sum(arr)
    assert result == expected


@pytest.mark.parametrize("arr, expected", [
    ([84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0], (90, 87)),
])
def test_first_second(arr, expected):
    result = functions.first_second(arr)
    assert result == expected


@pytest.mark.parametrize("arr, expected", [
    ([1, 2, 2, 4, 2, 4, 4, 5, 5, 2, 3], [1, 2, 3, 4, 5]),
    ([6, 6, 7, 5, 5, 4, 3, 2, 2, 1, 0], [0, 1, 2, 3, 4, 5, 6, 7]),
    ([-2, -2, 0, 0, 1, 2, 3, 4, 3], [-2, 0, 1, 2, 3, 4]),
])
def test_remove_duplicates(arr, expected):
    result = functions.remove_duplicates(arr)
    assert result == expected


@pytest.mark.parametrize("arr, target, expected", [
    ([2, 4, 3, 5, 6, -2, 4, 7, 8, 9], 7, ["2+5", "4+3", "3+4", "-2+9"]),
])
def test_pair_sum(arr, target, expected):
    result = functions.pair_sum(arr, target)
    assert result == expected


@pytest.mark.parametrize("arr, expected", [
    ([1, 2, 3, 1], True)
])
def test_contains_duplicate(arr, expected):
    result = functions.contains_duplicate(arr)
    assert result == expected


@pytest.mark.parametrize("list1, list2, expected", [
    ([1, 2, 3, 4], [4, 3, 2, 1], True),
    ([1, 3, 3, 5], [5, 4, 3, 2], False),
    (["a", "b", "c", "d"], ["a", "b", "c", "d"], True)
])
def test_permutation(list1, list2, expected):
    result = functions.permutation(list1, list2)
    assert result == expected


@pytest.mark.parametrize("matrix, expected", [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
])
def test_rotate(matrix, expected):
    result = functions.rotate(matrix)
    assert result == expected
