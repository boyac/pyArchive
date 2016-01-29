# -*- coding: utf-8 -*-
p0 = [[10, -1, 4, 2], [4, -2, 10, 8], [1, -10, 2, 2], [2, -6, 8, 10]]
j0 = [[6, 6, 2, 8], [8, 8, 4, 6], [10, 10, 3, 4], [4, 8, 10, 8], [1, 4, 3, 10]]

#def offers(pay, hours, impact, edu):

#money_grubber = [10, -1, 4, 2] = p0[0]
#entrepreneur = [4, -2, 10, 8] = p0[1]
#slacker = [1, -10, 2, 2] = p0[2]
#academic = [2, -6, 8, 10] = p0[3]
	
#software = [6, 6, 2, 8] = j0[0]
#hedge_fund = [8, 8, 4, 6] = j0[1]
#investment_bank = [10, 10, 3, 4] = j0[2]
#startup = [4, 8, 10, 8] = j0[3]
#grad_school = [1, 4, 3, 10] = j0[4]

people = [
['Amy', 'Academic'],
['Bob', 'Entrepreneur'], 
['Charlie', 'Money Grubber']
]

offers = [
['Amy', 'Academic', 'MacroHard', 'Big Software Firm', 'Seattle'],
['Amy', 'Academic', 'Stanguard College', 'Grad School', 'San Francisco'],
['Amy', 'Academic', 'Dartboard Modeling', 'Hedg Fund', 'NYC'],
['Bob', 'Entrepreneur', 'Bigup-Side', 'Startup', 'NYC'],
['Bob', 'Entrepreneur', 'Questionable Tactics', 'Hedge Fund', 'San Francisco'],
['Charlie', 'Money Grubber', 'Cash-Money Inc.', 'Investment Bank', 'NYC'],
['Charlie', 'Money Grubber', 'Arbitrack', 'Hedge Fund', 'San Francisco']
]
 
relationships= [
['Bob', 'Amy', 'Dating'],
['Bob', 'Charlie', 'Mortal Enemies']
]


import itertools
import numpy
class Name(object):

	def __init__(self, name, personalities, company, industry, location):
		self.name = name
		self.personalities = personalities
		self.company = company
		self.industry = industry
		self.location = location


	def combo_score(self, combo_score=[], combo_total=[]):

		self.combo_total = combo_total
		self.combo_score = combo_score

		if self.personalities == 'Money Grubber':
			self.combo_score.append(p0[0])
		elif self.personalities == 'Entrepreneur':
			self.combo_score.append(p0[1])
		elif self.personalities == 'Slacker':
			self.combo_score.append(p0[2])
		elif self.personalities == 'Academic':
			sfelf.combo_score.append(p0[3])
		else:
			return 'Error'

		if self.industry == 'Big Software Firm':
			self.combo_score.append(j0[0])
		elif self.industry == 'Hedge Fund':
			self.combo_score.append(j0[1])
		elif self.industry == 'Investment Bank':
			self.combo_score.append(j0[2])
		elif self.industry == 'Startup':
			self.combo_score.append(j0[3])
		elif self.industry == 'Grad School':
			self.combo_score.append(j0[4])
		else:
			return 'Error'

		self.combo_total = sum(map(lambda x, y: x*y, self.combo_score[0], self.combo_score[1]))
		return self.combo_total
	

	
	def offers(self, offers=[], offers_a=[], offers_b=[]):
		self.offers = offers
		
		self.offers.extend([self.name, self.personalities, self.company, self.industry, self.location, self.location]) 
		
		return self.offers
		

	def offers_c(self, offers_c=[]): #counterpart's offer
 		self.offers_c = offers_c
		self.offers_c.extend([self.name, self.personalities, self.company, self.industry, self.location, self.location]) 
		return self.offers_c
		

	def pairs(self, pairs=[]): #paring the offers of counterpart's
		self.pairs = pairs

		for i in itertools.product(self.offers(), self.offers_c()):
			if i[0] != i[1]:
				self.pairs.append(i)
	
		return self.pairs


	def status(self, connection=[], status=[]): # aftering the pairing, see the relationships of each Name pair
		self.connection = connection
		self.status = status
		for x in relationships: # make combinations of relationship and check if pairs(index name) are defined in the relationships list
		    self.connection.append(([x[0],x[1],x[2]]))
		    self.connection.append(([x[1],x[0],x[2]]))


		for i, j in self.pairs:
		    if set([i[0],j[0]]) in self.connection: # 這裡應該寫錯了
		        #return i[0],j[0],x[2]
		        self.status.append(i[0])
		        return self.status
		    

	def relationships(self, name, name2, relationships):
		self.name = name
		self.name2 = name2
		self.relationships = relationships

		relationships_score = 0 

		for i, j in self.pairs:
			if i[5] == j[5]: # 這裡表示 location 如果相同
				if self.relationships == 'Friends':
					relationships_score =+ 20
				elif self.relationships == 'Dating':
					relationships_score =+ 50
				elif self.relationships == 'Mortal Enemies':
					return 'Error'
				else:
					return 'None'
			else:
				if self.relationships == 'Married':
					return 'Error'
				else:
					return 'None'


	
# TEST 
amy = Name(['Amy', 'Academic', 'MacroHard', 'Big Software Firm', 'Seattle'],
['Amy', 'Academic', 'Stanguard College', 'Grad School', 'San Francisco'],
['Amy', 'Academic', 'Dartboard Modeling', 'Hedg Fund', 'NYC'],
['Bob', 'Entrepreneur', 'Bigup-Side', 'Startup', 'NYC'],
['Bob', 'Entrepreneur', 'Questionable Tactics', 'Hedge Fund', 'San Francisco']
)

bob = Name(['Amy', 'Academic', 'MacroHard', 'Big Software Firm', 'Seattle'],
['Amy', 'Academic', 'Stanguard College', 'Grad School', 'San Francisco'],
['Amy', 'Academic', 'Dartboard Modeling', 'Hedg Fund', 'NYC'],
['Bob', 'Entrepreneur', 'Bigup-Side', 'Startup', 'NYC'],
['Bob', 'Entrepreneur', 'Questionable Tactics', 'Hedge Fund', 'San Francisco']
)

print bob.pairs()
print bob.status()


# ref: http://interactivepython.org/runestone/static/pythonds/index.html
