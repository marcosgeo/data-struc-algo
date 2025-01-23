"""
Binary tree using linked list
"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


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
