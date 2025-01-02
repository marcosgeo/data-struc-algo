
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
