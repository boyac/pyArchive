# ch05 salary survey data
"""
Qualitative or categorical variables can be very useful 
as predictor variables in regression analysis,
which take only two values, usually 0 and 1.

Below example shows an analysis of salaries earned by computer programmers,
include variables such as:
1. education
2. years of experience
3. sex
as predictor variables
"""

import pandas as pd
from matplotlib.pyplot import *
x = pd.read_table("P130.txt")
plot(x)
xlabel ("x- axis")
ylabel ("my numbers")
title("my figure")
show()
print x

