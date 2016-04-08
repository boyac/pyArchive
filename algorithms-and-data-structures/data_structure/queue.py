# -*- coding: utf-8 -*-
# @Author: boyac
# @Date:   2016-04-08 22:50:17
# @Last Modified by:   boyac
# @Last Modified time: 2016-04-08 22:57:31

class Queue:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return len(self.items) == 0

	def enqueue(self, item):
		self.items.insert(0, item)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)
