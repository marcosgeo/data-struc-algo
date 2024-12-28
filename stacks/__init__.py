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
