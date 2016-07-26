def tagit(tag='p'):
	def deco(func):
		def new_func(title,txt):
			print '<'+tag+'>' + txt + '</'+tag+'>'
			print '#' + ' ' + title 
			print '-' + ' ' + txt
		return new_func
	return deco

@tagit(tag='h1')
def printer(title,txt):
	print txt


if __name__ == '__main__':
	print printer('pydata','use python 2.7')
