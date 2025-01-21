from .binarytree import TreeNode, pre_order_traversal, in_order_traversal


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


def test_should_traverse_tree_in_order():
    root = TreeNode("trunk")  # N 1
    left = TreeNode("left")  # N 2
    right = TreeNode("right")  # N 3
    root.left_child = left
    root.right_child = right
    left_left = left.left_child = TreeNode("left-left")  # N 4
    left_right = left.right_child = TreeNode("left-right")  # N 5
    right.left_child = TreeNode("right-left")  # N 6
    right.right_child = TreeNode("right-right")  # N 7
    left_left.left_child = TreeNode("left-left-left")  # N 9
    left_left.right_child = TreeNode("left-left-right")  # N 10

    result = in_order_traversal(root)
    # N 9 -> N 4 -> N 10 -> N 2 -> N 5 -> N 1 -> N 6 -> N 3 -> N 7
    assert result == [
        "left-left-left", "left-left", "left-left-right", "left",
        "left-right", "trunk", "right-left", "right", "right-right"
    ]

