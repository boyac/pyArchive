class Employee:
	empCount = 0 # empCount is a class variable whose value is shared among all instances of a this class. This can be accessed as Employee.empCount from inside the class or outside the class.

	def __init__(self, name, salary, age):
		self.name = name
		self.salary = salary
		self.age = age
		Employee.empCount += 1

	def displayCount(self): # attribute
		print 'Total Employee %d' % Employee.empCount

	def displayEmployee(self):
		print 'Name : ', self.name, ', Salary:', self.salary, ', Age:', self.age



# creating instance objects
emp1 = Employee('Zara', 2000, 30)
emp2 = Employee('Manni', 5000, 30)

emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount


# access attribute using spectial functions

print hasattr(emp1, 'age')
print getattr(emp1, 'age')
setattr(emp1, 'age', 18)
emp1.displayEmployee()
delattr(emp1, 'age')
setattr(emp1, 'age', 18)
emp1.displayEmployee()


print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__