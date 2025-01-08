import pytest

from .list_tree import TreeNode


@pytest.mark.parametrize("nodes, expected", [
    (["drinks", "cold", "hot"], "drinks\n cold\n hot\n"),
])
def test_tree_node(nodes, expected):
    root = TreeNode(nodes[0])
    for node in nodes[1:]:
        root.children.append(TreeNode(node))
    print()
    print(root)
    assert str(root) == expected


def test_tree_node_two_levels():
    root = TreeNode("Drinks")
    hot = TreeNode("Hot")
    cold = TreeNode("Cold")
    root.add_child(hot)
    root.add_child(cold)
    tea = TreeNode("Tea")
    coffee = TreeNode("Coffee")
    cola = TreeNode("Cola")
    fanta = TreeNode("Fanta")
    hot.add_child(tea)
    hot.add_child(coffee)
    cold.add_child(cola)
    cold.add_child(fanta)
    print()
    print(root)
    assert str(root) == "Drinks\n Hot\n  Tea\n  Coffee\n Cold\n  Cola\n  Fanta\n"
