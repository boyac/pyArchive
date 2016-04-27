# -*- coding: utf-8 -*-
# @Author: boyac
# @Date:   2016-04-27 19:12:18
# @Last Modified by:   boyac
# @Last Modified time: 2016-04-27 19:12:54

def rec(a, b):
	""""
	return if retangles overlaps, even points
	"""
	if b[0][0] > a[1][0]:
		return 'Safe'
	elif b[1][0] < a[0][0]:
		return 'Safe'
	elif b[0][1] > a[1][1]:
		return 'Safe'
	elif b[1][1] < a[0][1]:
		return 'Safe'
	else:
		return 'overlapping'

	# case of not overlapping
	# P2x > P1x
	# P3x < P0x
	# P2y > P1y
	# P3y < P0y

a = ((0,0), (2,2)) #p0, p1 = a([0][0],a[0][1]) | a[1][0], a[1][1] | x, y
b = ((4,4), (3,5)) #p2, p3 = b([0][0],b[0][1]) | b[1][0], b[1][1] | x, y

print rec(a,b)
