# pytest

def Klist(A, A_value):
	Klist = []
	for i, j in A:
	    K = A_value[i] + A_value[j]
	    Klist.append(K)
	return Klist.count(K)

def test_Klist():
	assert Klist(A, A_value) == 7

A = [(0, 8),(1,6),(4,8),(5,5),(6,1),(8,0),(8,4)] # index number pairing
A_value = [1, 8, -3, 0, 1, 3, -2, 4, 5] # corresponding values

print Klist(A, A_value)
