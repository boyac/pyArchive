#ref: http://www.python-course.eu/object_oriented_programming.php
class Counter(object):
	number = 0

	def __init__(self):
		type(self).number += 1

	def __del__(self):
		type(self).number -=1


class Account(Counter):
	#counter = 0 #can't be a instance variable
	def __init__(self, holder, number, balance, credit_line=1500):
		self.__holder = holder
		self.__number = number
		self.__balance = balance
		self.__credit_line = credit_line
		Counter.__init__(self)

	def deposit(self, amount):
		self.balance = amount

	def withdraw(self, amount):
		if(self.balance - amount < -self.credit_line):
			#coverage insufficient
			return False
		else:
			self.balance -= amount
			return True

	def balance(self):
		return self.balance

	def transfer(self, target, amount):
		if(self.balance - amount < -self.credit_line):
			#coverge insufficient
			return False
		else:
			self.balance -= amount
			target.balance += amount
			return True

	#def __def__(self):
	#	Account.counter -= 1
