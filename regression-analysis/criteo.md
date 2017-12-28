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

```stata
 reg gs cmpg1 cmpg2 egmt1 egmt2 bnnr1 bnnr2 bnnr3 bnnr4 bnnr5 bnnr6 bnnr7 plcmt1 plcmt2 plcmt3 plcmt4 plcmt5 display click pcc pcsa

      Source |       SS       df       MS              Number of obs =   15403
-------------+------------------------------           F( 20, 15382) = 1864.87
       Model |  51773941.8    20  2588697.09           Prob > F      =  0.0000
    Residual |    21352332 15382  1388.13756           R-squared     =  0.7080
-------------+------------------------------           Adj R-squared =  0.7076
       Total |  73126273.8 15402  4747.84274           Root MSE      =  37.258

------------------------------------------------------------------------------
          gs |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
       cmpg1 |  -7.412024   .6503593   -11.40   0.000    -8.686805   -6.137243
       cmpg2 |  -13.21711   1.110309   -11.90   0.000    -15.39345   -11.04077
       egmt1 |  -9.587029   .8080048   -11.87   0.000    -11.17081   -8.003244
       egmt2 |   .3530195   .7414629     0.48   0.634    -1.100336    1.806374
       bnnr1 |   5.731244   2.263983     2.53   0.011     1.293571    10.16892
       bnnr2 |   .8988081   2.228316     0.40   0.687    -3.468955    5.266571
       bnnr3 |   3.296005   2.228804     1.48   0.139    -1.072714    7.664725
       bnnr4 |   2.945652   2.219021     1.33   0.184    -1.403891    7.295195
       bnnr5 |  -12.08462   2.490843    -4.85   0.000    -16.96696   -7.202268
       bnnr6 |   2.531137   2.204377     1.15   0.251    -1.789701    6.851976
       bnnr7 |   4.442101    2.24376     1.98   0.048     .0440665    8.840136
      plcmt1 |  -.1864358   2.234049    -0.08   0.933    -4.565435    4.192563
      plcmt2 |   2.496886   2.035796     1.23   0.220    -1.493515    6.487288
      plcmt3 |  -4.207668   2.036922    -2.07   0.039    -8.200275   -.2150601
      plcmt4 |   1.842779   2.059578     0.89   0.371    -2.194238    5.879796
      plcmt5 |   4.478166   2.098946     2.13   0.033     .3639825    8.592349
     display |  -.0009149   .0000147   -62.14   0.000    -.0009437    -.000886
       click |   .0722916   .0007278    99.33   0.000     .0708651    .0737181
         pcc |   .0831074   .0114167     7.28   0.000     .0607293    .1054855
        pcsa |   .0025041   .0002368    10.58   0.000       .00204    .0029683
       _cons |   4.013357   2.990576     1.34   0.180    -1.848526     9.87524
------------------------------------------------------------------------------

. 
. 


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
