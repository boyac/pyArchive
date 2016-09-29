#### ESTIMATING PROBABILITY OF BANKRUPTCIES
#### ln((p)/(1-p)) = -10.15 + 0.33x1 + 0.18x2 + 5.09x3
- model: logit model
- method of estimation: maximum likelihood method
- y = 0 if bankrupt after 2 years; y = 1 if solvent after 2 years.
- x1 = Retained Earnings / Total Assets
- x2 = Earnings Before Interest and Taxes / Total Assets 
- x3 = Sales / Total Assets

```stata
. logit y x1 x2 x3

Iteration 0:   log likelihood = -45.747714  
Iteration 1:   log likelihood = -11.354799  
Iteration 2:   log likelihood = -5.0499239  
Iteration 3:   log likelihood = -3.1644536  
Iteration 4:   log likelihood = -2.9636672  
Iteration 5:   log likelihood = -2.9069846  
Iteration 6:   log likelihood = -2.9064526  
Iteration 7:   log likelihood = -2.9064524  

Logistic regression                               Number of obs   =         66
                                                  LR chi2(3)      =      85.68
                                                  Prob > chi2     =     0.0000
Log likelihood = -2.9064524                       Pseudo R2       =     0.9365

------------------------------------------------------------------------------
           y |      Coef.   Std. Err.      z    P>|z|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
          x1 |   .3312467   .3007414     1.10   0.271    -.2581957    .9206891
          x2 |   .1808756   .1069231     1.69   0.091    -.0286899    .3904411
          x3 |   5.087463   5.082157     1.00   0.317    -4.873381    15.04831
       _cons |  -10.15345   10.84008    -0.94   0.349    -31.39962    11.09273
------------------------------------------------------------------------------
Note: 17 failures and 10 successes completely determined.
```

```stata
. logit, or

Logistic regression                               Number of obs   =         66
                                                  LR chi2(3)      =      85.68
                                                  Prob > chi2     =     0.0000
Log likelihood = -2.9064524                       Pseudo R2       =     0.9365

------------------------------------------------------------------------------
           y | Odds Ratio   Std. Err.      z    P>|z|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
          x1 |   1.392703   .4188436     1.10   0.271      .772444     2.51102
          x2 |   1.198266   .1281224     1.69   0.091     .9717178    1.477632
          x3 |   161.9785      823.2     1.00   0.317     .0076475     3430812
       _cons |   .0000389   .0004221    -0.94   0.349     2.31e-14    65691.77
------------------------------------------------------------------------------
Note: 17 failures and 10 successes completely determined.
```
