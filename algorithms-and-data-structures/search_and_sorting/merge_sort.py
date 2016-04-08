# http://interactivepython.org/runestone/static/pythonds/SortSearch/TheMergeSort.html

def merge_sort(lst):
	if len(lst) > 1:
		mid = len(lst)/2
		lefthalf = lst[:mid]
		righthalf = lst[mid:]

		merge_sort(lefthalf) # keep split lists
		merge_sort(righthalf) # keep split lists

		i = 0
		j = 0
		k = 0 # new merged list index
		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i] < righthalf[j]:
				lst[k] = lefthalf[i]
				i = i+1
			else:
				lst[k] = righthalf[j]
				j = j+1
			k = k+1

		while i < len(lefthalf):
			lst[k] = lefthalf[i]
			i = i+1
			k = k+1

		while j < len(righthalf):
			lst[k] = righthalf[j]
			j = j+1
			k = k+1
	return lst	


lst = [27, 33, 28, 4, 2, 26, 13, 35, 8, 14]
print merge_sort(lst)
