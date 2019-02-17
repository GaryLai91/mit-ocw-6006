from avl import AVLNode, AVL

class RangeNode(AVLNode):
	"""Implementation of a RangeNode
	A RangeNode is also a node in an order
	statistics tree
	"""

	def __init__(self, key):
		AVLNode.__init__(self, key)
		self.tree_size = 1

	def update_subtree_info(self):
		AVLNode.update_subtree_info(self)
		self.tree_size = self._uncached_tree_size()

	def _uncached_tree_size(self):
		return 1 + (((self.left and self.left.tree_size) or 0) +
                ((self.right and self.right.tree_size) or 0))



	def list(self, low_key, high_key, result):
		"""
		Returns a list of keys that are inbetween
		low_key and high_key
		"""
		
		if low_key <= self.key and self.key <= high_key:
			result.append(self)
		if self.key >= low_key and self.left is not None:
			self.left.list(low_key, high_key, result)
		if self.key <= high_key and self.right is not None:
			self.right.list(low_key, high_key, result)


	def lca(self, low_key, high_key):
		"""Lowest-common ancestor node of nodes with low_key and high_key.

		If low_key and/or high_key are not in the tree, this returns the LCA of the
		nodes that would be created by inserting the keys in the tree.

		Returns a RangeNode instance, or None if low_key and high_key are not in the
		node's subtree, and there is no key in the tree such that
		low_key < key < high_key.
		"""

		if low_key <= self.key <= high_key:
			return self
		if low_key < self.key:
			return self.left and self.left.lca(low_key, high_key)
		else:
			return self.right and self.right.lca(low_key, high_key)

	def rank(self, key):
		"""
		Return the rank of key
		"""
		if key < self.key:
			if self.left is not None:
				return self.left.rank(key)
			else:
				return 0
		if self.left:
			lrank = 1 + self.left.tree_size
		else:
			lrank = 1
		if key > self.key and self.right is not None:
			return lrank + self.right.rank(key)
		return lrank

class RangeTree(AVL):
	"""Implementation of a RangeTree, also known 
	as order statistics tree
	"""

	def __init__(self, node_class = RangeNode):
		AVL.__init__(self, node_class)

	def rank(self, key):
		"""
		Rank of the given key
		"""
		if self.root is not None:
			return self.root.rank(key)
		return 0

	def lca(self, low_key, high_key):
		"""Lowest common ancestor of given key
		"""
		return self.root and self.root.lca(low_key, high_key)

	def list(self, low_key, high_key):
		"""List all keys that are inbetween 
		low_key and high_key
		"""

		result = []
		lca = self.lca(low_key, high_key)
		if lca is not None:
			lca.list(low_key, high_key, result)
		return result

class AvlRangeIndex(object):
	"""Sorted array-based range index implementation."""

	def __init__(self):
		"""Initially empty range index."""
		self.tree = RangeTree()

	def add(self, key):
		"""Inserts a key in the range index."""
		if key is None:
			raise ValueError('Cannot insert None in the index')
		self.tree.insert(key)

	def remove(self, key):
		"""Removes a key from the range index."""
		self.tree.delete(key)

	def list(self, low_key, high_key):
		"""List of values for the keys that fall within [low_key, high_key]."""
		return [node.key for node in self.tree.list(low_key, high_key)]

	def count(self, low_key, high_key):
		"""Number of keys that fall within [low_key, high_key]."""
		return self.tree.rank(high_key) - self.tree.rank(low_key)