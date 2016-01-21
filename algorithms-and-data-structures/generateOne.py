#Hill Climbing Optimization
# to check if the randomly generated string appears in our written target string,
# and using the hill climbing optimization method to print only the result completion (shown by the percentage) better than previous result

from __future__ import division
import random

def generateOne(strlen):
	alphabet = 'abcdefghijklmnopqrstuvwxyz ,-'
	alphabetlen = len(alphabet)
	res = ''
	for i in range(strlen):
		res = res + alphabet[random.randrange(alphabetlen)]

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
	goalstring = 'in the country of the blind, the one-eyed man is king'
	goallen = len(goalstring)
	newstring = generateOne(goallen)
	newscore = score(goalstring,newstring)
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
		newstring = generateOne(goallen)
		newscore = score(goalstring,newstring)
		
main()
