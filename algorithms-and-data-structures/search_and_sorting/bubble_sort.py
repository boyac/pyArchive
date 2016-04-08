#ref: https://www.youtube.com/watch?v=P00xJgWzz2c

def bubble_sort(lst):
    for j in range(len(lst)-1,0,-1): # range(start, end, step)
        for i in range(0,j):
            if lst[i] > lst[i+1]:
            	lst[i],lst[i+1] = lst[i+1],lst[i] #if List[i] > List[i+1], swaps position
    return lst


lst = [27, 33, 28, 4, 2, 26, 13, 35, 8, 14]
print bubble_sort(lst)
