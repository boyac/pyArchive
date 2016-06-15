#### claims of insurance (count data) given gender, number of people in the family, number of children in the family, income level

![alt tag](zp.jpg)

```stata
. summarize sex person child inc count

    Variable |       Obs        Mean    Std. Dev.       Min        Max
-------------+--------------------------------------------------------
         sex |       250        .588    .4931824          0          1
      person |       250       3.464    1.788154          1          6
       child |       250        .684    .8503153          0          3
         inc |       250    62.52322    21.02394      3.741    102.632
       count |       250       3.296    11.63503          0        149

. zip count sex child inc, inflate(person) vuong

Fitting constant-only model:

Iteration 0:   log likelihood =  -1347.807  
Iteration 1:   log likelihood = -1315.9747  
Iteration 2:   log likelihood = -1127.5224  
Iteration 3:   log likelihood = -1126.7194  
Iteration 4:   log likelihood = -1126.7194  

Fitting full model:

Iteration 0:   log likelihood = -1126.7194  
Iteration 1:   log likelihood = -1039.5401  
Iteration 2:   log likelihood = -1024.7435  
Iteration 3:   log likelihood = -1024.4317  
Iteration 4:   log likelihood = -1024.4312  
Iteration 5:   log likelihood = -1024.4312  

Zero-inflated Poisson regression                  Number of obs   =        250
                                                  Nonzero obs     =        108
                                                  Zero obs        =        142

Inflation model = logit                           LR chi2(3)      =     204.58
Log likelihood  = -1024.431                       Prob > chi2     =     0.0000

------------------------------------------------------------------------------
       count |      Coef.   Std. Err.      z    P>|z|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
count        |
         sex |   .6529134   .1003157     6.51   0.000     .4562981    .8495286
       child |  -.6915566      .1192    -5.80   0.000    -.9251843   -.4579288
         inc |   .0195758   .0042398     4.62   0.000      .011266    .0278857
       _cons |   .1367576   .3320234     0.41   0.680    -.5139963    .7875115
-------------+----------------------------------------------------------------
inflate      |
      person |   -.314848   .1059679    -2.97   0.003    -.5225413   -.1071546
       _cons |   .8881401   .3242491     2.74   0.006     .2526235    1.523657
------------------------------------------------------------------------------
Vuong test of zip vs. standard Poisson:            z =     3.79  Pr>z = 0.0001
```
