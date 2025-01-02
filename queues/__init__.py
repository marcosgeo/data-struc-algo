
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


class CircularQueue:
    """
    A circular queue implementation using list.
    """
    def __init__(self, max_size: int):
        self.max_size = max_size
        self.items = []
        self.start = -1
        self.end = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return " ".join(values)

    def enqueue(self, item) -> object:
        if len(self.items) == self.max_size:
            return None
        self.items.append(item)
        if self.start == -1:
            self.start = 0
        if self.end + 1 == self.max_size:
            self.end = 0
        else:
            self.end += 1
        return self

    def dequeue(self) -> object:
        if self.start == -1:
            return None
        item = self.items[self.start]
        self.start = (self.start + 1) % self.max_size  # 2 % 5 = 2; 5 % 5 = 0
        if self.start == self.end:
            self.start = -1
            self.end = -1
        return item
