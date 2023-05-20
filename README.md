# Predicting Air Quality
## Intro
We all have fundamental needs, such as food, water, love, and clean air. Practical takeaway from my findings if you live in the Bay Area like I do: air quality is better on weekends. You might want to open your windows for fresh air on Saturdays and Sundays. Another takeway is that the opposite is true when you factor in more data points from around California. I'm not entirely sure why that is. I trained a linear regression and decision tree machine learning algorithm to predict the AQI based on the amount of PM2.5 and the day of week. This is useful because day of week and PM2.5 is correlated with air quality and PM2.5 sensors are cheaper than more expensive sensors that collect Ozone, PM2.5, PM10, CO, SO2, and NO2 data. The decision tree model has the best performance, with an MSE (Mean Squared Error) of 0.10 on the test set. This is my personal project on air quality with Machine Learning. 
The objective is to train a machine learning model to predict the AQI based on PM2.5, day of week, date, and it would be location dependent. This could potentially be useful for forecasting the AQI.

## Practical Things You Can Do
My research shows that weekends in the Bay Area and Los Angeles have significantly better air quality. California, in general, too. I’m hypothesizing that it’s because of less work, there's less traffic and less industrial emissions. 

## Business Plan for Device
I asked chat GPT to write it up, but it was too long. So the elevator pitch is: We are gonna sell air quality sensors that are a lot cheaper and better quality than existing sensors because of our unique machine learning algorithm. If you still want to see the business plan, I'll send you the chat GPT response. High quality AQI sensors cost $800 to $3000. Most of the world, including developed countries and cities, cannot afford that. Our high quality air quality sensor costs only $197, which is 4 x cheaper than high quality AQI sensors. As for our standard air quality sensor? It only costs $40. The costs associated with the AQI sensor depends on the PM2.5 sensor quality (high quality or standard) and the Machine Learning microcontroller. 

