from btree import BinaryTreeNode

def main():
	print BinaryTreeNode(0, BinaryTreeNode(1, None, BinaryTreeNode(2)), BinaryTreeNode(3, BinaryTreeNode(4), BinaryTreeNode(5, BinaryTreeNode(6)))).to_list()
	print BinaryTreeNode(0, BinaryTreeNode(1, BinaryTreeNode(5), BinaryTreeNode(6, BinaryTreeNode(7))), BinaryTreeNode(2, BinaryTreeNode(3), BinaryTreeNode(4))).to_list()

if __name__ == "__main__":
	main()