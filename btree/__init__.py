
class BinaryTreeNode:

	def __init__(self, value, left = None, right = None):
		self.value = value
		self.left = left
		self.right = right

	def is_leaf(self):
		return self.left is None and self.right is None

	def __iter__(self):
		if self.is_leaf():
			yield self.value
		else:
			children = []
			if self.left is not None:
				for child in self.left:
					children.append(child)
			yield self.value
			if self.right is not None:
				for child in self.right:
					children.append(child)
			yield children

	def to_list(self):
		result = []
		level = 0

		def flatten(value, level):
			if isinstance(value, list):
				for item in value:
					flatten(item, level + 1)
			else:
				if level >= len(result):
					for i in range(len(result), level):
						result.append([])
				result[level - 1].append(value)

		items = [child for child in self]
		flatten(items, 0)
		return result

if __name__ == "__main__":
	print BinaryTreeNode(0, BinaryTreeNode(1, BinaryTreeNode(5), BinaryTreeNode(6, BinaryTreeNode(7))), BinaryTreeNode(2, BinaryTreeNode(3), BinaryTreeNode(4))).to_list()