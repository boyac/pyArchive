#### gs = 
* gross profit = revenue - cost

user engagement
campaign
size
placement
displays
cost
clicks

```stata
. reg gs dengagementh dengagementl dcmpgn1 dcmpgn2 d28 d60 d65 d75 d96 d200 d232 dplace1 dplace2 dplace3 dplace4 dplace5
>  display cost click 
note: d200 omitted because of collinearity
note: dplace5 omitted because of collinearity

      Source |       SS       df       MS              Number of obs =     683
-------------+------------------------------           F( 17,   665) =   67.74
       Model |  5588243.72    17  328720.219           Prob > F      =  0.0000
    Residual |  3226810.47   665  4852.34657           R-squared     =  0.6339
-------------+------------------------------           Adj R-squared =  0.6246
       Total |   8815054.2   682  12925.2994           Root MSE      =  69.659

------------------------------------------------------------------------------
          gs |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
dengagementh |   13.97364   7.478947     1.87   0.062      -.7115533    28.65884
dengagementl |   19.79979   6.410803     3.09   0.002**     7.211938    32.38765
     dcmpgn1 |   6.330333   6.369657     0.99   0.321      -6.176729    18.83739
     dcmpgn2 |  -35.95234   7.807854    -4.60   0.000**    -51.28336   -20.62133
         d28 |  -17.73812   18.84873    -0.94   0.347       -54.7483    19.27207
         d60 |  -22.44131   18.73838    -1.20   0.231      -59.23482    14.35221
         d65 |  -34.23231   19.51286    -1.75   0.080      -72.54655    4.081916
         d75 |   -30.6547   19.09507    -1.61   0.109       -68.1486    6.839192
         d96 |  -28.02574    18.4289    -1.52   0.129      -64.21159    8.160103
        d200 |          0  (omitted)
        d232 |  -22.49835    21.2753    -1.06   0.291       -64.2732     19.2765
     dplace1 |   2.988378   12.02756     0.25   0.804      -20.62819    26.60494
     dplace2 |  -6.789674   8.711002    -0.78   0.436      -23.89405    10.31471
     dplace3 |   1.373714    8.85313     0.16   0.877      -16.00974    18.75717
     dplace4 |    -25.428   9.703913    -2.62   0.009**      -44.482   -6.374002
     dplace5 |          0  (omitted)
     display |  -.0002445   .0001095    -2.23   0.026**    -.0004594   -.0000296
        cost |   .1200766   .0853163     1.41   0.160      -.0474452    .2875983
       click |    .084786   .0043299    19.58   0.000**      .076284     .093288
       _cons |   23.50245   19.88094     1.18   0.238      -15.53452    62.53942
------------------------------------------------------------------------------

```

