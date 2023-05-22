# Potentially useful code and some documentation
# Unorganized so far

# How to process data from US EPA gov. 
# 1. Download csv files and merge if necessary
# 2. Delete optional columns like units for PM2.5 is already known
# 3. Sort date column for more accurate time series forecasting
# 4. Use python script to get day of week column 

# Find the AQI on a certain date, useful in determining AQI on holidays
print('Average AQI on July 4:', df[df['Date']=='2022-12-31']['DAILY_AQI_VALUE'].mean())



# Bar plot
# Group the data by 'Day Of Week' and calculate the average AQI for each day
avg_aqi_by_day = df.groupby('Day Of Week')['DAILY_AQI_VALUE'].mean()

# Define the order of the days of the week for proper sorting on the x-axis
weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Create a bar plot using Seaborn
sns.set_style('whitegrid')
#plt.figure(figsize=(10, 6))
sns.barplot(x=weekday_order, y=avg_aqi_by_day)
plt.title('Average AQI by Day of Week')
plt.xlabel('Day of Week')
plt.ylabel('Average AQI')
plt.show()




# Geohash doesn't seem to improve model
!pip install geohash2
import geohash2
from sklearn.preprocessing import LabelEncoder

# Encode the coordinates into geohash
df['geohash'] = df.apply(lambda row: geohash2.encode(row['SITE_LATITUDE'], row['SITE_LONGITUDE']), axis=1)

# Perform label encoding on the 'geohash' column
label_encoder = LabelEncoder()
df['geohash'] = label_encoder.fit_transform(df['geohash'])
