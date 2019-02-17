from bst import BSTNode, BST



class AVLNode(BSTNode):
	"""Implementation of AVL Node"""

	def __init__(self, key):
		BSTNode.__init__(self, key)
		self.height = 0
	
	def update_subtree_info(self):
		self.height = self._uncached_height()

	def _uncached_height(self):
		return 1 + max((self.left and self.left.height) or -1,
						(self.right and self.right.height) or - 1)



class AVL(BST):
	"""Implementation of AVL Tree"""

	def __init__(self, node_class = AVLNode):
		BST.__init__(self, node_class)
	

	def height(self, node):
		"""Return height of subtree rooted at this node
		"""
		if node is None:
			return -1
		return node.height


	def insert(self, key):
		inserted_node = BST.insert(self, key)
		self._rebalance(inserted_node)
		return inserted_node

	def delete(self, key):
		deleted_node = BST.delete(self, key)
		self._rebalance(deleted_node)
		return deleted_node
		

	def _left_rotate(self, node):
		"""Left rotate on this node"""
		temp = node.right
		node.right = temp.left
		if temp.left is not None:
			temp.left.parent = node
		temp.parent = node.parent
		if node.parent is None:
			self.root = temp
		elif node == node.parent.left:
			node.parent.left = temp
		elif node == node.parent.right:
			node.parent.right = temp
		node.parent = temp
		temp.left = node
		node.update_subtree_info()
		temp.update_subtree_info()

	def _right_rotate(self, node):
		"""Right rotate on this node"""
		temp = node.left
		node.left = temp.right
		if temp.right is not None:
			temp.right.parent = node
		temp.parent = node.parent
		if node.parent is None:
			self.root = temp
		elif node == node.parent.right:
			node.parent.right = temp
		elif node == node.parent.left:
			node.parent.left = temp
		node.parent = temp
		temp.right = node
		node.update_subtree_info()
		temp.update_subtree_info()


	def _rebalance(self, node):
		"""Rebalance Tree"""
		while node is not None:
			node.update_subtree_info()
			if self.height(node.left) >= 2 + self.height(node.right):
				if self.height(node.left.left) >= self.height(node.left.right):
					self._right_rotate(node)
				else:
					self._left_rotate(node.left)
					self._right_rotate(node)
			elif self.height(node.right) >= 2 + self.height(node.left):
				if self.height(node.right.right) > self.height(node.right.left):
					self._left_rotate(node)
				else:
					self._right_rotate(node.right)
					self._left_rotate(node)
			node = node.parent