#### gs = -7.41cmpg1 - 13.22cmpg2 - 9.59egmt1 + 0.35egmt2 + 5.73bnnr1 + 0.90bnnr2 + 3.30bnnr3 + 2.95bnnr4 - 12.08bnnr5 + 2.53bnnr6 + 4.44bnnr7 - 0.19plcmt1 + 2.50plcmt2 -4.21plcmt3 + 1.84plcmt4 + 4.48plcmt5 + 0.07click + 0.08pcc
* gross profit = revenue - cost

 Campaign: set by BurritosOnline to segment users
* User Engagement: level of engagement of the users
* Banner: size of the ad served by Criteo
* Placement: publisher space where the ad is served by Criteo
* Displays: number of ads served by Criteo
* Cost: Price paid by Criteo to serve the ads
* Clicks: number of ads clicked by the users
* Revenue: Price paid by BurritosOnline for the clicks generated 
* Post Click Conversions: On-site transactions that happened in the next 30 days after a click
* Post Click Sales Amount: Amount of the on-site transactions that happened in the next 30 days after a click

categorical variables
cmpg1 = Campaign1
cmpg2 = Campaign2
egmt1 = High
egmt2 = Medium
bnnr1 = 160 x 600
bnnr2 = 240 x 400
bnnr3 = 300 x 250
bnnr4 = 468 x 60
bnnr5 = 580 x 400
bnnr6 = 670 x 90
bnnr7 = 728 x 90
plcmt1 = abc
plcmt2 = def
plcmt3 = ghi
plcmt4 = jkl
plcmt5 = mno

### Summary

```stata
 reg gs cmpg1 cmpg2 egmt1 egmt2 bnnr1 bnnr2 bnnr3 bnnr4 bnnr5 bnnr6 bnnr7 plcmt1 plcmt2 plcmt3 plcmt4 plcmt5 display cl
> ick cmpg1click cmpg2click pcc pcsa

      Source |       SS       df       MS              Number of obs =   15403
-------------+------------------------------           F( 22, 15380) =11088.39
       Model |  68789306.2    22  3126786.65           Prob > F      =  0.0000
    Residual |  4336967.56 15380  281.987488           R-squared     =  0.9407
-------------+------------------------------           Adj R-squared =  0.9406
       Total |  73126273.8 15402  4747.84274           Root MSE      =  16.792

------------------------------------------------------------------------------
          gs |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
       cmpg1 |  -2.621046   .3118786    -8.40   0.000    -3.232365   -2.009728
       cmpg2 |    4.52718   .5208904     8.69   0.000     3.506173    5.548187
       egmt1 |  -2.634566     .36528    -7.21   0.000    -3.350558   -1.918574
       egmt2 |  -1.593112   .3400345    -4.69   0.000     -2.25962   -.9266041
       bnnr1 |   1.235643    1.02497     1.21   0.228      -.77342    3.244706
       bnnr2 |  -2.317703   1.010357    -2.29   0.022    -4.298123   -.3372834
       bnnr3 |   1.946418   1.011121     1.93   0.054    -.0354999    3.928335
       bnnr4 |   1.547997   1.001011     1.55   0.122    -.4141041    3.510097
       bnnr5 |  -5.347867   1.131116    -4.73   0.000    -7.564988   -3.130746
       bnnr6 |   1.050176   .9948337     1.06   0.291    -.8998157    3.000168
       bnnr7 |   1.377246   1.015252     1.36   0.175    -.6127688     3.36726
      plcmt1 |  -.1368135   1.006944    -0.14   0.892    -2.110543    1.836916
      plcmt2 |   .6121289   .9182078     0.67   0.505    -1.187667    2.411925
      plcmt3 |  -2.723683   .9193441    -2.96   0.003    -4.525706     -.92166
      plcmt4 |   1.623967   .9283749     1.75   0.080    -.1957579    3.443691
      plcmt5 |   1.305169   .9506276     1.37   0.170    -.5581733    3.168512
     display |  -.0005595   7.05e-06   -79.35   0.000    -.0005733   -.0005456
       click |   .1591175   .0038185    41.67   0.000     .1516329    .1666021
  cmpg1click |   .0744177   .0039007    19.08   0.000      .066772    .0820635
  cmpg2click |  -.1158428   .0037635   -30.78   0.000    -.1232197   -.1084659
         pcc |  -.2403804   .0053194   -45.19   0.000    -.2508071   -.2299537
        pcsa |   .0000375   .0001073     0.35   0.727    -.0001729    .0002479
       _cons |   .7806625    1.34913     0.58   0.563    -1.863791    3.425116
------------------------------------------------------------------------------
```

#### inspect
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
