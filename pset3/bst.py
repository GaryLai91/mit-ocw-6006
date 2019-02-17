class BSTNode(object):
	"""Implementation of a Binary Search Tree Node."""

	def __init__(self, key):
		self.key = key
		self.parent = None
		self.left = None
		self.right = None

	def insert(self, node):
		"""Insert a node into the subtree rooted at this node."""
		if node.key < self.key:
			if self.left is not None:
				return self.left.insert(node)
			else:
				node.parent = self
				self.left = node
				return node
		elif node.key > self.key:
			if self.right is not None:
				return self.right.insert(node)
			else:
				node.parent = self
				self.right = node
				return node
		return self

	def find(self, key):
		"""Finds and return the node with the corresponding key 
		   rooted as this node
		"""
		if key < self.key:
			return self.left and self.left.find(key)
		elif key > self.key:
			return self.right and self.right.find(key)
		return self

	def find_min(self):
		"""Find the node with minimum key rooted at this node"""

		if self.left is None:
			return self
		return self.left.find_min()

	def next_larger(self):
		"""Find the node with the next larger key
		   rooted at this node.
		"""
		if self.right is not None:
			return self.right.find_min()
		current = self
		while current.parent is not None and current is current.parent.right:
			current = current.parent
		return current

	def delete(self):
		"""Delete and return the node deleted"""
		if self.left is None or self.right is None:
			if self is self.parent.left:
				self.parent.left = self.left or self.right
				if self.parent.left is not None:
					self.parent.left.parent = self.parent
			else:
				self.parent.right = self.left or self.right
				if self.parent.right is not None:
					self.parent.right.parent = self.parent
			return self
		else:
			s = self.next_larger()
			deleted_node = s.delete()
			self.key, s.key = s.key, self.key
			return deleted_node

class BST(object):
	""" Implementation of a BST"""

	def __init__(self, node_class = BSTNode):
		self.root = None
		self.node_class = node_class

	def find(self, key):
		"""Search for node with corresponding key and return key"""
		return self.root and self.root.find(key)

	def find_min(self):
		"""Search and return for node with the minimum key"""
		if self.root is None:
			return None
		else:
			return self.root.find_min(key)

	def insert(self, key):
		"""Insert node into BST"""
		node = self.node_class(key)
		if self.root is None:
			self.root = node
			return node
		return self.root.insert(node)

	def delete(self, key):
		"""Delete and return a node"""
		node = self.find(key)
		if node is None:
			return None
		if node is self.root:
			pseudoroot = self.node_class(None)
			self.root.parent = pseudoroot
			pseudoroot.left = self.root
			deleted = self.root.delete()
			self.root = pseudoroot.left
			if self.root is not None:
				self.root.parent = None
			return deleted
		else:
			return node.delete()

	def next_larger(self, key):
		"""Return node with the next larger corresponding key"""
		node = self.find(key)
		return node and node.next_larger()