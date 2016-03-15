# Hash Map
# hashmap: key(either an integer or a string) pairs a value
# O(1) for add, get, delete function, so it is extremely fast
# in python, use dict
# components of hashmap: array, hash function(convert key into index), collision handling
# better hash function: index = sum(ASCII value for each letter in key) % 5, which can randonly distributed our data into an array

class HashMap:
	def __init__(self):
		self.size = 6
		self.map = [None] * self.size #force python to create a list with fixed length
	
	def _get_hash(self, key):
		hash = 0
		for char in str(key):
			hash += ord(char)
		return hash % self.size

	def add(self, key, value):
		key_hash = self._get_hash(key) #index value we gonna place in
		key_value = [key, value]

		if self.map[key_hash] is None:
			self.map[key_hash] = list([key_value])
			return True
		else:
			for pair in self.map[key_hash]:
				if pair[0] == key:
					pair[1] = value
					return True
			self.map[key_hash].append(key_value)
			return True

	def get(self, key): #return value of that key
		key_hash = self._get_hash(key)
		if self.map[key_hash] is not None:
			for pair in self.map[key_hash]:
				if pair[0] == key:
					return pair[1]
		return None

	def delete(self, key):
		key_hash = self._get_hash(key)
		if self.map[key_hash] is None:
			return False
		for i in range(0, len(self.map[key_hash])):
			if self.map[key_hash][i][0] == key:
				self.map[key_hash].pop(i)
				return True

	def print_(self):
		print('---PHONEBOOK---')
		for item in self.map:
			if item is not None:
				print(str(item))

h = HashMap()
h.add('Bob', '567-9999')
h.add('Ming', '293-0000')
h.add('Ankit', '222-9872')
h.add('Alicia', '444-2991')
h.add('Mike', '222-0000')
h.print_()
h.delete('Bob')
h.print_()
print('Ming:' + h.get('Ming'))
