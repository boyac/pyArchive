# -*- coding: utf-8 -*-
# @Author: boyac
# @Date:   2016-04-27 20:40:29
# @Last Modified by:   boyac
# @Last Modified time: 2016-04-27 21:52:54

def area(K, L, M, N, P, Q, R, S):
	"""	
	Calculate the sum of areas of two rectangles and 
	count only once for the overlapped area if any.
	"""
	area = (M-K)*(N-L)+(R-P)*(S-Q)
	overlap = (M-P)*(S-L)
	if area <= 2147483647:
		return [area if (P>M or S<L) else (area-overlap)]
	else:
		return -1
		
print area(-4, 1, 2, 6, 0, -1, 4, 3)
