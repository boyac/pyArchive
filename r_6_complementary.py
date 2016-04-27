# -*- coding: utf-8 -*-
# @Author: boyac
# @Date:   2016-04-27 20:40:29
# @Last Modified by:   boyac
# @Last Modified time: 2016-04-27 21:52:54

A = [(0, 8),(1,6),(4,8),(5,5),(6,1),(8,0),(8,4)]
A_value = [1, 8, -3, 0, 1, 3, -2, 4, 5]

Klist = []
for i, j in A:
    K = A_value[i] + A_value[j]
    Klist.append(K)

print Klist.count(K)
