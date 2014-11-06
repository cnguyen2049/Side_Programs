class Node:
	def __init__(self,cargo=None,next=None):
		self.cargo = cargo
		self.next = next
	def __str__(self):
		return str(self.cargo)

def printList(node):
	while node:
		print node,
		node = node.next

def printBackward(list):
	if list == None: return
	head = list
	tail = list.next
	printBackward(tail)
	print head,

def shortRecursion(list):
	if list == None:return
	shortRecursion(list.next)
	print list,
node = Node("Start")
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node.next = node1
node1.next = node2
node2.next = node3

printList(node)
print
printBackward(node)
print
shortRecursion(node)
