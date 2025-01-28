import pytest


from .binarytree import (
    TreeNode,
    pre_order_traversal,
    in_order_traversal,
    post_order_traversal,
    level_order_traversal,
    search,
    insert,
)


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
    left_left.left_child = TreeNode("left-left-left")  # N 8
    left_left.right_child = TreeNode("left-left-right")  # N 9

    result = in_order_traversal(root)
    # N 8 -> N 4 -> N 9 -> N 2 -> N 5 -> N 1 -> N 6 -> N 3 -> N 7
    assert result == [
        "left-left-left", "left-left", "left-left-right", "left",
        "left-right", "trunk", "right-left", "right", "right-right"
    ]


def test_should_traverse_tree_in_post_order():
    root = TreeNode("trunk")  # N 1
    left = TreeNode("left")  # N 2
    right = TreeNode("right")  # N 3
    root.left_child = left
    root.right_child = right
    left_left = left.left_child = TreeNode("left-left")  # N 4
    left_right = left.right_child = TreeNode("left-right")  # N 5
    right.left_child = TreeNode("right-left")  # N 6
    right.right_child = TreeNode("right-right")  # N 7
    left_left.left_child = TreeNode("left-left-left")  # N 8
    left_left.right_child = TreeNode("left-left-right")  # N 9

    result = post_order_traversal(root)

    # N 8 -> N 9 -> N 4 -> N 5 -> N 2 -> N 6 -> N 7 -> N 3 -> N 1
    assert result == [
        "left-left-left", "left-left-right", "left-left", "left-right", "left",
        "right-left", "right-right", "right", "trunk"
    ]


def test_should_traverse_tree_in_level_order():
    root = TreeNode("trunk")  # N 1
    left = TreeNode("left")  # N 2
    right = TreeNode("right")  # N 3
    root.left_child = left
    root.right_child = right
    left_left = left.left_child = TreeNode("left-left")  # N 4
    left_right = left.right_child = TreeNode("left-right")  # N 5
    right.left_child = TreeNode("right-left")  # N 6
    right.right_child = TreeNode("right-right")  # N 7
    left_left.left_child = TreeNode("left-left-left")  # N 8
    left_left.right_child = TreeNode("left-left-right")  # N 9

    result = level_order_traversal(root)

    # N 1 -> N 2 -> N 3 -> N 4 -> N 5 -> N 6 -> N 7 -> N 8 -> N 9
    assert result == [
        "trunk", "left", "right",
        "left-left", "left-right",
        "right-left", "right-right",
        "left-left-left", "left-left-right"
    ]


@pytest.mark.parametrize("value, expected", [
    ("left-left", "left-left"),
    ("inexistent", "Value not found"),
    ("right", "right"),
    ("right-left-left", "Value not found"),
])
def test_should_search_in_tree(value, expected):
    root = TreeNode("trunk")
    left = TreeNode("left")
    right = TreeNode("right")
    root.left_child = left
    root.right_child = right
    left_left = left.left_child = TreeNode("left-left")
    left.right_child = TreeNode("left-right")

    result = search(root, value)
    assert result == expected


def test_should_insert_new_node():
    root = TreeNode("trunk")  # N 1
    left = TreeNode("left")  # N 2
    right = TreeNode("right")  # N 3
    root.left_child = left
    root.right_child = right
    left_left = left.left_child = TreeNode("left-left")  # N 4
    free_node = left.right_child = TreeNode("left-right")  # N 5
    right.left_child = TreeNode("right-left")  # N 6
    right.right_child = TreeNode("right-right")  # N 7
    left_left.left_child = TreeNode("left-left-left")  # N 8
    left_left.right_child = TreeNode("left-left-right")  # N 9

    assert free_node.left_child is None

    new_node: TreeNode = insert(root, "new-node")  # N 8
    assert free_node.left_child.data == new_node.data
    assert new_node.data == "new-node"
