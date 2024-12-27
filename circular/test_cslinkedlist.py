import pytest

from circular.cslinkedlist import CSLinkedList


@pytest.mark.parametrize("value, head, tail, next_", [
    (1, 1, 1, 1),
    (2, 2, 2, 2,),
])
def test_cslinkedlist_init(value, head, tail, next_):
    csll = CSLinkedList(value)
    assert csll.head.value == head
    assert csll.tail.value == tail
    assert csll.head.next.value == next_

