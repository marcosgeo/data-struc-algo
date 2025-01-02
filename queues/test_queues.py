import pytest

from . import BasicQueue


def test_basic_queue_init():
    queue = BasicQueue()
    assert queue.items == []


def test_basic_queue_isempty():
    queue = BasicQueue()
    assert queue.isempty() is True
