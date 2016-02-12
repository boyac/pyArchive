＃Red envelope lucky draw
"""
The user assigns a lump sum to a group red envelope, 
and the number of small red envelopes within it. 
After posting to a group chat, WeChat will randomly assign the amount in each envelope to each recipient
"""
import numpy as np, numpy.random
def money(amount, n):
    return np.random.dirichlet(np.ones(n),size=1) * amount # data clean 就不處理了
print money(10, 15) #假設有10元，隨機分給15個人
