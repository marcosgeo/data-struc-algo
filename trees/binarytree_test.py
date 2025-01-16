from .binarytree import TreeNode, pre_order_traversal


def test_should_create_root_node():
    root = TreeNode("trunk")
    assert root.data == "trunk"
    assert root.left_child is None
    assert root.right_child is None


def test_should_traverse_tree_in_pre_order():
    root = TreeNode("\ntrunk")
    left = TreeNode("left")
    right = TreeNode("right")
    root.left_child = left
    root.right_child = right
    left.left_child = TreeNode("left-left")
    left.right_child = TreeNode("left-right")
    right.left_child = TreeNode("right-left")
    right.right_child = TreeNode("right-right")
    result = pre_order_traversal(root)
    assert result == ["\ntrunk", "left", "left-left", "left-right", "right", "right-left", "right-right"]