Sales infographic below (inspired by Costco's coconut water):
Air Quality Sensor?
Why?
Informs you if you should open windows or wear mask outside for your health.
Uses Machine Learning, the technology of the future, to help you.

## Exploratory Data Analysis
### Los Angeles
![Screenshot 2023-05-19 at 1 59 40 AM](https://github.com/cheung0/California-Air-Quality-Prediction/assets/56772737/98bbd6a7-ff94-4d8f-8b2d-ed256529800f)

![Screenshot 2023-05-19 at 2 05 33 AM](https://github.com/cheung0/California-Air-Quality-Prediction/assets/56772737/44825c1d-b968-4ebc-96e9-d0eabfe79dff)

![Screenshot 2023-05-19 at 2 06 33 AM](https://github.com/cheung0/California-Air-Quality-Prediction/assets/56772737/5d4f47e5-24be-431c-b842-f18367ba1b2e)

![Screenshot 2023-05-19 at 2 07 00 AM](https://github.com/cheung0/California-Air-Quality-Prediction/assets/56772737/01110808-0741-4f91-873b-05e6fcf36ce0)

![Screenshot 2023-05-19 at 2 07 16 AM](https://github.com/cheung0/California-Air-Quality-Prediction/assets/56772737/1359b359-25e7-4628-93d1-22e2d20cc083)

![Screenshot 2023-05-19 at 2 07 28 AM](https://github.com/cheung0/California-Air-Quality-Prediction/assets/56772737/de11b047-ebb5-4d58-b2ac-e47d83b3398b)

![Screenshot 2023-05-19 at 2 07 47 AM](https://github.com/cheung0/California-Air-Quality-Prediction/assets/56772737/c91c4706-1bd7-4a14-aaa0-4d14386ce499)

![Screenshot 2023-05-19 at 2 13 47 AM](https://github.com/cheung0/California-Air-Quality-Prediction/assets/56772737/4c2ae099-f712-44cd-884e-4a5e07bbe2a6)

![Screenshot 2023-05-19 at 2 13 55 AM](https://github.com/cheung0/California-Air-Quality-Prediction/assets/56772737/5786f6c2-d9b0-484f-825a-1fb1ef785a14)

### California
![Screenshot 2023-05-19 at 2 20 43 AM](https://github.com/cheung0/California-Air-Quality-Prediction/assets/56772737/00117c1b-ccd1-4292-902e-85651ab6b7f8)

![Screenshot 2023-05-19 at 2 21 22 AM](https://github.com/cheung0/California-Air-Quality-Prediction/assets/56772737/98391515-1309-48f9-b561-891977e40282)

![Screenshot 2023-05-19 at 2 24 22 AM](https://github.com/cheung0/California-Air-Quality-Prediction/assets/56772737/1c63fb7e-2b72-42c2-bf62-8e8e447351a3)

![Screenshot 2023-05-19 at 2 25 56 AM](https://github.com/cheung0/California-Air-Quality-Prediction/assets/56772737/60c3df85-4ca6-4ea6-85d6-ef8b65b75c4f)

![Screenshot 2023-05-19 at 2 26 22 AM](https://github.com/cheung0/California-Air-Quality-Prediction/assets/56772737/0b53d20b-8b9e-4661-a6b0-5212fe5f1eea)

![Screenshot 2023-05-19 at 2 29 01 AM](https://github.com/cheung0/California-Air-Quality-Prediction/assets/56772737/95fb1898-0093-4b65-a719-5b2630d45ccc)

![Screenshot 2023-05-19 at 2 29 24 AM](https://github.com/cheung0/California-Air-Quality-Prediction/assets/56772737/3b5e69c7-092b-44b7-a550-32c425cd55d0)

![Screenshot 2023-05-19 at 2 29 37 AM](https://github.com/cheung0/California-Air-Quality-Prediction/assets/56772737/1d392efa-0ad3-485d-b80d-6c84a9bda3a0)

## The Bay Area

## Analysis for the Bay Area
I analyzed 1678 data samples from air quality sensor data around the Bay Area during 2023. Some factors that play a role in air quality include: traffic, industrial activity, and environmental factors. For Alameda County specifically, the average AQI for weekends was 23 (0 - 50 is a good AQI) and the average for weekdays 23.6. My sample size wasn't big enough, so I analyzed again with data from all the Bay Area. The average AQI for weekends was 22.38 and the average for weekdays 23.15. A 0.6 and a 0.77 difference. Then I looked at the data for PM 2.5 μg/m3 levels. I noticed that weekends were slightly higher, by 0.16, on average. Again, a small difference appears, but if you use this knowledge and apply it over the span of thousands of days, it can make a big difference in your health and well being.

## Analysis for California



## Machine Learning on California Air Quality 
### Time Series and XGBoost Tree
![Screenshot 2023-05-20 at 1 06 24 AM](https://github.com/cheung0/California-Air-Quality-Prediction/assets/56772737/d2d4eaf9-913b-490b-aa5d-09e2ea32a808)








### Time Series 
Not working yet. I'm thinking of using an XGBoost model on top of a linear regression time series forecasting prediction model. 
![Screenshot 2023-05-19 at 2 18 27 AM](https://github.com/cheung0/California-Air-Quality-Prediction/assets/56772737/868238d6-1198-4417-86aa-c8fc76e79764)


### Data Engineering
I normalized Air Quality and PM2.5, one hot encoded day of week, and deleted the other columns that do not play a role in predicting air quality, such as site longitude / latitude, side id, etc. 


### Decision Tree
![Screenshot 2023-05-14 at 4 32 53 PM](https://github.com/cheung0/Predicting-Air-Quality/assets/56772737/a48765c0-0014-442a-a3d1-256bfa2aec13)

![Screenshot 2023-05-15 at 1 30 10 AM](https://github.com/cheung0/Predicting-Air-Quality/assets/56772737/931078c0-34b2-477e-ad98-8aac663ef923)


### Linear Regression

![Screenshot 2023-05-11 at 3 43 14 AM](https://github.com/cheung0/Predicting-Air-Quality/assets/56772737/f2117fa5-e5c1-439a-b646-8a576f6f4dd2)

### Ideas
XGBoost can be effective for time series prediction, there are other specialized models and techniques specifically designed for time series forecasting, such as autoregressive integrated moving average (ARIMA), recurrent neural networks (RNNs), or long short-term memory (LSTM) networks. Depending on the specific characteristics and complexity of your time series data, these models may provide better performance.
Linear regression, 
XGBoost, ARIMA, Prophet, RNN, LSTM, FML


## Story
I remember the day the Bay Area sky turned into a thick, purple, smog. I remember stepping out of my home and choking on the very air I was breathing. Air quality is definitely a problem we as a society need to solve. 

## Conclusion

I acknowledge that my analysis might be wrong and the data from the US EPA gov website does attach a disclaimer that some data may be inaccurate and should not be used for governmental advisory. Nontheless, I still learned a lot about data science.


