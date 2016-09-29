## ARPU - Estimating Average Revenue Per User in a given timeframe
- ARPU = Total Revenue / Total # of Subscribers
- Total Revenue = Total # of Subscribers * Retention Rate<sup>[1](#Survival Analysis)</sup> * Predicted Daily Revenue per User * Estimated # of Days

#### Assumptions:
in a given timeframe
- # of installs is constant
- Retention rate is constant
- All users are active
- The main source of disposable income comes from salary
 
 
#### Model
- Predicted Daily Revenue per User = Income level (continuous) + Gender (categorical) + Age group (categorical) [(16-24),
(25-34), (35-44), (45-54), (55-64), 65 +] + Marital status (categorical) + Occupation (categorical) + Education level (categorical) + Geographical location (categorical) + Devices (categorical) + Frequencies of use of mobile (continuous) + Sessions duration (continuous) + Disposable income multiplier (continuous; accumulative spending / income)


#### Reference
<a name="Survival Analysis">1</a>: [Survival Analysis in Python](https://github.com/CamDavidsonPilon/lifelines)
