# ref: https://www.youtube.com/watch?v=6nDMgr0-Yyo
# search for the smallest element and swap it into the first position
# and search rest of the array and again finding the smallest element and swap into the 2nd postion

def selection_sort(lst):
	index = len(lst) - 1 # index of remaining unsorted list
	while index:
		min_index = index
		for i in range(index):
			if lst[i] > lst[min_index]:
				min_index = i
		if lst[min_index] > lst[index]:
			lst[index], lst[min_index] = lst[min_index], lst[index]
		index -= 1
	return lst


lst = [27, 33, 28, 4, 2, 26, 13, 35, 8, 14]
print selection_sort(lst)
