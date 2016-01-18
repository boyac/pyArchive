import random

def generateOne(strlen):
	alphabet = 'abcdefghijklmnopqrstuvwxyz '
	res = ''
	for i in range(strlen):
		res = res + alphabet[random.randrange(27)]

	return res

#print generateOne()

def score(goal, teststring):
	
