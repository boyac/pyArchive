# ch05 salary survey data
"""
Qualitative or categorical variables can be very useful 
as predictor variables in regression analysis,
which take only two values, usually 0 and 1.

Below example shows an analysis of salaries earned by computer programmers;
the response variable is salary (S) and 
The predictors are: 
(1) experience (X), measured in years; 
(2) education (E), coded as 1 for completion of a high school (H.S.) diploma, 
    2 for completion of a bachelor degree (B.S.), and 
	3 for the completion of an advanced degree; and 
(3) management(M), which is coded as 1 for a person with management responsibility 
	and 0 otherwise

//model functions: 
a linear relationship will be used for salary and experience.
we shall assume that each additional year of experience is worth a fixed salary increment.
education may also be treated in a linear fashion.	

//model 
S = B0 + B1X + r1E1 + r2E2 + s1M + e
"""
import pandas as pd
import statsmodels.formula.api as sm

"""import numpy as np
from pandas.stats.api import ols
from matplotlib.pyplot import *
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
"""

df = pd.read_table("P130.txt")
y = df.S #response
x1 = df.X #predictor
x2 = df.E
x3 = df.M
est = sm.ols(formula="y ~ x1 + x2 + x3", data=df).fit()
print est.summary

"""
est = sm.OLS(y, x)
est = est.fit()
est.summary()
#%pylab inline
x_prime = np.linspace(x.X.min(), x.X.max(), 100)[:, np.newaxis]
x_prime = sm.add_constant(x_prime) # add constant as we did before

# now we calculate the predicted values
y_hat = est.predict(x_prime)

plt.scatter(x.X, y, alpha=0.3) #plot the raw data
plt.xlabel("Years of Experiences")
plt.ylabel("Salary")
plt.plot(x_prime[:, 1], y_hat, 'r', alpha=0.9) # Add the regression line, colored in red

plot(df)
xlabel ("x- axis")
ylabel ("my numbers")
title("my figure")
show()
print df
"""
