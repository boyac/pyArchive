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
['Amy', 'Academic', 'Dartboard Modeling', 'Hedge Fund', 'NYC'],
['Bob', 'Entrepreneur', 'Bigup-Side', 'Startup', 'NYC'],
['Bob', 'Entrepreneur', 'Questionable Tactics', 'Hedge Fund', 'San Francisco'],
['Charlie', 'Money Grubber', 'Cash-Money Inc.', 'Investment Bank', 'NYC'],
['Charlie', 'Money Grubber', 'Arbitrack', 'Hedge Fund', 'San Francisco']
]

import itertools

class Name(object):
	#def __init__(self, name):
	#	self.name = name

	def __init__(self, name, personalities, company, industry, location):
		self.name = name
		self.personalities = personalities
		self.company = company
		self.industry = industry
		self.location = location


	def personalities(self, personalities):
		self.personalities = personalities

	def offers(self):
		
		offers = [] 
		#return offers.append(['%s, %s, %s, %s, %s']) % (self.name, self.personalities, self.company, self.industry, self.location) # fixing this soon
		return 'TEST, Happy 2016!!'

	def relationship(self, relationship):
		self.relationship = relationship


class  OffersPair(Name):
	def pair(self, offer):
		self.offer = offer 

		pairs = []
		for i,j in itertools.combinations(self.offer, 2): #offer 變數來自上一個 def offers 裡面
			if i != j:
				return pair.append((i, j)) #這裡只產生 A(一人為 base 值的的組合與對照組)

class Calculator(Name):
	 def combo_score(self):
		combo = [] 
		if self.personalities == 'Money Grubber':
			combo.append(p0[0])
		elif self.personalities == 'Entrepreneur':
			combo.append(p0[1])
		elif self.personalities == 'Slacker':
			combo.append(p0[2])
		elif self.personalities == 'Academic':
			combo.append(p0[3])
		else:
			return 'Error'

		if self.industry == 'Big Software':
			combo.append(j0[0])
		if self.industry == 'Hedge Fund':
			combo.append(j0[1])
		if self.industry == 'Investment Bank':
			combo.append(j0[2])
		if self.industry == 'Startup':
			combo.append(j0[3])
		if self.industry == 'Grad School':
			combo.append(j0[4])

		combo_score = sum(map(lambda x, y: x*y, combo[0], combo[1]))
		
		return combo_score
		#return self.name, self.personalities, self.name_com, self.industry, self.location




class CounterPart(Name): # 這裡不確定是要這麼開一個新 class 寫？？？ 還在找相關的資料做參考 ＃（http://interactivepython.org/courselib/static/pythonds/index.html）

	def __init__(self, name):
		self.name = name

	def offers(self, name_com, industry, location):
		self.name_com = name_com
		self.industry = industry
		self.location = location

	def relationships_score(self, relationships):
		relationships_score = 0 

		self.relationships = relationships

		for i, j in pairs:
			if i[5] == j[5]: # 這裡表示 location 如果相同；＃我還不知道要怎麼把他練到對照組
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


#TEST
amy = Name('Amy', 'Academic', 'MacroHard', 'Big Software Firm', 'Seattle')
print amy.offers()


