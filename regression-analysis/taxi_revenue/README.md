#### How would change the starting fee of taxi ride will affect the sales?
- I just saw a news of テレビ東京, said the taxi industry is discussing changing the start fee from 730 yen to 400 yen.
- As a consumer and who favours riding a taxi most of the time, I am more than delight to learn the news.
- However, what makes me like the country so much is its stability and social system.
- The dramatic change of the fee will definitely impact the volumes and thus the life of the cap drivers.
- I am also curious how do they decide to impose the fee from 730 yen to 400 yen, which is an almost 50% off (around 45% off).

#### Assumptions
- The drop in the starting fee will attract new passengers
- The final revenue will be increased due to the increase of passengers

#### Model
- in order to predict the sales, we need to predict the multipers caused by the starting price drop
- Number of customers = a + b1*kilometer_per_ride* + b2*starting_fee* + b3*weather_condition* + b4*drivers_working_hours* + (b5*rout_covered*)
