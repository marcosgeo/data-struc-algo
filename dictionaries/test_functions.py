import pytest

from . import functions


@pytest.mark.parametrize("words, expected", [
    (
        ["apple", "orange", "banana", "apple", "orange", "apple"],
        {"apple": 3, "orange": 2, "banana": 1}
    ),
])
def test_count_word_frequency(words, expected):
    result = functions.count_word_frequency(words)
    assert result == expected


@pytest.mark.parametrize("dict1, dict2, expected", [
    (
        {'a': 1, 'b': 2, 'c': 3},
        {'c': 2, 'd': 4, 'e': 5},
        {'a': 1, 'b': 2, 'c': 5, 'd': 4, 'e': 5}),
])
def test_merge_dicts(dict1, dict2, expected):
    result = functions.merge_dicts(dict1, dict2)
    assert result == expected


@pytest.mark.parametrize("the_dict, expected", [
    ({'a': 5, 'b': 9, 'c': 2}, 'b'),
])
def test_max_value_key(the_dict, expected):
    result = functions.max_value_key(the_dict)
    assert result == expected


@pytest.mark.parametrize("the_dict, expected", [
    ({'a': 1, 'b': 2, 'c': 3}, {1: 'a', 2: 'b', 3: 'c'})
])
def test_reverse_dict(the_dict, expected):
    result = functions.reverse_dict(the_dict)
    assert result == expected


@pytest.mark.parametrize("the_dict, function, expected", [
    ({'a': 1, 'b': 2, 'c': 3, 'd': 4}, lambda k, v: v % 2 == 0, {'b': 2, 'd': 4}),
])
def test_filter_dict(the_dict, function, expected):
    result = functions.filter_dict(the_dict, function)
    assert result == expected


@pytest.mark.parametrize("list1, list2, expected", [
    ([1, 2, 3, 4, 5], [3, 1, 2, 1, 3], False),
    ([1, 2, 3, 4, 5], [5, 4, 3, 1, 2], True),
])
def test_check_same_frequency(list1, list2, expected):
    result = functions.check_same_frequency(list1, list2)
    assert result == expected
