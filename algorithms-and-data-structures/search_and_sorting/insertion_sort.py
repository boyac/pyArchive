# https://www.youtube.com/watch?v=c4BRHC7kTaQ&ebc=ANyPxKqtvf4vnJvX_-MvFdFz0VvIVjCP78snuSWurShDi02Nz32LELcBhRFsBcIS4z-pB1XiJgoZ

def insertion_sort(lst):
	for i in range(1, len(lst)):
		j = i
		while j > 0 and lst[j] < lst[j-1]: # while the previous item is bigger than current item, swap value
			lst[j], lst[j-1] = lst[j-1], lst[j]
			j = j-1 # reposition index until the while loop ends
	return lst
	
lst = [27, 33, 28, 4, 2, 26, 13, 35, 8, 14]
print insertion_sort(lst)
