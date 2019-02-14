class BSTNode(object):
	"""Implementation of a Binary Search Tree Node."""

	def __init__(self, key):
		self.key = key
		self.parent = None
		self.left = None
		self.right = None

	def insert(self, node):
		if node.key < self.key:
			if self.left is not None:
				self.left.insert(node)
			else:
				self.left = node
				node.parent = self
			return node
		elif node.key > self.key:
			if self.right is not None:
				self.right.insert(node)
			else:
				self.right = node
				node.parent = self
			return node
		return self

	def find(self, key):
		if key < self.key:
			return self.left and self.left.find(key)
		elif key > self.key:
			return self.right and self.right.find(key)
		return self

	def find_min(self):
		if self.left is None:
			return self
		return self.left.find_min()

	def next_larger(self):
		if self.right is not None:
			return self.find_min()
		current = self.parent
		while current is not None and self == current.right:
			self = current
			current = current.parent
		return current

	def delete(self):
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
			self.key, s.key = s.key, self.key
			s.delete()

class BST(object):
	def __init__(self, node_class = BSTNode):
		self.root = None
		self.node_class = node_class

	def find(self, key):
		if self.root is None:
			return None
		else:
			return self.root.find(key)

	def find_min(self):
		if self.root is None:
			return None
		else:
			return self.find_min(key)

	def insert(self, key):
		node = self.node_class(key)
		if self.root is None:
			self.root = node
			return node
		return self.root.insert(node)

	def delete(self, key):
		pass

	def next_larger(self, key):
		pass