
import pytest

from . import BasicStack


def test_stack_init():
    stack = BasicStack()
    assert stack.list == []
