# ch05 salary survey data

# STEP 1. MODEL BUILDING
"""
Qualitative or categorical variables can be very useful 
as predictor variables in regression analysis,
which take only two values, usually 0 and 1.

//DESCRIPTION
Below example shows an analysis of salaries earned by computer programmers;
the response variable is salary (S) and 
The predictors are: 
(1) experience (X), measured in years; 
(2) education (E), coded as 1 for completion of a high school (H.S.) diploma, 
	2 for completion of a bachelor degree (B.S.), and 
	3 for the completion of an advanced degree; and 
(3) management(M), which is coded as 1 for a person with management responsibility 
	and 0 otherwise

//MODEL FUNCTION: 
a linear relationship will be used for salary and experience.
we shall assume that each additional year of experience is worth a fixed salary increment.
education may also be treated in a linear fashion.	

//MODEL_01 # to be refined
S = B0 + B1X + r1E1 + r2E2 + s1M + e
"""

# CODE
import pandas as pd
import statsmodels.formula.api as sm

df = pd.read_table("P130.txt")
y = df.S # response
x1 = df.X 
x2 = df.E
x3 = df.M
est = sm.ols(formula="y ~ x1 + x2 + x3", data=df).fit()
print est.summary()


# STEP 2. MODEL ADAQUACY
"""
			OLS Regression Results
==============================================================================
Dep. Variable:                      y   R-squared:                       0.928
Model:                            OLS   Adj. R-squared:                  0.923
Method:                 Least Squares   F-statistic:                     179.6
Date:                Sun, 24 May 2015   Prob (F-statistic):           5.60e-24
Time:                        16:31:26   Log-Likelihood:                -393.45
No. Observations:                  46   AIC:                             794.9
Df Residuals:                      42   BIC:                             802.2
Df Model:                           3
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [95.0% Conf. Int.]
------------------------------------------------------------------------------
Intercept   6963.4777    665.695     10.460      0.000      5620.051  8306.904
x1           570.0874     38.559     14.785      0.000       492.272   647.903
x2          1578.7503    262.322      6.018      0.000      1049.364  2108.137
x3          6688.1299    398.276     16.793      0.000      5884.377  7491.883
==============================================================================
Omnibus:                        2.672   Durbin-Watson:                   2.264
Prob(Omnibus):                  0.263   Jarque-Bera (JB):                1.863
Skew:                           0.479   Prob(JB):                        0.394
Kurtosis:                       3.229   Cond. No.                         33.6
==============================================================================
"""


# Step 3. MODEL ASSUMPTION
# Residual test and diagnostic plots
