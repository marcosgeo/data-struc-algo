
import pytest

from . import BasicStack, LimitedStack, Stack


def test_stack_init():
    stack = BasicStack()
    assert stack.list == []


@pytest.mark.parametrize("items, expected", [
    ([1], [1]),
    ([1, 2], [1, 2]),
    ([1, 2, 3], [1, 2, 3]),
])
def test_stack_push(items, expected):
    stack = BasicStack()
    for item in items:
        stack.push(item)
    assert stack.list == expected


def test_stack_str():
    stack = BasicStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print()
    print(stack)
    assert str(stack) == "3\n2\n1"


@pytest.mark.parametrize("items, expected", [
    ([], True),
    ([1], False),
    ([1, 2], False),
])
def test_stack_isempty(items, expected):
    stack = BasicStack()
    for item in items:
        stack.push(item)
    assert stack.isempty() == expected


@pytest.mark.parametrize("items, expected", [
    ([], None),
    ([1], 1),
    ([1, 2], 2),
    ([1, 2, 3], 3),
])
def test_stack_pop(items, expected):
    stack = BasicStack()
    for item in items:
        stack.push(item)
    assert stack.pop() == expected


@pytest.mark.parametrize("items, expected", [
    ([], None),
    ([1], 1),
    ([1, 2], 2),
    ([1, 2, 3], 3),
])
def test_stack_peek(items, expected):
    stack = BasicStack()
    for item in items:
        stack.push(item)
    assert stack.peek() == expected


def test_stack_clear():
    stack = BasicStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.isempty() is False

    stack.clear()
    assert stack.list == []
    assert stack.isempty() is True
    assert stack.peek() is None
    assert stack.pop() is None
    assert str(stack) == ""


@pytest.mark.parametrize("max_size, items, expected", [
    (3, [1, 2, 3], True),
    (4, [1, 2, 3, 4], True),
    (3, [1, 2], False),
    (3, [3, 4, 5], True),
])
def test_limited_stack_init(max_size, items, expected):
    stack = LimitedStack(max_size)
    for item in items:
        stack.push(item)
    assert stack.isfull() == expected
    assert len(stack.list) <= max_size


@pytest.mark.parametrize("max_size, items, expected", [
    (3, [1, 2, 3], [1, 2, 3]),
    (3, [1, 2, 3, 4], [1, 2, 3]),
    (5, [1, 2], [1, 2]),
    (4, [3, 4, 5], [3, 4, 5]),
])
def test_limited_stack_push(max_size, items, expected):
    stack = LimitedStack(max_size)
    for item in items:
        stack.push(item)
    assert stack.list == expected


@pytest.mark.parametrize("max_size, items, expected", [
    (3, [1, 2, 3], [1, 2]),
    (3, [1, 2, 3, 4], [1, 2]),
    (5, [1, 2], [1]),
    (4, [3, 4, 5], [3, 4]),
])
def test_limited_stack_pop(max_size, items, expected):
    stack = LimitedStack(max_size)
    for item in items:
        stack.push(item)
    stack.pop()
    assert stack.list == expected


def test_stack_constructor():
    stack = Stack()
    assert stack.linked_list.head is None


@pytest.mark.parametrize("items, expected", [
    ([1, 2, 3], "3\n2\n1"),
    ([], ""),
    ([1], "1"),
    ([1, 2], "2\n1"),
    ([1, 2, 3, 4], "4\n3\n2\n1"),
])
def test_linked_stack_push(items, expected):
    stack = Stack()
    for item in items:
        stack.push(item)
    assert str(stack) == expected


@pytest.mark.parametrize("items, expected", [
    ([1, 2, 3], 3),
    ([], None),
    ([1], 1),
    ([2, 1], 1),
    ([1, 2, 3, 4], 4),
])
def test_linked_stack_pop(items, expected):
    stack = Stack()
    for item in items:
        stack.push(item)
    assert stack.pop() == expected


@pytest.mark.parametrize("items, expected", [
    ([1, 2, 3], 3),
    ([4, 3, 2], 2),
    ([1], 1),
    ([], None),
    ([1, 2, 3, 4], 4),
])
def test_linked_stack_peek(items, expected):
    stack = Stack()
    for item in items:
        stack.push(item)
    assert stack.peek() == expected


@pytest.mark.parametrize("items, expected", [
    ([1, 2, 3], True),
    ([], None),
])
def test_linked_stack_clear(items, expected):
    stack = Stack()
    for item in items:
        stack.push(item)
    result = stack.clear()
    assert result == expected
    assert stack.linked_list.head is None
