class Stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return len(self.items) == 0
	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items) - 1]

	def size(self):
		return len(self.items)

s = Stack()
s.push(5)
s.pop()
for i in range(100):
	s.push(i)
print s.size()
print s.peek() #return the top element of the stack
