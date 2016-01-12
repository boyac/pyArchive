"""
input_1 = people (name | personalities)
input_2 = offers (company_name | type | locations)
input_3 = relationships (name | relationships)
"""

#people
#Amy | Academic
#Bob | Entrepreneur
#Charlie | Money Grubber

#offers
#Amy | MacroHard | Big Software Firm | Seattle
#Amy | Stanguard College | Grad School | San Francisco
#Amy | Dartboard Modeling | Hedge Fund | NYC
#Bob | Bigup-Side | Startup | NYC
#Bob | Questionable Tactics | Hedge Fund | San Francisco
#Charlie | Cash-Money Inc. | Investment Bank | NYC
#Charlie | Arbitrack | Hedge Fund | San Francisco

#relationships
#Bob | Amy | Dating
#Bob | Charlie | Mortal Enemies


"""
#SQL_db
import sqlite3
connection = sqlite3.connect("data.db")
cursor = connection.cursor()
# delete 
#cursor.execute(DROP TABLE employee;)
sql_command = 
CREATE TABLE people ( 
name VARCHAR(50) PRIMARY KEY, 
personalities VARCHAR(50); 
cursor.execute(sql_command)
cursor = connection.cursor()

people = [('Amy', 'academic'), ('Bob', 'entrepreneur'), ('Charlie','money_grubber')]
offers = [('Amy', 'MacroHard', 'Big Software Firm', 'Seattle'), ('Amy', 'Stanguard College', 'grad_school', 'San Francisco'), 
			('Bob', 'Bigup-Side', 'Startup', 'NYC'), ('Charlie', 'Cash-Money Inc.', 'investment_bank', 'NYC'),
			('Charlie', 'Arbitrack', 'hedge_fund', 'San Francisco')]
relationships = [('Bob', 'Amy', 'Dating'), ('Bob', 'Charlie', 'Mortal Enemies')]

for i in people:
	format_str = INSERT INTO people (name, personalities)
	VALUES ('{name}', '{personalities}');
	sql_command = format_str.format(name=i[0], personalities=i[1])
	cursor.execute(sql_command)
# never forget this, if you want the changes to be saved:
connection.commit()
connection.close()
"""
"""
#dictionaries
offers = [
{'name': 'Amy', 'company': 'MacroHard', 'industry': 'Big Software Firm', 'locations': 'Seattle'},
{'name': 'Amy', 'company': 'Stanguard College', 'industry': 'Grad School', 'locations': 'San Francisco'},
{'name': 'Amy', 'company': 'Dartboard Modeling', 'industry': 'Hedge Fund', 'locations': 'NYC'},
{'name': 'Bob', 'company': 'Bigup-Side', 'industry': 'Startup', 'locations': 'NYC'},
{'name': 'Bob', 'company': 'Questionable Tactics', 'industry': 'Hedge Fund', 'locations': 'San Francisco'},
{'name': 'Charlie', 'company': 'Cash-Money Inc.', 'industry': 'Investment Bank', 'locations': 'NYC'},
{'name': 'Charlie', 'company': 'Arbitrack', 'industry': 'Hedge Fund', 'locations': 'San Francisco'}
]

relationships = [
{'name1': 'Bob', 'name2': 'Amy', 'relationships': 'Dating'},
{'name1': 'Bob', 'name2': 'Charlie', 'relationships': 'Mortal Enemies'}
]
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
['Amy', 'MacroHard', 'Big Software Firm', 'Seattle'],
['Amy', 'Stanguard College', 'Grad School', 'San Francisco'],
['Amy', 'Dartboard Modeling', 'Hedge Fund', 'NYC'],
['Bob', 'Bigup-Side', 'Startup', 'NYC'],
['Bob', 'Questionable Tactics', 'Hedge Fund', 'San Francisco'],
['Charlie', 'Cash-Money Inc.', 'Investment Bank', 'NYC'],
['Charlie', 'Arbitrack', 'Hedge Fund', 'San Francisco']
]

relationships = [
['Bob', 'Amy', 'Dating'],
['Bob', 'Charlie', 'Mortal Enemies']
]

relationships_new = [
[('Bob', 'Amy'), 'Dating'],
[('Bob', 'Charlie'), 'Mortal Enemies'],
[('Amy', 'Bob'), 'Dating'],
[('Charlie', 'Bob'), 'Mortal Enemies']
]

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
			a_combi.append([i,j])
for i in a:
	for k in c:
		a_combi.append([i,k])

for i in b:
	for j in a:
		b_combi.append([i,j])
for i in b:
	for k in c:
		b_combi.append([i,k])

for i in c:
	for j in a:
		c_combi.append([i,j])
for i in c:
	for k in b:
		c_combi.append([i,k])

def abc(name):
	if name == 'a':
		return a_combi
	elif name == 'b':
		return b_combi
	elif name == 'c':
		return c_combi
	else:
		return 'The name was not found, please enter again. Happy 2016!'

a_combi_local = []
b_combi_local = []
c_combi_local = []
for i, j in a_combi:
	a_combi_local.append([(i[0],j[0]),(i[3],j[3])])
for i, j in b_combi:
	b_combi_local.append([(i[0],j[0]),(i[3],j[3])])
for i, j in c_combi:
	c_combi_local.append([(i[0],j[0]),(i[3],j[3])])
#print a_combi_local[0]
#print relationships_new[2]

def check_combo(name):
	if name == 'a':
		for i, j in a_combi_local:
			if i in (i for i, j in relationships_new):
				if j[0] == j[1]:
					print i, j
	elif name == 'b':
		for i, j in b_combi_local:
			if i in (i for i, j in relationships_new):
				if j[0] == j[1]:
					print i, j
	elif name == 'c':
		for i, j in c_combi_local:
			if i in (i for i, j in relationships_new):
				if j[0] == j[1]:
					print i, j
	else:
		return 'The name was not found, please enter again. Happy 2016!'


