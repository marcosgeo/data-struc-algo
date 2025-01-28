"""
Binary tree using linked list
"""
from typing import Optional
from queues import LinkedListQueue as Queue


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return f"{self.data} -> "


def pre_order_traversal(root_node: TreeNode, result=[]):
    if not root_node:
        return
    print(root_node.data)
    result.append(root_node.data)
    pre_order_traversal(root_node.left_child, result)
    pre_order_traversal(root_node.right_child, result)
    return result


def in_order_traversal(root_node: TreeNode, result=[]):
    if not root_node:
        return
    in_order_traversal(root_node.left_child, result)
    result.append(root_node.data)
    in_order_traversal(root_node.right_child, result)
    return result


def post_order_traversal(root_node: TreeNode, result=[]):
    if not root_node:
        return
    post_order_traversal(root_node.left_child, result)
    post_order_traversal(root_node.right_child, result)
    result.append(root_node.data)
    return result


def level_order_traversal(root_node: TreeNode, result=[]):
    if not root_node:
        return None
    else:
        custom_queue = Queue()
        custom_queue.enqueue(root_node)
        while not custom_queue.isempty():
            node = custom_queue.dequeue()
            result.append(node.data)
            if node.left_child:
                custom_queue.enqueue(node.left_child)
            if node.right_child:
                custom_queue.enqueue(node.right_child)

    return result


def search(root_node: TreeNode, value: str) -> str:
    if not root_node:
        return "Empty tree"
    custom_queue = Queue()
    custom_queue.enqueue(root_node)
    while not custom_queue.isempty():
        node = custom_queue.dequeue()
        if node.data == value:
            return node.data
        if node.left_child:
            custom_queue.enqueue(node.left_child)
        if node.right_child:
            custom_queue.enqueue(node.right_child)
    return "Value not found"


def insert(root_node: TreeNode, value: str) -> Optional[TreeNode]:
    if not root_node:
        return TreeNode(value)
    custom_queue = Queue()
    custom_queue.enqueue(root_node)
    while not custom_queue.isempty():
        node = custom_queue.dequeue()
        if not node.left_child:
            node.left_child = TreeNode(value)
            return node.left_child
        if not node.right_child:
            node.right_child = TreeNode(value)
            return node.right_child
        custom_queue.enqueue(node.left_child)
        custom_queue.enqueue(node.right_child)
    return None
