"""
Circular Singly Linked List
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self) -> str:
        if self.head is None:
            return ""
        temp_node = self.head
        result = str(self.head.value)
        while temp_node.next != self.head:
            temp_node = temp_node.next
            result += f" -> {temp_node.value}"
        result += f" -> {self.head.value}"
        return result

    def append(self, value) -> None:
        new_node: Node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1
