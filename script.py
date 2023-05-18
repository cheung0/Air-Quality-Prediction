# Python script that adds a new column for the day of the week and overwrites original csv file
# Make sure to change csv file name

# Convert the "Date" column to datetime format
df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y")

# Add a new column for the day of the week
df["Day Of Week"] = df["Date"].dt.day_name()

# Save the modified DataFrame to a new CSV file
df.to_csv("/California Air Quality.csv", index=False)

