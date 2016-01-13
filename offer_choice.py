p0 = [[10, -1, 4, 2], [4, -2, 10, 8], [1, -10, 2, 2], [2, -6, 8, 10]]
j0 = [[6, 6, 2, 8], [8, 8, 4, 6], [10, 10, 3, 4], [4, 8, 10, 8], [1, 4, 3, 10]]

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


	def score(self):
		score = 0
		if self.personalities == 'Money Grubber':
			return p0[0]
		elif self.personalities == 'Entrepreneur':
			return p0[1]
		elif self.personalities == 'Slacker':
			return p0[2]
		elif self.personalities == 'Academic':
			return p0[3]
		else:
			return 'Maybe Typo'

		if self.industry == ''	

class CounterPart(object):
	def __init__(self, name):
		self.name = name

	def offers(self, name_com, industry, location):
		self.name_com = name_com
		self.industry = industry
		self.location = location
