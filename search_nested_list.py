def search_nested(mylist, val):
    for i in range(len(mylist)):
        for j in range(len(mylist[i])):
            #print i,j
            if mylist[i][j] == val:
                return mylist[i]
    return str(val) + ' not found'
nested_list = [[1,2,3],[5,6,7],[9,10,11]]
print search_nested(nested_list, 1)
print search_nested(nested_list, 4)
print search_nested(nested_list, 6)
