
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
        self.children = []
        self.set_level(level)
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

    def set_level(self, value):
        self.level = value
        for child in self.children:
            if child is not None:
                child.set_level(self.level + 1)

    def set_parent(self, value):
        self.parent = value
        if self.parent is not None:
            self.set_level(self.parent.level + 1)
        else:
            self.set_level(0)

    def __iter__(self):
        return chain(*([isingle((self.value, self.level))] + map(ichild, self.children)))

    def __repr__(self):
        return str(map(str, self))



if __name__ == "__main__":
    assert TreeNode(0).is_leaf() == True
    assert TreeNode(0, None, TreeNode(1)).is_leaf() == False
