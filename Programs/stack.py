class Stack :
	def __init__(self):
		self.objs =[]
	def push(self,obj):
		self.objs.append(obj)
	def pop(self):
		return (self.objs.pop())
	def isEmpty(self):
		return self.objs == []

std = Stack()
std.push("AIDS")
std.push("Herp")

while not std.isEmpty():
	print std.pop(),

