import pandas as pd

# Load the data
df = pd.read_csv('../data/weather_data.csv')

# Inspect the data
print("Data Info:")
print(df.info())
print("\nMissing Values:")
print(df.isnull().sum())
print("\nSummary Statistics:")
print(df.describe())

# Handle missing values (example: fill with mean)
df['TMAX'] = df['TMAX'].fillna(df['TMAX'].mean())
df['TMIN'] = df['TMIN'].fillna(df['TMIN'].mean())
df['PRCP'] = df['PRCP'].fillna(0)  # Assuming 0 for no precipitation

# Convert date column to datetime (assuming a 'DATE' column)
df['DATE'] = pd.to_datetime(df['DATE'])

# Save the cleaned data
df.to_csv('../data/cleaned_weather_data.csv', index=False)
print("\nCleaned data saved to data/cleaned_weather_data.csv")