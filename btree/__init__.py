
from itertools import imap, chain, starmap

def isingle(item):
    yield item

def ichild(item):
    if item is None:
        return [item]
    else:
        return iter(item)

class TreeNode:

    def __init__(self, value, left = None, right = None, level = 0):
        self.value = value
        self.parent = None
        self.level = level
        self.children = []
        self.add_child(left)
        self.add_child(right)

    def add_child(self, node):
        if node is not None:
            node.set_parent(self)
        self.children.append(node)

    def is_leaf(self):
        return len(self.children) == 0

    def is_root(self):
        return self.parent is None

    def set_parent(self, value):
        self.parent = value
        self.level = self.parent.level + 1

    def __iter__(self):
        return chain(*([isingle((self.value, self.level))] + map(ichild, self.children)))

    def __repr__(self):
        return str(map(str, self))



if __name__ == "__main__":
    assert TreeNode(0, TreeNode(1, None, TreeNode(2)), TreeNode(3, TreeNode(4), TreeNode(5, TreeNode(6)))).to_list() == [[0], [1, 3], [2, 4, 5], [6]]
    assert TreeNode(0, TreeNode(1, TreeNode(5), TreeNode(6, TreeNode(7))), TreeNode(2, TreeNode(3), TreeNode(4))).to_list() == [[0], [1, 2], [5, 6, 3, 4], [7]]
    assert TreeNode(0, TreeNode(1), TreeNode(2)).to_list() == [[0], [1, 2]]
    assert TreeNode(0).to_list() == [[0]]
    assert TreeNode(0).is_leaf() == True
    assert TreeNode(0, None, TreeNode(1)).is_leaf() == False
