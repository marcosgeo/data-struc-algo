
import pytest

from . import BasicStack


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
