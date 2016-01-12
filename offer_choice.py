"""
input_1 = people (name | personalities)
input_2 = offers (company_name | type | locations)
input_3 = relationships (name | relationships)
"""
"""
def personalities(person):
	if person == 'money_grubber':
		return [10, -1, 4, 2]
	elif person == 'entrepreneur':
		return [4, -2, 10, 8]
	elif person == 'slacker':
		return [1, -10, 2, 2]
	elif person == 'academic':
		return [2, -6, 8, 10]
	else:
		return 'S/he is not a human...Happy 2016!'

def offers(job):
	if job == 'software':
		return [6, 6, 2, 8]
	elif job == 'hedge_fund':
		return [8, 8, 4, 6]
	elif job == 'investment_bank':
		return [10, 10, 3, 4]
	elif job == 'startup':
		return [4, 8, 10, 8]
	elif job == 'grad_school':
		return [1, 4, 3, 10]
"""


def personalities(pay, hours, impact, edu):
	money_grubber = [10, -1, 4, 2]
	entrepreneur = [4, -2, 10, 8]
	slacker = [1, -10, 2, 2]
	academic = [2, -6, 8, 10]
		#personalities = [[10, -1, 4, 2], [4, -2, 10, 8], [1, -10, 2, 2], [2, -6, 8, 10]]
	#personalities = [10, -1, 4, 2]

def offers(pay, hours, impact, edu):
	software = [6, 6, 2, 8]
	hedge_fund = [8, 8, 4, 6]
	investment_bank = [10, 10, 3, 4]
	startup = [4, 8, 10, 8]
	grad_school = [1, 4, 3, 10]
	#jobs = [[6, 6, 2, 8], [8, 8, 4, 6], [10, 10, 3, 4], [4, 8, 10, 8], [1, 4, 3, 10]]
	#jobs = [6, 6 , 2, 8]

class choice(object):
	def __init__(self, people, offers, relationships):
		self.people = people
		self.offers = offers 
		self.relationships = relationships



import itertools
# Data_input
p0 = [[10, -1, 4, 2], [4, -2, 10, 8], [1, -10, 2, 2], [2, -6, 8, 10]]
j0 = [[6, 6, 2, 8], [8, 8, 4, 6], [10, 10, 3, 4], [4, 8, 10, 8], [1, 4, 3, 10]]

utility_combi = []
utility_score = []

for combi in itertools.product(p0, j0):
    utility_combi.append(map(lambda x, y: x*y, combi[0], combi[1]))
for item in utility_combi:
	utility_score.append(reduce(lambda x, y: x+y, item))
#print utility_combi
#print utility_score


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


relationships_new = [
[('Bob', 'Amy'), 'Dating'],
[('Bob', 'Charlie'), 'Mortal Enemies'],
[('Amy', 'Bob'), 'Dating'],
[('Charlie', 'Bob'), 'Mortal Enemies']
]

# name: people[0], person: people[1]
# name: offers[0], industry: offers[2]
# pair: relationships_new[0], relationships_new[1]


a = []
b = []
c = []
for i in offers:
	if i[0] == 'Amy':
		a.append(i)
	elif i[0] == 'Bob':
		b.append(i)
	elif i[0] == 'Charlie':
		c.append(i)

a_combi = []
b_combi = []
c_combi = []
for i in a: 
	for j in b:
			if (i[0],j[0]) in [m for m, n in relationships_new]:
				a_combi.append([i,j,(i[0],j[0])])

				
for i in a:
	for k in c:
		if (i[0],k[0]) in [m for m, n in relationships_new]:
				a_combi.append([i,k,(i[0],k[0])])

for i in b:
	for j in a:
		if (i[0],j[0]) in [m for m, n in relationships_new]:
				b_combi.append([i,j,(i[0],j[0])])
for i in b:
	for k in c:
		if (i[0],k[0]) in [m for m, n in relationships_new]:
				b_combi.append([i,k,(i[0],k[0])])

for i in c:
	for j in a:
		if (i[0],j[0]) in [m for m, n in relationships_new]:
				c_combi.append([i,j,(i[0],j[0])])

for i in c:
	for k in b:
		if (i[0],k[0]) in [m for m, n in relationships_new]:
				c_combi.append([i,k,(i[0],k[0])])



a_combi_full = [[i, j, k, b] for i, j, k in a_combi for a, b in relationships_new if k == a]
b_combi_full = [[i, j, k, b] for i, j, k in b_combi for a, b in relationships_new if k == a]
c_combi_full = [[i, j, k, b] for i, j, k in c_combi for a, b in relationships_new if k == a]

#for i, j, k, l in c_combi_full:
	#print 'Name: %s.' %(i[0]), (i[1], i[3], i[4], j[4], l)

#for i in range(len(c_combi_full)):
#	return c_combi_full[i][0][1]
def personalities(person):
	if person == 'Money Grubber':
		return [10, -1, 4, 2]
	elif person[1] == 'Entrepreneur':
		return [4, -2, 10, 8]
	elif person[1] == 'Slacker':
		return [1, -10, 2, 2]
	elif person[1] == 'Academic':
		return [2, -6, 8, 10]
	else:
		return 'S/he is not a human...Happy 2016!'

def offers(job):
	if job == 'Big Software Firm':
		return [6, 6, 2, 8]
	elif job == 'Hedge Fund':
		return [8, 8, 4, 6]
	elif job == 'Investment Bank':
		return [10, 10, 3, 4]
	elif job == 'Startup':
		return [4, 8, 10, 8]
	elif job == 'Grad School':
		return [1, 4, 3, 10]
	else:
		return 'S/he got not job...Happy 2016!'

c_pre_cal = []
for i in c_combi_full:
	c_pre_cal.append([i[0][0],i[0][1], i[0][3], i[0][4], i[1][4], i[3]])
