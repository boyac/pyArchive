##### Description
- In the case of Japan.

##### Predictor Variables
- married female employees with kid(s)
- //*The reason for picking the variable as expected variable since women tend to leave work after having children.
Thus, married female employees with kid(s) can see as a proxy to learn what factors will be helpful to keep female employees stay at their corporate positions after having kids.*//

##### Predicted Variables
- tax incentives/marital status (0/1): if spouses' annual income below ￥1.03 million yen, tax reduction of ￥380,000
- salary level: on average, female employees' salary of women are lower than male counterparts by 30.2%
- managerial position ratio (0/1): among private companies, female only accounts 11% of its managerial positions
- cultural reform_internal/companies' nations (US:0, European:1, Asia:2): transparent opportunity for promotion, equal importance of responsiblities assigned
- cultural reform_external: reform seniority and diversity
- support_internal: promote flexible working hours, places and make it easy to kindergarden schedule and nursury, materity leaves
- support_external (ratio of cost/salary): loose domestic helper regulations, such as affordatbility
- employment_type (0/1): full-time, dispatch worker

##### Model
- ln(p/(1-p)) = Marital_Status(0/1) + Salary + Managerial_Position(0/1) + Cultural(categorical_var) + Flexible_Hour(0/1) + Flexible_WorkPlace(0/1) + Number_Daycare + Daycare_center_30mins(0/1) + Employment_type(0/1) + Domestic_Helper_Affordability(Ratio Cost/Salary) 
