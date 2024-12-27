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
