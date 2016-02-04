combo = ['Boya', 'Alexis']
#combo2 = ['Bob', 'Ted'] 
re = ['Boya', 'Alexis', 'Couple']
#re2 = ['Alexis', 'X.X', 'Married']
#re3 = ['Alexis','Eric', 'Friends']
#re4 = ['Alexis', 'Neil', 'Enemies']

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
