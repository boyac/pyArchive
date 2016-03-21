class Sort:
	def __init__(self, myList):
		self.myList = myList

	def bubble(self):
	    for j in range(len(self.myList)-1,0,-1): # range(start, end, step)
	        for i in range(0,j):
	            if self.myList[i] > self.myList[i+1]:
	            	self.myList[i],self.myList[i+1] = self.myList[i+1],self.myList[i] #if List[i] > List[i+1], swaps position
	    return self.myList
	
	#def insertion(self):
	
	#def merge(self):
		

def main(): #instantiating the class, for the class we created to be actually use
	#instaniate the class
	testlist = Sort([27, 33, 28, 4, 2, 26, 13, 35, 8, 14])
	print testlist.bubble()
	#print testlist.insertion()

if __name__== "__main__":
	main()
