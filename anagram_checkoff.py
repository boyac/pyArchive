# checking if the combination appears in the relationship chart
# will need to develop into nested lists

combo = ['Amy', 'Bob']
#combo2 = ['Bob', 'Ted'] 
re = ['Bob', 'Amy', 'Friends']

def connect(s1,s2):
    pos1 = 0
    new = []
    while pos1< len(s1):
        pos2 = 0
        while pos2 < len(s2):
            if s1[pos1] == s2[pos2]:
                new.append(s1[pos1])
                break
            else:
                pos2 = pos2 + 1
        pos1 = pos1 + 1
    
    if len(new) == 2:
        new.append(re[2])
    return new 

print(connect(combo, re))



