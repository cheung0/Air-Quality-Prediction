# Predicting-Air-Quality
## Intro

We all have fundamental needs, such as food, water, love, and clean air. Practical takeaway from my findings if you live in the Bay Area like I do: air quality is better on weekends. You might want to open your windows for fresh air on Saturdays and Sundays. Another takeway is that the opposite is true when you factor in more data points from around California. I'm not entirely sure why that is. I trained a linear regression and decision tree machine learning algorithm to predict the AQI based on the amount of PM2.5 and the day of week. The decision tree model has the best performance, with an MSE (Mean Squared Error) of 0.10 on the test set. This is my data science / machine learning project exploration on air quality.

## Graph of Results for California
![Screenshot 2023-05-10 at 6 28 12 PM](https://github.com/cheung0/Predicting-Air-Quality/assets/56772737/29eeddd8-10bc-4110-9357-0af9d621f8ed)

![Screenshot 2023-05-10 at 6 28 41 PM](https://github.com/cheung0/Predicting-Air-Quality/assets/56772737/9eab993d-5f01-4504-b49b-21b6842feaeb)

![Screenshot 2023-05-10 at 5 00 56 PM](https://github.com/cheung0/Predicting-Air-Quality/assets/56772737/f0c47c7d-c950-43a7-8feb-1e7743f24a1a)

## Graph of Results for the Bay Area
![Screenshot 2023-05-10 at 2 28 20 AM](https://github.com/cheung0/Predicting-Air-Quality/assets/56772737/00fdc0e1-6299-44a0-b6c0-77e874364f68)

## Analysis for the Bay Area
I analyzed 1678 data samples from air quality sensor data around the Bay Area during 2023. Some factors that play a role in air quality include: traffic, industrial activity, and environmental factors. For Alameda County specifically, the average AQI for weekends was 23 (0 - 50 is a good AQI) and the average for weekdays 23.6. My sample size wasn't big enough, so I analyzed again with data from all the Bay Area. The average AQI for weekends was 22.38 and the average for weekdays 23.15. A 0.6 and a 0.77 difference. Then I looked at the data for PM 2.5 μg/m3 levels. I noticed that weekends were slightly higher, by 0.16, on avgerage. Again, a small difference appears, but if you use this knowledge and apply it over the span of thousands of days, it can make a big difference in your health and well being.

## Analysis for California
I analyzed 128,077 data samples from air quality sensor data around California during 2023. I found out that the average AQI for weekdays was 34.07 and for weekends 34.84. 


## Machine Learning on California Air Quality
### Data Engineering
I normalized Air Quality and PM2.5, one hot encoded day of week, and deleted the other columns that do not play a role in predicting air quality, such as site longitude / latitude, side id, etc. 

### Decision Tree
![Screenshot 2023-05-14 at 4 32 53 PM](https://github.com/cheung0/Predicting-Air-Quality/assets/56772737/a48765c0-0014-442a-a3d1-256bfa2aec13)


![Screenshot 2023-05-14 at 4 06 14 PM](https://github.com/cheung0/Predicting-Air-Quality/assets/56772737/d1302b24-eb54-4a0c-b16e-7b748bedbb3b)


### Linear Regression
I trained a linear regression model to predict the AQI based on input with PM2.5 and the day of week. This is useful because day of week and PM2.5 is correlated with air quality and PM2.5 sensors are cheaper than more expensive sensors that collect Ozone, PM2.5, PM10, CO, SO2, and NO2 data. Based on the evaluation metrics for the train and test sets, the model seems to be performing reasonably well for AQI prediction.

![Screenshot 2023-05-11 at 3 43 14 AM](https://github.com/cheung0/Predicting-Air-Quality/assets/56772737/f2117fa5-e5c1-439a-b646-8a576f6f4dd2)

## Analysis for Alameda County
Graph of weekend vs weekday data without outliers.

<img width="577" alt="Screen Shot 2023-05-11 at 1 53 06 PM" src="https://github.com/cheung0/Predicting-Air-Quality/assets/56772737/37a9fde5-6761-42a8-be00-af3f7e2795d8">

## Conclusion

The small, individual actions of each and every single one of us can cause big, large actions in the environment. I acknowledge that my analysis might be wrong and the data from the US EPA gov website does attach a disclaimer that some data may be inaccurate and should not be used for governmental advisory. Nontheless, I still learned a lot about data science.
