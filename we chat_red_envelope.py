import numpy as np, numpy.random
def money(amount, n):
    return np.random.dirichlet(np.ones(n),size=1) * amount # data clean 就不處理了
print money(10, 15) #假設有10元，隨機分給15個人