###inspect
```stata

cmpg:                                           Number of Observations
-------                                     ------------------------------
                                            Total   Integers   Nonintegers
|                            Negative           -         -          -
|                            Zero               -         -          -
|                            Positive           -         -          -
|                                           -----     -----      -----
|                            Total              -         -          -
|                            Missing        15403
+----------------------                     -----
.             -9.0e+307                     15403
   (0 unique value)

egmt:                                           Number of Observations
-------                                     ------------------------------
                                            Total   Integers   Nonintegers
|                            Negative           -         -          -
|                            Zero               -         -          -
|                            Positive           -         -          -
|                                           -----     -----      -----
|                            Total              -         -          -
|                            Missing        15403
+----------------------                     -----
.             -9.0e+307                     15403
   (0 unique value)

bnnr:                                           Number of Observations
-------                                     ------------------------------
                                            Total   Integers   Nonintegers
|                            Negative           -         -          -
|                            Zero               -         -          -
|                            Positive           -         -          -
|                                           -----     -----      -----
|                            Total              -         -          -
|                            Missing        15403
+----------------------                     -----
.             -9.0e+307                     15403
   (0 unique value)

plcmt:                                          Number of Observations
--------                                    ------------------------------
                                            Total   Integers   Nonintegers
|                            Negative           -         -          -
|                            Zero               -         -          -
|                            Positive           -         -          -
|                                           -----     -----      -----
|                            Total              -         -          -
|                            Missing        15403
+----------------------                     -----
.             -9.0e+307                     15403
   (0 unique value)

display:                                        Number of Observations
----------                                  ------------------------------
                                            Total   Integers   Nonintegers
|  #                         Negative           -         -          -
|  #                         Zero              22        22          -
|  #                         Positive       15381     15381          -
|  #                                        -----     -----      -----
|  #                         Total          15403     15403          -
|  #   .   .   .   .         Missing            -
+----------------------                     -----
0                455986                     15403
(More than 99 unique values)

cost:                                           Number of Observations
-------                                     ------------------------------
                                            Total   Integers   Nonintegers
|  #                         Negative           -         -          -
|  #                         Zero              64        64          -
|  #                         Positive       15339         2      15337
|  #                                        -----     -----      -----
|  #                         Total          15403        66      15337
|  #   .   .   .   .         Missing            -
+----------------------                     -----
0              556.7048                     15403
(More than 99 unique values)

click:                                          Number of Observations
--------                                    ------------------------------
                                            Total   Integers   Nonintegers
|  #                         Negative           -         -          -
|  #                         Zero            4892      4892          -
|  #                         Positive       10511     10511          -
|  #                                        -----     -----      -----
|  #                         Total          15403     15403          -
|  #   .   .   .   .         Missing            -
+----------------------                     -----
0                 14566                     15403
(More than 99 unique values)

rev:                                            Number of Observations
------                                      ------------------------------
                                            Total   Integers   Nonintegers
|  #                         Negative           -         -          -
|  #                         Zero            5098      5098          -
|  #                         Positive       10305      1510       8795
|  #                                        -----     -----      -----
|  #                         Total          15403      6608       8795
|  #   .   .   .   .         Missing            -
+----------------------                     -----
0              2096.212                     15403
(More than 99 unique values)

pcc:                                            Number of Observations
------                                      ------------------------------
                                            Total   Integers   Nonintegers
|  #                         Negative           -         -          -
|  #                         Zero            9835      9835          -
|  #                         Positive        5568      5568          -
|  #                                        -----     -----      -----
|  #                         Total          15403     15403          -
|  #   .   .   .   .         Missing            -
+----------------------                     -----
0                  3369                     15403
(More than 99 unique values)

pcsa:                                           Number of Observations
-------                                     ------------------------------
                                            Total   Integers   Nonintegers
|  #                         Negative           -         -          -
|  #                         Zero            9816      9816          -
|  #                         Positive        5587         1       5586
|  #                                        -----     -----      -----
|  #                         Total          15403      9817       5586
|  #   .   .   .   .         Missing            -
+----------------------                     -----
0              199930.3                     15403
(More than 99 unique values)

cmpg1:                                          Number of Observations
--------                                    ------------------------------
                                            Total   Integers   Nonintegers
|  #                         Negative           -         -          -
|  #                         Zero            8530      8530          -
|  #   #                     Positive        6873      6873          -
|  #   #                                    -----     -----      -----
|  #   #                     Total          15403     15403          -
|  #   #                     Missing            -
+----------------------                     -----
0                     1                     15403
   (2 unique values)

cmpg2:                                          Number of Observations
--------                                    ------------------------------
                                            Total   Integers   Nonintegers
|  #                         Negative           -         -          -
|  #                         Zero           13789     13789          -
|  #                         Positive        1614      1614          -
|  #                                        -----     -----      -----
|  #                         Total          15403     15403          -
|  #   .                     Missing            -
+----------------------                     -----
0                     1                     15403
   (2 unique values)

egmt1:                                          Number of Observations
--------                                    ------------------------------
                                            Total   Integers   Nonintegers
|  #                         Negative           -         -          -
|  #                         Zero           10522     10522          -
|  #                         Positive        4881      4881          -
|  #                                        -----     -----      -----
|  #   #                     Total          15403     15403          -
|  #   #                     Missing            -
+----------------------                     -----
0                     1                     15403
   (2 unique values)

egmt2:                                          Number of Observations
--------                                    ------------------------------
                                            Total   Integers   Nonintegers
|  #                         Negative           -         -          -
|  #                         Zero            9914      9914          -
|  #                         Positive        5489      5489          -
|  #   #                                    -----     -----      -----
|  #   #                     Total          15403     15403          -
|  #   #                     Missing            -
+----------------------                     -----
0                     1                     15403
   (2 unique values)

bnnr1:                                          Number of Observations
--------                                    ------------------------------
                                            Total   Integers   Nonintegers
|  #                         Negative           -         -          -
|  #                         Zero           13600     13600          -
|  #                         Positive        1803      1803          -
|  #                                        -----     -----      -----
|  #                         Total          15403     15403          -
|  #   .                     Missing            -
+----------------------                     -----
0                     1                     15403
   (2 unique values)

bnnr2:                                          Number of Observations
--------                                    ------------------------------
                                            Total   Integers   Nonintegers
|  #                         Negative           -         -          -
|  #                         Zero           12979     12979          -
|  #                         Positive        2424      2424          -
|  #                                        -----     -----      -----
|  #                         Total          15403     15403          -
|  #   #                     Missing            -
+----------------------                     -----
0                     1                     15403
   (2 unique values)

bnnr3:                                          Number of Observations
--------                                    ------------------------------
                                            Total   Integers   Nonintegers
|  #                         Negative           -         -          -
|  #                         Zero           12583     12583          -
|  #                         Positive        2820      2820          -
|  #                                        -----     -----      -----
|  #                         Total          15403     15403          -
|  #   #                     Missing            -
+----------------------                     -----
0                     1                     15403
   (2 unique values)

bnnr4:                                          Number of Observations
--------                                    ------------------------------
                                            Total   Integers   Nonintegers
|  #                         Negative           -         -          -
|  #                         Zero           13504     13504          -
|  #                         Positive        1899      1899          -
|  #                                        -----     -----      -----
|  #                         Total          15403     15403          -
|  #   .                     Missing            -
+----------------------                     -----
0                     1                     15403
   (2 unique values)

bnnr5:                                          Number of Observations
--------                                    ------------------------------
                                            Total   Integers   Nonintegers
|  #                         Negative           -         -          -
|  #                         Zero           14797     14797          -
|  #                         Positive         606       606          -
|  #                                        -----     -----      -----
|  #                         Total          15403     15403          -
|  #   .                     Missing            -
+----------------------                     -----
0                     1                     15403
   (2 unique values)

bnnr6:                                          Number of Observations
--------                                    ------------------------------
                                            Total   Integers   Nonintegers
|  #                         Negative           -         -          -
|  #                         Zero           13051     13051          -
|  #                         Positive        2352      2352          -
|  #                                        -----     -----      -----
|  #                         Total          15403     15403          -
|  #   #                     Missing            -
+----------------------                     -----
0                     1                     15403
   (2 unique values)

bnnr7:                                          Number of Observations
--------                                    ------------------------------
                                            Total   Integers   Nonintegers
|  #                         Negative           -         -          -
|  #                         Zero           12261     12261          -
|  #                         Positive        3142      3142          -
|  #                                        -----     -----      -----
|  #                         Total          15403     15403          -
|  #   #                     Missing            -
+----------------------                     -----
0                     1                     15403
   (2 unique values)

plcmt1:                                         Number of Observations
---------                                   ------------------------------
                                            Total   Integers   Nonintegers
|  #                         Negative           -         -          -
|  #                         Zero           14435     14435          -
|  #                         Positive         968       968          -
|  #                                        -----     -----      -----
|  #                         Total          15403     15403          -
|  #   .                     Missing            -
+----------------------                     -----
0                     1                     15403
   (2 unique values)

plcmt2:                                         Number of Observations
---------                                   ------------------------------
                                            Total   Integers   Nonintegers
|  #                         Negative           -         -          -
|  #                         Zero           11866     11866          -
|  #                         Positive        3537      3537          -
|  #                                        -----     -----      -----
|  #                         Total          15403     15403          -
|  #   #                     Missing            -
+----------------------                     -----
0                     1                     15403
   (2 unique values)

plcmt3:                                         Number of Observations
---------                                   ------------------------------
                                            Total   Integers   Nonintegers
|  #                         Negative           -         -          -
|  #                         Zero           11921     11921          -
|  #                         Positive        3482      3482          -
|  #                                        -----     -----      -----
|  #                         Total          15403     15403          -
|  #   #                     Missing            -
+----------------------                     -----
0                     1                     15403
   (2 unique values)

plcmt4:                                         Number of Observations
---------                                   ------------------------------
                                            Total   Integers   Nonintegers
|  #                         Negative           -         -          -
|  #                         Zero           12899     12899          -
|  #                         Positive        2504      2504          -
|  #                                        -----     -----      -----
|  #                         Total          15403     15403          -
|  #   #                     Missing            -
+----------------------                     -----
0                     1                     15403
   (2 unique values)

plcmt5:                                         Number of Observations
---------                                   ------------------------------
                                            Total   Integers   Nonintegers
|  #                         Negative           -         -          -
|  #                         Zero           10904     10904          -
|  #                         Positive        4499      4499          -
|  #                                        -----     -----      -----
|  #   #                     Total          15403     15403          -
|  #   #                     Missing            -
+----------------------                     -----
0                     1                     15403
   (2 unique values)

. 


```
