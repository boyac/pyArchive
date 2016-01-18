from __future__ import division
import random

def generateOne(strlen):
	alphabet = 'abcdefghijklmnopqrstuvwxyz '
	res = ''
	for i in range(strlen):
		res = res + alphabet[random.randrange(27)]

	return res

#print generateOne()

def score(goal,teststring):
	numSame = 0
	for i in range(len(goal)):
		if goal[i] == teststring[i]:
			numSame = numSame + 1
	return numSame / len(goal) 

#print score('methinks it is like a result', generateOne(28))

def main():
	#goalstring = 'methinks it is like a weasel'
	goalstring = 'alexis is pig'
	newstring = generateOne(13)
	newscore = score(goalstring,newstring)
	best = 0
	count = 0
	
	while newscore <= 1:
		if newscore > best:
			print count, best, newscore, newstring
			count = count + 1
			best = newscore
		newstring = generateOne(13)
		newscore = score(goalstring,newstring)
		
main()
