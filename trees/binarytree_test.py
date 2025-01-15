from .binarytree import TreeNode


def test_should_create_root_node():
    root = TreeNode("trunk")
    assert root.data == "trunk"
    assert root.left_child is None
    assert root.right_child is None
