class Node(object):
	"""docstring for Node"""
	def __init__(self):
		self.data = None	# The data of the node.
		self.next = None	# The reference to the next node.

class linked_list(object):
	"""docstring for linked_list"""
	def __init__(self):
		self.cur_node = None

	def AddNode(self, data):
		new_node = Node()	# Create a new node.
		new_node.data = data
		new_node.next = self.cur_node	# Point to the last node.
		self.cur_node = new_node	# Change the current node.

	def PrintNode(self):	# Browse the linked list.
		while self.cur_node:
			print(self.cur_node.data)
			self.cur_node = self.cur_node.next

ll = linked_list()
ll.AddNode(1)
ll.AddNode(2)
ll.AddNode(3)
ll.PrintNode()

		