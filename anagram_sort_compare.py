combo = ['Amy', 'Bob']
#combo2 = ['Bob', 'Ted'] 
re = ['Bob', 'Amy', 'Friends']

def connection_2(s1,s2):
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos] == alist2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches

print(connection_2(combo,re))
