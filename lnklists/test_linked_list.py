import pytest

from .linked_list import LinkedList, Node


@pytest.mark.parametrize("lst_val_1, lst_val_2, lst_val_3, src_val, expected", [
    (30, 45, 60, 45, 1),
    (10, 25, 30, 10, 0),
    (11, 14, 17, 17, 2),
    (1, 6, 9, 10, -1),
])
def test_linked_list_search(lst_val_1, lst_val_2, lst_val_3, src_val, expected):
    lnk_list = LinkedList()
    lnk_list.append(lst_val_1)
    lnk_list.append(lst_val_2)
    lnk_list.append(lst_val_3)
    result = lnk_list.search(src_val)
    assert result == expected


@pytest.mark.parametrize("val_1, val_2, val_3, search_index, expected", [
    (2, 4, 8, 2, Node(8)),
    (10, 50, 80, 1, Node(50)),
])
def test_linked_list_get(val_1, val_2, val_3, search_index, expected):
    lnk_list = LinkedList()
    lnk_list.append(val_1).append(val_2).append(val_3)
    result: Node = lnk_list.get(search_index)
    assert result.value == expected.value


@pytest.mark.parametrize("val_1, val_2, val_3, upd_index, value, expected", [
    (3, 6, 9, 1, 12, Node(12)),
])
def test_linked_list_set_value(val_1, val_2, val_3, upd_index, value, expected):
    lnk_list = LinkedList()
    lnk_list.append(val_1).append(val_2).append(val_3)
    result = lnk_list.set_value(upd_index, value)
    assert result
    result: Node = lnk_list.get(upd_index)
    assert result.value == expected.value


@pytest.mark.parametrize("val_1, val_2, val_3, val_4, expected", [
    (10, 20, 30, 40, Node(10)),
    (None, None, None, None, None),
])
def test_linked_list_pop_first(val_1, val_2, val_3, val_4, expected):
    lnk_list = LinkedList()
    if val_1:
        lnk_list.append(val_1).append(val_2).append(val_3).append(val_4)
    result: Node = lnk_list.pop_first()
    if result is not None:
        assert result.value == expected.value
        assert lnk_list.length == 3
    else:
        assert result == expected


@pytest.mark.parametrize("val_1, val_2, val_3, val_4, expected", [
    (10, 20, 30, 40, Node(40)),
    (None, None, None, None, None)
])
def test_linked_list_pop(val_1, val_2, val_3, val_4, expected):
    lnk_list = LinkedList()
    if val_1:
        lnk_list.append(val_1).append(val_2).append(val_3).append(val_4)
        result: Node = lnk_list.pop()
        assert result.value == expected.value
    else:
        result = lnk_list.pop()
        assert result is expected


@pytest.mark.parametrize("val_1, val_2, val_3, val_4, removed, expected", [
    (10, 20, 30, 40, 2, Node(30)),
    (10, 20, 30, 40, 0, Node(10)),
    (10, 20, None, None, 3, None),
    (10, 20, 30, None, -1, Node(30)),
    (10, 30, 30, None, 2, Node(30)),
])
def test_linked_list_remove(val_1, val_2, val_3, val_4, removed, expected):
    lnk_list = LinkedList()
    lnk_list.append(val_1).append(val_2).append(val_3).append(val_4)
    result = lnk_list.remove(removed)
    if expected:
        assert result.value == expected.value
    else:
        assert result == expected


@pytest.mark.parametrize("val_1, val_2, val_3, val_4, expected", [
    (10, 20, 30, 40, 0),
])
def test_linked_list_delete_all(val_1, val_2, val_3, val_4, expected):
    lnk_list = LinkedList()
    lnk_list.append(val_1).append(val_2).append(val_3).append(val_4)
    lnk_list.delete_all()
    assert lnk_list.length == expected
    assert lnk_list.head is None
    assert lnk_list.tail is None


