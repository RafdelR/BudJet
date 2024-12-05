import pandas as pd

# Sample data: Total per month per bank
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June'],
    'Bank1': [1000, 1050, 1100, 1080, 1120, 1150],
    'Bank2': [1500, 1520, 1550, 1530, 1580, 1600],
    'Investment1': [2000, 2100, 2200, 2150, 2250, 2300],
    'Investment2': [2500, 2600, 2550, 2620, 2700, 2750],
    'Investment3': [3000, 3100, 3200, 3150, 3250, 3300],
    'Savings': [500, 530, 560, 550, 580, 600],
}

# Create a DataFrame from your data
df = pd.DataFrame(data)

# Set 'Month' as the index
df.set_index('Month', inplace=True)

# Calculate the total amount per month by summing across the accounts
df['Total'] = df.sum(axis=1)

# Calculate the percentage change from the previous month
df['% Change'] = df['Total'].pct_change() * 100

df['% Change'] = df['% Change'].fillna(0)

# Format the percentage change to two decimal places
df['% Change'] = df['% Change'].round(2)

# Display the DataFrame
print(df)
