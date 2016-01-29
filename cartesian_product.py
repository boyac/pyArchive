# Ref: https://zh.wikipedia.org/wiki/笛卡儿积

import itertools
p0 = [[10, -1, 4, 2], [4, -2, 10, 8], [1, -10, 2, 2], [2, -6, 8, 10]]
j0 = [[6, 6, 2, 8], [8, 8, 4, 6], [10, 10, 3, 4], [4, 8, 10, 8], [1, 4, 3, 10]]

utility = []
for combi in itertools.product(p0, j0):
    utility.append(map(lambda x, y: x*y, combi[0], combi[1]))

# calculate the sum of each item in cartesian product
def summation(utility):    
    for i in utility:
        print reduce(lambda x, y: x+y, i)

print summation(utility)
	




