class Parent: 

	parentAttr = 100

	def __init__(self):
		print 'Calling parent constructor'

	def parentMethod(self):
		print 'Calling parent method'

	def setAttr(self, attr):
		Parent.parentAttr = attr

	def getAttr(self):
		print 'Parent attribute :', Parent.parentAttr

	def myMethod(self):
		print 'Calling parent method'


class Child(Parent):
	def __init__(self):
		print 'Calling child constructor'

	def childMethod(self):
		print 'Calling child meethod'


	def myMethod(self):
		print 'Overriding!'


class Vector:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def __str__(self):
		return 'Vector (%d, %d)' % (self.a, self.b)

	def __add__(self,other):
		return Vector(self.a + other.a, self.b + other.b)



if __name__ == '__main__':	
	p = Parent()
	c = Child()
	c.childMethod()
	c.parentMethod()
	c.setAttr(200)
	c.getAttr()
	p.myMethod()
	c.myMethod()
	p.myMethod()

	v1 = Vector(2, 10)
	v2 = Vector(5, -2)
	
	print v1
	print v2
	print v1 + v2
