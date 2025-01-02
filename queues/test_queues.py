import pytest

from . import BasicQueue


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
