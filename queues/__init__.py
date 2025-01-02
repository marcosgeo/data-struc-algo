
class BasicQueue:
    """
    A basic queue implementation using list.
    """
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return " ".join(values)

    def isempty(self) -> bool:
        return self.items == []

    def enqueue(self, item) -> object:
        if not item:
            return None
        self.items.append(item)  # O(n) complexity, since added to the end
        return self

    def dequeue(self):
        if self.isempty():
            return None
        return self.items.pop(0)  # O(n) complexity, couse shift all elements to the left

    def peek(self):
        if self.isempty():
            return None
        return self.items[0]

    def clear(self):
        self.items = []
        return self