@pytest.mark.parametrize("val_1, val_2, val_3, val_4, index, expected", [
    (10, 20, 30, 40, 0, 10),
    (10, 20, 30, 40, 1, 20),
    (10, 20, 30, 40, 3, 40),
    (10, 20, 30, 40, 4, None),
    (None, None, None, None, 0, None),
    (10, 20, 30, 40, -1, None),
])
def test_linked_list_delete(val_1, val_2, val_3, val_4, index, expected):
    lnk_list = LinkedList()
    if val_1:
        lnk_list.append(val_1).append(val_2).append(val_3).append(val_4)
    result = lnk_list.delete(index)
    if result:
        assert result.value == expected
    else:
        assert result is expected


def test_linked_list_delete_head():
    lnk_list = LinkedList()
    lnk_list.append(10).append(20).append(30).append(40)
    deleted = lnk_list.delete(0)
    assert deleted.value == 10
    assert lnk_list.head.value == 20


@pytest.mark.parametrize("val_1, val_2, val_3, val_4, val_5, expected", [
    (10, 20, 30, 40, None, [40, 30, 20, 10]),
    (10, 20, None, None, None, [20, 10]),
    (1, 2, 3, 4, 5, [5, 4, 3, 2, 1]),
])
def test_linked_list_reverse(val_1, val_2, val_3, val_4, val_5, expected):
    lnk_list = LinkedList()
    lnk_list.append(val_1).append(val_2).append(val_3).append(val_4).append(val_5)
    print(lnk_list)
    for i, num in enumerate(reversed(expected)):
        node = lnk_list.get(i)
        assert node.value == num
    lnk_list.reverse()
    for i, num in enumerate(expected):
        node = lnk_list.get(i)
        assert node.value == num
    print(lnk_list)


@pytest.mark.parametrize("values, expected", [
    ([10, 20, 30, 40], 30),
    ([10, 20, 30, 40, 50], 30),
    ([1, 2, 3, 4, 4, 5, 6, 7, 8, 9], 5),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 5),
    ([1, 2, 3, 4, 5, 6, 7], 4),
])
def test_linked_list_find_middle(values, expected):
    lnk_list = LinkedList()
    for value in values:
        lnk_list.append(value)
    middle: Node = lnk_list.find_middle()
    assert middle.value == expected


@pytest.mark.parametrize("values, expected", [
    ([10, 20, 30, 30, 40], [10, 20, 30, 40]),
    ([10, 10, 20, 30, 30, 40], [10, 20, 30, 40]),
    ([10, 20, 30, 40, 40], [10, 20, 30, 40]),
])
def test_linked_list_remove_duplicates(values, expected):
    lnk_list = LinkedList()
    for value in values:
        lnk_list.append(value)
    lnk_list.remove_duplicates()
    for i in range(lnk_list.length):
        node = lnk_list.get(i)
        assert node.value == expected[i]


@pytest.mark.parametrize("list1, list2, expected", [
    ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
])
def test_linked_list_merge(list1, list2, expected):
    lnk_list1 = LinkedList()
    for value in list1:
        lnk_list1.append(value)
    lnk_list2 = LinkedList()
    for value in list2:
        lnk_list2.append(value)
    result = lnk_list1.merge(lnk_list2)
    assert list(result) == expected


@pytest.mark.parametrize("list1, list2, expected", [
    ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
    ([1, 3, 5, 5], [2, 4, 6, 7], [1, 2, 3, 4, 5, 5, 6, 7]),
])
def test_linked_list_join(list1, list2, expected):
    lnk_list1 = LinkedList()
    for value in list1:
        lnk_list1.append(value)
    lnk_list2 = LinkedList()
    for value in list2:
        lnk_list2.append(value)
    result = LinkedList.join(lnk_list1.head, lnk_list2.head)
    assert list(result) == expected


@pytest.mark.parametrize("list1, expected", [
    ([1, 1, 2], [1, 2]),
    ([1, 1, 2, 3, 3], [1, 2, 3]),
    ([1, 1, 1], [1]),
])
def test_linked_list_remove_duplicates_sorted(list1, expected):
    lnk_list_1 = LinkedList()
    for value in list1:
        lnk_list_1.append(value)
    lnk_list_2 = LinkedList()
    for value in expected:
        lnk_list_2.append(value)
    LinkedList.remove_duplicates_sorted(lnk_list_1.head)
    assert list(lnk_list_1) == list(lnk_list_2)
