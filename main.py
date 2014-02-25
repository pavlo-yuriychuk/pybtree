from btree import TreeNode

def main():
	print TreeNode(0, TreeNode(1, None, TreeNode(2)), TreeNode(3, TreeNode(4), TreeNode(5, TreeNode(6)))).to_list()
	print TreeNode(0, TreeNode(1, TreeNode(5), TreeNode(6, TreeNode(7))), TreeNode(2, TreeNode(3), TreeNode(4))).to_list()

if __name__ == "__main__":
	main()