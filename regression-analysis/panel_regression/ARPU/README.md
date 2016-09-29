## ARPU - Estimating Average Revenue Per User in a given timeframe
- ARPU = Total Revenue / Total # of Installs
- # of Active Users = Total # of Installs * Retention%<sup>[1](#myfootnote1)</sup>
- Total Revenue = Total # of Installs * Retention% * Estimated Average Revenue Per User


#### Assumptions
in a given timeframe
- # of installs is constant
- Retention rate is constant
- All users are active
- The main source of disposable income comes from salary
 
 
#### Model
Based on the above assumptions, we can now only consider factors that influence buying behavior.
- Estimated Revenue Per User = Income level (continuous) + Gender (categorical) + Age group (categorical) [(16-24),
(25-34), (35-44), (45-54), (55-64), 65 +] + Marital status (categorical) + Occupation (categorical) + Education level (categorical) + Geographical location (categorical) + Devices (categorical) + Frequencies of use of mobile (continuous) + Sessions duration (continuous) + Disposable income multiplier (continuous; accumulative spending / income)


#### Reference
<a name="myfootnote1">[1]</a>: [Survival Analysis in Python](https://github.com/CamDavidsonPilon/lifelines)
