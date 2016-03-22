# -*- coding: utf-8 -*-
import numpy as np, numpy.random
class Lucky:
	def __init__(self, amount, n):
		self.amount = amount
		self.n = n

	def money(self):
	    self.hong_bao = np.random.dirichlet(np.ones(self.n),size=1) * self.amount
	    np.set_printoptions(precision=2)
	    self.hong_bao = np.round(self.hong_bao, decimals=2).flatten()
	    return self.hong_bao.tolist()
	    #return reduce(lambda x, y: x+y, self.hong_bao) #works the same as flatten()
	
	def env(self):
		for index, element in enumerate(self.hong_bao.tolist()):
			print 'No.{}, {} 元'.format(index+1, element)
		

def main():
	test = Lucky(10,3)
	print test.money()
	print test.env()

if __name__== "__main__":
	main()
