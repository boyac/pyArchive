def search_nested(lst, val):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            #print i,j
            if lst[i][j] == val:
                return lst[i]
    return str(val) + ' not found'
nested_list = [[1,2,3],[5,6,7],[9,10,11]]
print search_nested(nested_list, 1)
print search_nested(nested_list, 4)
print search_nested(nested_list, 6)
