#### gs = -3.94cmpg1 - 6.92cmpg2 - 5.84egmt1 + 0.03egmt2 + 6.04bnnr1 - 0.06bnnr2 + 5.46bnnr3 - 4.35bnnr4 - 11.29bnnr5 + 4.15bnnr6 + 6.56bnnr7 - 0.54plcmt1 + 3.47plcmt2 - 4.23plcmt3 + 3.23plcmt4 + 6.54plcmt5 + 0.23click - 0.06cmpg1click - 0.17cmpg2click
* gross profit = revenue - cost

## Campaign: set by BurritosOnline to segment users
* User Engagement: level of engagement of the users
* Banner: size of the ad served by Criteo
* Placement: publisher space where the ad is served by Criteo
* Displays: number of ads served by Criteo
* Cost: Price paid by Criteo to serve the ads
* Clicks: number of ads clicked by the users
* Revenue: Price paid by BurritosOnline for the clicks generated 
* Post Click Conversions: On-site transactions that happened in the next 30 days after a click
* Post Click Sales Amount: Amount of the on-site transactions that happened in the next 30 days after a click

## Categorical Variables
* cmpg1 = Campaign1
* cmpg2 = Campaign2
* egmt1 = High
* egmt2 = Medium
* bnnr1 = 160 x 600
* bnnr2 = 240 x 400
* bnnr3 = 300 x 250
* bnnr4 = 468 x 60
* bnnr5 = 580 x 400
* bnnr6 = 670 x 90
* bnnr7 = 728 x 90
* plcmt1 = abc
* plcmt2 = def
* plcmt3 = ghi
* plcmt4 = jkl
* plcmt5 = mno
* cmpg1click = cmpg1 * click
* cmpg2click = cmpg2 * click

### Summary

```stata
 reg gs cmpg1 cmpg2 egmt1 egmt2 bnnr1 bnnr2 bnnr3 bnnr4 bnnr5 bnnr6 bnnr7 plcmt1 
> plcmt2 plcmt3 plcmt4 plcmt5 display click cmpg1click cmpg2click

      Source |       SS       df       MS              Number of obs =   15403
-------------+------------------------------           F( 20, 15382) = 6562.34
       Model |  65455005.6    20  3272750.28           Prob > F      =  0.0000
    Residual |  7671268.21 15382  498.717216           R-squared     =  0.8951
-------------+------------------------------           Adj R-squared =  0.8950
       Total |  73126273.8 15402  4747.84274           Root MSE      =  22.332

------------------------------------------------------------------------------
          gs |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
       cmpg1 |  -3.944657   .4144107    -9.52   0.000    -4.756951   -3.132363
       cmpg2 |   6.918291    .692035    10.00   0.000      5.56182    8.274761
       egmt1 |  -5.842452   .4841314   -12.07   0.000    -6.791407   -4.893497
       egmt2 |    .032601   .4517561     0.07   0.942    -.8528945    .9180964
       bnnr1 |   6.041952   1.361819     4.44   0.000     3.372626    8.711278
       bnnr2 |  -.0640657   1.343279    -0.05   0.962    -2.697051     2.56892
       bnnr3 |   5.455461    1.34367     4.06   0.000     2.821709    8.089213
       bnnr4 |   4.353542   1.330758     3.27   0.001     1.745099    6.961986
       bnnr5 |  -11.29322    1.50229    -7.52   0.000    -14.23789   -8.348559
       bnnr6 |   4.153138   1.322446     3.14   0.002     1.560988    6.745289
       bnnr7 |   6.564524   1.348625     4.87   0.000      3.92106    9.207989
      plcmt1 |   .5427908   1.338995     0.41   0.685    -2.081798    3.167379
      plcmt2 |   3.472562   1.220494     2.85   0.004     1.080251    5.864874
      plcmt3 |  -4.225428   1.222239    -3.46   0.001     -6.62116   -1.829696
      plcmt4 |    3.23312   1.234373     2.62   0.009     .8136023    5.652638
      plcmt5 |   6.539862   1.262572     5.18   0.000     4.065071    9.014652
     display |   -.000945   8.06e-06  -117.18   0.000    -.0009608   -.0009292
       click |   .2257284   .0050104    45.05   0.000     .2159075    .2355493
  cmpg1click |  -.0561559   .0049258   -11.40   0.000     -.065811   -.0465009
  cmpg2click |   -.174374   .0049495   -35.23   0.000    -.1840757   -.1646724
       _cons |  -3.392832   1.793437    -1.89   0.059    -6.908182     .122517
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
