Consumer expenditure and money stock in the United States.
Data: during 1952 to 1956; quarterly data in billions of dollars units.

CONSUMER_EXPENDITURE = -154.719 + 2.300MONEY_STOCK

```
. reg expendit stock

      Source |       SS       df       MS              Number of obs =      20
-------------+------------------------------           F(  1,    18) =  403.22
       Model |  6395.76619     1  6395.76619           Prob > F      =  0.0000
    Residual |  285.511158    18   15.861731           R-squared     =  0.9573
-------------+------------------------------           Adj R-squared =  0.9549
       Total |  6681.27735    19  351.646176           Root MSE      =  3.9827

------------------------------------------------------------------------------
    expendit |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
       stock |    2.30037   .1145584    20.08   0.000     2.059692    2.541049
       _cons |  -154.7191   19.85004    -7.79   0.000    -196.4225   -113.0157
------------------------------------------------------------------------------
```
