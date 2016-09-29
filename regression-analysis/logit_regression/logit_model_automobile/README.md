- Description: predict whether a car is foreign on the basis of its weight an mileage.
- Result: heavier and better mileage cars are less likely to be foreign.

```stata
. use http://www.stata-press.com/data/r13/auto, clear
(1978 Automobile Data)

. keep make mpg weight foreign

. describe

Contains data from http://www.stata-press.com/data/r13/auto.dta
  obs:            74                          1978 Automobile Data
 vars:             4                          13 Apr 2013 17:45
 size:         1,702                          (_dta has notes)
--------------------------------------------------------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
--------------------------------------------------------------------------------------------------------------------------------
make            str18   %-18s                 Make and Model
mpg             int     %8.0g                 Mileage (mpg)
weight          int     %8.0gc                Weight (lbs.)
foreign         byte    %8.0g      origin     Car type
--------------------------------------------------------------------------------------------------------------------------------
Sorted by:  foreign
     Note:  dataset has changed since last saved

. inspect foreign

foreign:  Car type                              Number of Observations
------------------                          ------------------------------
                                            Total   Integers   Nonintegers
|  #                         Negative           -         -          -
|  #                         Zero              52        52          -
|  #                         Positive          22        22          -
|  #                                        -----     -----      -----
|  #   #                     Total             74        74          -
|  #   #                     Missing            -
+----------------------                     -----
0                     1                        74
   (2 unique values)

      foreign is labeled and all values are documented in the label.

. logit foreign weight mpg

Iteration 0:   log likelihood =  -45.03321  
Iteration 1:   log likelihood = -29.238536  
Iteration 2:   log likelihood = -27.244139  
Iteration 3:   log likelihood = -27.175277  
Iteration 4:   log likelihood = -27.175156  
Iteration 5:   log likelihood = -27.175156  

Logistic regression                               Number of obs   =         74
                                                  LR chi2(2)      =      35.72
                                                  Prob > chi2     =     0.0000
Log likelihood = -27.175156                       Pseudo R2       =     0.3966

------------------------------------------------------------------------------
     foreign |      Coef.   Std. Err.      z    P>|z|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
      weight |  -.0039067   .0010116    -3.86   0.000    -.0058894    -.001924
         mpg |  -.1685869   .0919175    -1.83   0.067    -.3487418     .011568
       _cons |   13.70837   4.518709     3.03   0.002     4.851859    22.56487
------------------------------------------------------------------------------
```

