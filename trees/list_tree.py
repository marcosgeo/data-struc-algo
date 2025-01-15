"""
Tree using python list
"""


class TreeNode:
    def __init__(self, data, children=[]):
        self.data = data
        self.children = children

    def __str__(self, level=0):
        result = " " * level + str(self.data) + "\n"
        for child in self.children:
            result += child.__str__(level + 1)
        return result

    def add_child(self, node):
        self.children.append(node)
        return self
