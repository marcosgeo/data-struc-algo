import pytest

from . import BasicQueue, CircularQueue, LinkedListQueue


def test_basic_queue_init():
    queue = BasicQueue()
    assert queue.items == []


def test_basic_queue_isempty():
    queue = BasicQueue()
    assert queue.isempty() is True


@pytest.mark.parametrize("items, expected", [
    ([1], [1]),
    ([1, 2], [1, 2]),
    ([1, 2, 3], [1, 2, 3]),
    ([3, 2, 1], [3, 2, 1])
])
def test_basic_queue_enqueue(items, expected):
    queue = BasicQueue()
    for item in items:
        queue.enqueue(item)
    assert queue.items == expected


@pytest.mark.parametrize("items, expected", [
    ([], None),
    ([1], 1),
    ([4, 6], 4),
    ([1, 2, 3], 1)
])
def test_basic_queue_dequeue(items, expected):
    queue = BasicQueue()
    for item in items:
        queue.enqueue(item)
    assert queue.dequeue() == expected


@pytest.mark.parametrize("items, expected", [
    ([], None),
    ([1], 1),
    ([4, 6], 4),
    ([1, 2, 3], 1)
])
def test_basic_queue_peek(items, expected):
    queue = BasicQueue()
    for item in items:
        queue.enqueue(item)
    assert queue.peek() == expected


def test_basic_queue_clear():
    queue = BasicQueue()
    queue.enqueue(1).enqueue(2).enqueue(3)
    assert queue.isempty() is False
    queue.clear()
    assert queue.items == []
    assert queue.isempty() is True


def test_circular_queue_init():
    queue = CircularQueue(3)
    assert queue.items == []
    assert str(queue) == ""


@pytest.mark.parametrize("items, start, end", [
    ([1, 2, 3], 1, 3),
    ([1, 2, 3, 4], 1, 4),
    ([3, 2, 1], 3, 1),
    ([1, 2, 3, 4, 5], 1, 5),
])
def test_circular_queue_enqueue(items, start, end):
    queue = CircularQueue(len(items))
    for item in items:
        queue.enqueue(item)
    assert queue.items[queue.start] == start
    assert queue.items[queue.end] == end


@pytest.mark.parametrize("items, expected, start, end", [
    ([], None, -1, -1),
    ([1, 2, 3], 1, 1, 2),
    ([1, 2, 3, 4, 5, 6], 1, 1, 5),
    ([1], 1, -1, -1),
])
def test_circular_queue_dequeue(items, expected, start, end):
    queue = CircularQueue(len(items))
    for item in items:
        queue.enqueue(item)
    assert queue.dequeue() == expected
    assert queue.start == start
    assert queue.end == end


@pytest.mark.parametrize("items, expected", [
    ([], False),
    ([1, 2, 3], True),
    ([1, 2, 3, 4, 5], True)
])
def test_circular_queue_isfull(items, expected):
    queue = CircularQueue(len(items) + 1)
    for item in items:
        queue.enqueue(item)
    if expected is False:
        assert queue.isfull() == expected
    else:
        assert len(queue.items) == len(items)
        queue.enqueue(10)
        assert queue.isfull() == expected


def test_linkedlist_queue_init():
    queue = LinkedListQueue()
    assert queue.linked_list.head is None
    assert queue.linked_list.tail is None
    assert str(queue) == ""


@pytest.mark.parametrize("items, expected, head, tail", [
    ([3, 2, 1], "3 -> 2 -> 1", 3, 1),
    ([1, 2, 3], "1 -> 2 -> 3", 1, 3),
    ([1, 2, 3, 4, 5], "1 -> 2 -> 3 -> 4 -> 5", 1, 5),
    ([], "", None, None)
])
def test_linkedlist_queue_enqueue(items, expected, head, tail):
    queue = LinkedListQueue()
    for item in items:
        queue.enqueue(item)
    assert str(queue) == expected
    if head and tail:
        assert queue.linked_list.head.value == head
        assert queue.linked_list.tail.value == tail


def test_linkedlist_queue_isempty():
    queue = LinkedListQueue()
    assert queue.isempty() is True


@pytest.mark.parametrize("items, expected", [
    ([3, 2, 1], 3),
    ([1, 2, 3], 1),
    ([1, 2, 3, 4, 5], 1),
    ([], None)
])
def test_linkedlist_queue_dequeue(items, expected):
    queue = LinkedListQueue()
    for item in items:
        queue.enqueue(item)
    value = queue.dequeue()
    assert value == expected


@pytest.mark.parametrize("items, expected", [
    ([3, 2, 1], 3),
    ([1, 2, 3], 1),
])
def test_linkedlist_queue_peek(items, expected):
    queue = LinkedListQueue()
    for item in items:
        queue.enqueue(item)
    assert queue.peek() == expected


def test_linkedlist_queue_clear():
    queue = LinkedListQueue()
    queue.enqueue(1).enqueue(2).enqueue(3)
    assert queue.isempty() is False
    queue.clear()
    assert queue.linked_list.head is None
    assert queue.linked_list.tail is None
    assert queue.isempty() is True
    assert str(queue) == ""
