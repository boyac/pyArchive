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


class Name(object):
	def __init__(self, name):
		self.name = name

	def personalities(self, personalities):
		self.personalities = personalities

	def offers(self, name_com, industry, location):
		self.name_com = name_com
		self.industry = industry
		self.location = location
	
	def relationship(self, relationship):
		self.relationship = relationship

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

		score = sum(map(lambda x, y: x*y, combo[0], combo[1]))
		return score

	def total_score(self):
		



class CounterPart(Name): # 這裡不確定是要這麼寫？？？ 還在找相關的資料

	def __init__(self, name):
		self.name = name

	def offers(self, name_com, industry, location):
		self.name_com = name_com
		self.industry = industry
		self.location = location

	def relationships_score(self, relationships):
		relationships_score = 0 

		self.relationships = relationships

		if self.location == SAME # 我還不知道要怎麼把他練到對照組
			if self.relationships == 'Friends':
				relationships_score =+ 20
			elif self.relationships == 'Dating':
				relationships_score =+ 50
			elif self.relationships_score == 'Mortal Enemies'
				return 'Error'
		else:
			if self.location != 
				if self.relationships == 'Married':
					return 'Error'
				else:
					return 'None'



