import pytest

from circular.cslinkedlist import CSLinkedList


@pytest.mark.parametrize("value, head, tail", [
    (1, 1, 1),
    (2, 2, 2,),
    (2, 5, 6),
])
def test_cslinkedlist_init(value, head, tail):
    csll = CSLinkedList()
    csll.append(head)
    csll.append(tail)
    assert csll.head.value == head
    assert csll.tail.value == tail


@pytest.mark.parametrize("list1, expected", [
    ([1, 2, 3], [1, 2, 3]),
    ([4, 5, 6], [4, 5, 6]),
])
def test_cslinkedlist_append(list1, expected):
    csll = CSLinkedList()
    for value in list1:
        csll.append(value)
    assert csll.head.value == expected[0]
    assert csll.tail.value == expected[-1]


@pytest.mark.parametrize("list1, expected", [
    ([1, 2, 3], "1 -> 2 -> 3 -> 1"),
    ([4, 5, 6], "4 -> 5 -> 6 -> 4"),
    ([], ""),
    ([1], "1 -> 1"),
    ([1, 2], "1 -> 2 -> 1"),
    ([1, 2, 3, 4, 5], "1 -> 2 -> 3 -> 4 -> 5 -> 1"),
    ([1, 2, 3, 4, 5, 6], "1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 1"),
])
def test_cslinkedlist_str(list1, expected):
    csll = CSLinkedList()
    for value in list1:
        csll.append(value)
    assert str(csll) == expected
