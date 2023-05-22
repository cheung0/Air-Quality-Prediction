# Predicting Air Quality
## Intro

I trained an XG Boost Regressor Tree model on predicting AQI based on feature variables relating to: PM2.5 concentration, distance as measured by the Haversine formula, location, and date. Currently, the model is trained on Los Angeles Air Quality data from 2010 - 2022 and produces highly accurate results.

This is useful because PM2.5, location, date, etc. can predict air quality and PM2.5 sensors are cheaper than more expensive sensors that collect Ozone, PM2.5, PM10, CO, SO2, and NO2 data. The XGBoost Regressor model has the best performance with an MSE (Mean Squared Error) of 0.003 and an R2 score of 0.99 on the test set. This is my personal project on air quality with Machine Learning. 

## Practical Things You Can Do
We all have fundamental needs, such as food, water, and clean air. In the 2022 data, the data suggests that weekends in the Bay Area and Los Angeles have better air quality. California, in general, too. I’m hypothesizing that it’s because of less work, there's less traffic and less industrial emissions.

Practical takeaway from my findings if you live in the Bay Area like I do: air quality is better on weekends. You might want to open your windows for fresh air on Saturdays and Sundays. 


## Business Plan for Device
We are gonna sell air quality sensors that are a lot cheaper and better quality than existing sensors.

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

## Los Angeles Analysis
Notes:
2010 - 2022 csv file LA data
54347 data points, probably big enough?
XGBoost 
Linear Regression 
2023 as additional test set, graph compare with predict, find out good features

Using a time series forecasting perspective, the data fluctuates and shows signs of patterns and trends. The date can be used as a feature variable. The AQI and PM2.5 concentration on weekends is lower than weekdays, showing us that we can use day of week as a feature variable. PM2.5 has a 0.88 correlation with AQI because PM2.5 is one of the 5 particulate matters used to calculate AQI, so PM2.5 is a feature variable as well.

## Machine Learning on California Air Quality 
### Time Series and XGBoost Tree
![Screenshot 2023-05-20 at 1 58 47 AM](https://github.com/cheung0/California-Air-Quality-Prediction/assets/56772737/526b1724-f5ff-48e6-b0ef-bb257145a995)

One hot encoding is good in general, but not for day of week in this case. 

I used the Haversine formula to calculate the distance between two places with longitudes and latitudes. The first place being the center of LA and the second being the data point. 

![Screenshot 2023-05-21 at 1 58 49 AM](https://github.com/cheung0/California-Air-Quality-Prediction/assets/56772737/e98c870f-462a-4718-93ee-ee76a166d80c)

![Screenshot 2023-05-21 at 1 59 00 AM](https://github.com/cheung0/California-Air-Quality-Prediction/assets/56772737/c1257a7e-babb-4efa-9ab2-250a97e6c2a0)

Without PM2.5 in the model:
Angular distance, site location, date, and holiday seem to be moderately important features.

![Screenshot 2023-05-21 at 2 00 51 AM](https://github.com/cheung0/California-Air-Quality-Prediction/assets/56772737/ef8bc622-6f6e-4df7-9b8e-10d689ac4fc9)

![Screenshot 2023-05-21 at 2 07 01 AM](https://github.com/cheung0/California-Air-Quality-Prediction/assets/56772737/cc4873ef-d974-40c2-bb25-9585a50d1b5c)

With only PM2.5:
PM2.5 seems to be able to explain AQI extremely well. The error metrics are close to 0, with mean absolute error being around 0.003. 
![Screenshot 2023-05-21 at 2 09 10 AM](https://github.com/cheung0/California-Air-Quality-Prediction/assets/56772737/457b235c-76ef-4ab6-93b1-8b5ccd922d3b)

With only year:
Years are values from 2010 - 2022. I wanted to see if my model was actually using the other features to predict AQI and it is.
![Screenshot 2023-05-21 at 2 13 15 AM](https://github.com/cheung0/California-Air-Quality-Prediction/assets/56772737/601edf21-8b8a-427d-aed0-05790804364a)

### Ideas
Potential Models: Linear regression, XGBoost, ARIMA, Prophet, RNN, LSTM, etc. Currently, Sklearn is being used. Tensorflow may be helpful.

### ARIMA Time Series Forecasting Model
![Screenshot 2023-05-21 at 2 23 32 AM](https://github.com/cheung0/California-Air-Quality-Prediction/assets/56772737/4b8a1e09-729d-4057-a743-3663ac8779a6)


## Story
I remember the day the Bay Area sky turned into a thick, purple, smog. I remember stepping out of my home and choking on the very air I was breathing. Air quality is definitely a problem we as a society need to solve. My hope is that with Machine Learning, we can get better and more accurate air quality sensor readings. We already know that our weather forecasts are very good, but whether or not its raining doesn't significantly impact our lives. But knowing whether or not we are breathing hazardous chemicals in our lungs does. 


## Conclusion

I acknowledge that my analysis might be wrong and the data from the US EPA gov website does attach a disclaimer that some data may be inaccurate and should not be used for governmental advisory. Nontheless, I still learned a lot about data science.

## Sources
![Screenshot 2023-05-21 at 2 33 14 AM](https://github.com/cheung0/California-Air-Quality-Prediction/assets/56772737/363979a0-bdf7-430e-a394-75ca1bd27aa6)

"Angular distance gives info about the circular nature of weeks and the actual distance between the days."
https://www.mikulskibartosz.name/time-in-machine-learning/

Andrew Ng's Machine Learning course

google and chat gpt
