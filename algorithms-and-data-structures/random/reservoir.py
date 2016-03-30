import random

def reservoir_sampling(n, k): # n as unknow size of population, k as sample size
    sample = items[0:k]
    for i in range(k, len(items)):
    	j = random.randrange(1, i + 1)
    	if j <= k:
    		sample[j] = items[i]
    return sample
