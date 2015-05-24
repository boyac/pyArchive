# ch05 salary survey data
# BACKGROUND and MODEL DESCRIPTION
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


df = pd.read_table("P130.txt")
y = df.S #response
x1 = df.X #predictor
x2 = df.E
x3 = df.M
est = sm.ols(formula="y ~ x1 + x2 + x3", data=df).fit()
print est.summary()
