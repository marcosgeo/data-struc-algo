from typing import Optional


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        if self.next:
            return f"{self.value} -> {self.next.value}"
        return f"{self.value} ->"


class LinkedList:
    _current = None
    _iter = -1

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        result = ""
        temp_node = self.head
        while temp_node:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += " -> "
            temp_node = temp_node.next if temp_node.next else ""
        return result

    def __iter__(self):
        return self

    def __next__(self):
        if not self._current and self._iter < 0:
            self._current = self.head
        if self._current:
            current = self._current
            self._current = current.next
            self._iter += 1
            return current.value
        raise StopIteration

    def append(self, value):
        if value is None:
            print(f"Invalid parameter: {value}")
            return self
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return self
        # Overall time and space complexity: O(n)

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return self
        # Overall time and space complexity: O(n)

    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        elif self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index + 1):  # O(n)
                # advances until reach the required node
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
            self.length += 1
        return self
        # Overall time complexity: O(n)
        # Overall space complexity: O(1)

    def traverse(self):
        current = self.head  # O(1)
        while current is not None:  # O(n)
            print(current.value)
            current = current.next  # O(1)

    def search(self, value):
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1
        # time complexity: O(n)
        # space complexity: O(1)

    def get(self, index):
        if index == -1:
            return self.tail
        if index < -1 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def pop_first(self):
        if self.length == 0:
            return None
        popped_node: Node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1
        return popped_node

    def pop(self) -> Optional[Node]:
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            temp.next = None
        self.length -= 1
        return popped_node

    def remove(self, index: int) -> Optional[Node]:
        if index >= self.length or index < -1:
            return None
        if index == 0:
            return self.pop_first()
        if index == -1 or index == self.length - 1:
            return self.pop()
        prev_node = self.get(index - 1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node

    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0

    def delete(self, index):
        if self.length == 0 or index >= self.length:
            return None
        deleted_node = None
        current_node = None
        previous_node = None
        for i in range(index + 1):
            if not current_node:
                current_node = self.head
            if i == index:
                deleted_node = current_node
                if previous_node:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
                deleted_node.next = None
            else:
                previous_node = current_node
                current_node = current_node.next

            if deleted_node:
                self.length -= 1
                break
        return deleted_node

    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head, self.tail = self.tail, self.head

    def find_middle(self):
        middle_num = self.length // 2
        middle = self.head
        for _ in range(middle_num):
            middle = middle.next
        return middle

    def remove_duplicates(self):
        current = self.head
        for _ in range(self.length):
            next_ = current.next
            if next_ and current.value == next_.value:
                current.next = next_.next
                self.length -= 1
                del next_
            elif not next_:
                break
            else:
                current = current.next

    def merge(self, other):
        l1_current = self.head
        l1_previous = None
        l2_current = other.head
        if self.head.value > other.head.value:
            self.head = other
        for _ in range(self.length + 1):
            if l1_current and l1_current.value > l2_current.value:
                l1_next = l1_current.next
                l2_next = l2_current.next
                l1_previous.next = Node(l2_current.value)
                if l1_current.value <= l2_next.value:
                    l1_previous.next.next = l1_current
                else:
                    l1_previous.next.next = l2_next
                l1_previous = l1_current
                l2_current = l2_next
                l1_current = l1_next
            elif not l1_current and l2_current:
                l1_previous.next = l2_current
            else:
                l1_previous = l1_current
                l1_current = l1_current.next
        return self

    @staticmethod
    def join(n1: Node, n2: Node) -> object:
        joined = LinkedList().append(Node(0))
        current = joined.head
        while n1 and n2:
            if n1.value <= n2.value:
                current.next = n1
                n1 = n1.next
            else:
                current.next = n2
                n2 = n2.next
            current = current.next
        current.next = n1 if n1 else n2
        joined.delete(0)
        return joined

    @staticmethod
    def remove_duplicates_sorted(head):
        current = head
        while current is not None and current.next is not None:
            if current.value == current.next.value:
                current.next = current.next.next
            else:
                current = current.next
        return head

    @staticmethod
    def remove_value(head: Node, value: int) -> list:
        current: Node = head
        previous: Node = Node(None)
        while current:
            if current.value == value:
                if not previous.value:
                    head = current.next
                else:
                    previous.next = current.next
            else:
                previous = current
            current = current.next
        result = []
        while head:
            result.append(head.value)
            head = head.next
        return result

    @staticmethod
    def reverse_list(lnk_list: "LinkedList"):
        current = lnk_list.head
        previous = None
        while current:
            _next = current.next
            current.next = previous
            previous = current
            current = _next
            lnk_list.head = previous

        return lnk_list

    def is_palindrome(self, head: Node) -> bool:
        if self.length > 105 or self.length < 1:
            return False
        list_items = list(self)
        items = len(list_items) // 2
        for i, value in enumerate(list_items[:items]):
            if value != list_items[-(i+1)]:
                return False
        return True

    def is_palindrome_sln(self, head: None):
        """Commented course solution for palindrome linked list"""
        # pointers to traverse the linked list
        slow = fast = head

        # the fast pointer moves twice as fast as the slow pointer
        # so, by the time fast reaches the end, slow will be at the middle of the linked list
        while fast and fast.next:
            slow = slow.next  # move slow one step forward
            fast = fast.next.next  # move fast two steps forward

        # starting to reverse the sencond half of the linked list
        prev = None
        while slow:
            _next = slow.next  # save the next node
            slow.next = prev  # reverse the slow node pointing next to previous node
            prev = slow  # move prev one step forward
            slow = _next  # move slow one step forward

        # compare the first half and the second half
        tail = prev  # only for clarification
        while tail:
            if head.value != tail.value:
                return False
            head = head.next  # move to the right
            tail = tail.next  # move to the left
        return True


if __name__ == "__main__":
    print("\n-- new linked list")
    new_linked_list = LinkedList().append(10)
    print(new_linked_list)  # output 10
    print(new_linked_list.head)  # output <__main__.node object at 0x73c....>
    print(new_linked_list.head.value)  # output 10
