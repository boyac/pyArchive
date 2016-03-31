# How many searches do you need to find an element between 0 and 1000?
__author__ = 'Boya Chiou'
from __future__ import division
import random

def generateTwo(strlen):
	digit = str(range(0, 1001))
	digitlen = len(digit)
	res = ''
	
	for i in range(strlen):
		res = res + digit[random.randrange(digitlen)]
	return res

def score(goal,teststring):
	numSame = 0
	for i in range(len(goal)):
		if goal[i] == teststring[i]:
			numSame = numSame + 1
	return numSame / len(goal) 

def main():	
	goalnum = '1000'
	goallen = len(goalnum)
	newstring = generateTwo(goallen)
	newscore = score(goalnum, newstring)
	best = 0
	count = 0

	while newscore <= 1:
		count += 1
		if newscore > best:
			print count, best, newscore, newstring
			#count = count + 1
			best = newscore
		if newscore == 1: 
			print count, newstring, 'DONE!'
			exit()
		newstring = generateTwo(goallen)
		newscore = score(goalnum,newstring)
		
main()
