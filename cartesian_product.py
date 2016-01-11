"""
input_1 = people (name | personalities)
input_2 = offers (company | type | locations)
input_3 = relationships (name | relationships)

"""
def personalities(pay, hours, impact, edu):
	money_grubber = [10, -1, 4, 2]
	entrepreneur = [4, -2, 10, 8]
	slacker = [1, -10, 2, 2]
	acamemic = [2, -6, 8, 10]
	#personalities = [[10, -1, 4, 2], [4, -2, 10, 8], [1, -10, 2, 2], [2, -6, 8, 10]]
	#personalities = [10, -1, 4, 2]

def jobs(pay, hours, impact, edu):
	soft_ware = [6, 6, 2, 8]
	hedge_fund = [8, 8, 4, 6]
	investment_bank = [10, 10, 3, 4]
	startup = [4, 8, 10, 8]
	gard_school = [1, 4, 3, 10]
	#jobs = [[6, 6, 2, 8], [8, 8, 4, 6], [10, 10, 3, 4], [4, 8, 10, 8], [1, 4, 3, 10]]
	#jobs = [6, 6 , 2, 8]


#personalities = [[10, -1, 4, 2], [4, -2, 10, 8], [1, -10, 2, 2], [2, -6, 8, 10]]
#jobs = [[6, 6, 2, 8], [8, 8, 4, 6], [10, 10, 3, 4], [4, 8, 10, 8], [1, 4, 3, 10]]
import itertools
p = [10, -1, 4, 2]
j = [6, 6 , 2, 8]
p0 = [[10, -1, 4, 2], [4, -2, 10, 8], [1, -10, 2, 2], [2, -6, 8, 10]]
j0 = [[6, 6, 2, 8], [8, 8, 4, 6], [10, 10, 3, 4], [4, 8, 10, 8], [1, 4, 3, 10]]

utility = []
for combi in itertools.product(p0, j0):
    utility.append(map(lambda x, y: x*y, combi[0], combi[1]))
	
for i in utility:
	print reduce(lambda x, y: x+y, i)


	
#print utility(personalities, jobs)
#utility = map(lambda x, y: x*y, p, j)
#u_total = reduce(lambda x, y: x+y, utility)
#print u_total





