# ref: https://www.youtube.com/watch?v=6nDMgr0-Yyo

def select_sort(lst):
	index = len(lst) - 1
	while index:
		max_index = index
		for i in range(index):
			if lst[i] > lst[max_index]:
				max_index = i
		if lst[max_index] > lst[index]:
			lst[index], lst[max_index] = lst[max_index], lst[index]
		index -= 1
