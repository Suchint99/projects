import pandas as pd

# Load the dataset


# Display the first few rows of the dataset
print("Dataset preview:")
print(df.head())

# Summary of the dataset
print("\nDataset information:")
print(df.info())

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Basic statistics for numeric columns
print("\nBasic statistics:")
print(df.describe())

# Calculate average sleep duration if 'Sleep Duration' column is present
if 'Sleep Duration' in df.columns:
    average_sleep = df['Sleep Duration'].mean()
    print(f"\nAverage sleep duration: {average_sleep:.2f} hours")

# Example of correlation analysis with other factors, if columns are available
if 'Sleep Duration' in df.columns and 'Physical Activity' in df.columns:
    correlation = df['Sleep Duration'].corr(df['Physical Activity'])
    print(f"\nCorrelation between sleep duration and physical activity: {correlation:.2f}")
