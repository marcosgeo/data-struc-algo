"""Implements a stack data structure."""


class BasicStack:
    """Implements a stack data structure using python list."""
    def __init__(self):
        self.list = []

    def __str__(self):
        values = [str(x) for x in reversed(self.list)]
        return "\n".join(values)

    def push(self, item):
        """Add an item to the stack."""
        self.list.append(item)
        return self

    def isempty(self):
        """Check if the stack is empty."""
        return len(self.list) == 0

    def pop(self):
        """Remove and return the last item added to the stack."""
        if self.isempty():
            return None
        return self.list.pop()

    def peek(self):
        """Return the last item added to the stack."""
        if self.isempty():
            return None
        return self.list[-1]

    def clear(self):
        """Remove all items from the stack."""
        self.list.clear()
        return self


class LimitedStack(BasicStack):
    """Implements a stack with a limited size."""
    def __init__(self, max_size):
        self.max_size = max_size
        self.list = []

    def isfull(self):
        """Check if the stack is full."""
        return len(self.list) >= self.max_size

    def push(self, value):
        """Add an item to the stack if it is not full."""
        if self.isfull():
            print("\nStack is full, cannot add item.")
            return self
        self.list.append(value)
        return self


class Node:
    """Implements a node for a linked list."""
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    """Implements a linked list data structure."""
    def __init__(self):
        self.head = None

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next

    def __repr__(self):
        result = ""
        temp_node = self.head
        while temp_node:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += " -> "
            temp_node = temp_node.next if temp_node.next else ""
        return result


class Stack:
    """Implements a stack data structure using a linked list."""
    def __init__(self):
        """Initialize the stack."""""
        self.linked_list = LinkedList()

    def __str__(self):
        """Return a string representation of the stack."""
        values = [str(x.value) for x in self.linked_list]
        return "\n".join(values)

    def isempty(self) -> bool:
        """Check is the stack is empty"""
        return self.linked_list.head is None

    def push(self, value) -> object:
        """Add an item to the stack."""
        node = Node(value)
        node.next = self.linked_list.head
        self.linked_list.head = node
        return self

    def pop(self):
        """Remove and return the last item added to the stack."""
        if not self.linked_list.head:
            return None
        last = self.linked_list.head
        self.linked_list.head = last.next
        return last.value

    def peek(self):
        """Return the value of the last item added to the stack"""
        if not self.linked_list.head:
            return None
        return self.linked_list.head.value

    def clear(self):
        """Remove all items from the stack."""
        if not self.linked_list.head:
            return None
        self.linked_list.head = None
        return True

