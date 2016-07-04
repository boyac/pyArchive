# Recipes 3
#2 features: height, eye color

import numpy as np
import matplotlib.pyplot as plt

grevyhounds = 500 
labs = 500

# + or - 4 inches randomly
grey_height = 28 + 4 * np.random.randn(grevyhounds)
lab_height = 24 + 4 * np.random.randn(labs)

plt.hist([grey_height, lab_height], stacked=True, color=['r','b'])
plt.show()

# 50/50 features doesn't tell much infomation
# avoid redundant features
# Ideal features are: informative, independent, simple