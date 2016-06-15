#### ln(u) = constant + beta1*Race + beta2*Income + beta3*GPA
- predicts number of job offers, given indivuals race(categorical), parents income(continuous), gpa score(continuous)

```stata
. summarize job race income gpa

    Variable |       Obs        Mean    Std. Dev.       Min        Max
-------------+--------------------------------------------------------
         job |       200        .755    1.184054          0          6
        race |       200       2.025    .6904772          1          3
      income |       200    63.66208    11.26087     39.693     90.936
         gpa |       200      2.7868    .7366328        1.5       3.99

. poisson job i.race income gpa, vce(robust)

Iteration 0:   log pseudolikelihood = -192.07007  
Iteration 1:   log pseudolikelihood = -192.06193  
Iteration 2:   log pseudolikelihood = -192.06193  

Poisson regression                                Number of obs   =        200
                                                  Wald chi2(4)    =     124.08
                                                  Prob > chi2     =     0.0000
Log pseudolikelihood = -192.06193                 Pseudo R2       =     0.2562

------------------------------------------------------------------------------
             |               Robust
         job |      Coef.   Std. Err.      z    P>|z|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
        race |
          2  |   1.033785   .2716525     3.81   0.000     .5013555    1.566214
          3  |   .2702573   .3497969     0.77   0.440     -.415332    .9558466
             |
      income |    .064258   .0079459     8.09   0.000     .0486843    .0798317
         gpa |   .1219593      .1259     0.97   0.333    -.1248001    .3687187
       _cons |  -5.807757   .7557297    -7.68   0.000     -7.28896   -4.326554
------------------------------------------------------------------------------

. poisson, irr # convert coefficient from log count into count

Poisson regression                                Number of obs   =        200
                                                  Wald chi2(4)    =     124.08
                                                  Prob > chi2     =     0.0000
Log pseudolikelihood = -192.06193                 Pseudo R2       =     0.2562

------------------------------------------------------------------------------
             |               Robust
         job |        IRR   Std. Err.      z    P>|z|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
        race |
          2  |   2.811687   .7638018     3.81   0.000     1.650958    4.788483
          3  |   1.310302   .4583394     0.77   0.440     .6601211    2.600872
             |
      income |   1.066367   .0084733     8.09   0.000     1.049889    1.083105
         gpa |   1.129708   .1422302     0.97   0.333     .8826733    1.445881
       _cons |   .0030042   .0022703    -7.68   0.000      .000683     .013213
------------------------------------------------------------------------------
```
