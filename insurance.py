# Import the pandas library as pd
import pandas as pd

# Read the CSV file named 'insurance.csv' and store the data in a DataFrame named 'df'
df = pd.read_csv('insurance.csv')

# Print information about the DataFrame, including the number of entries, the number of non-null entries for each column, the column data types, and memory usage
print(df.info())

# Print the unique values in the 'sex' column
print(df['sex'].unique())

# Create a dictionary to map 'sex' values to integers
sex_map = {
    'female': 0,
    'male': 1
}

# Replace the 'sex' column values based on the mapping dictionary
df['sex']=df['sex'].map(sex_map) 

# Create a dictionary to map 'smoker' values to integers
smoker_map = {
    'yes': 1,
    'no': 0
}

# Replace the 'smoker' column values based on the mapping dictionary
df['smoker']=df['smoker'].map(smoker_map)

# Create dummy variables for 'region' column
region_encoded = pd.get_dummies(df['region'], columns=['region'], dtype=int)

# Print the first 5 rows of the encoded 'region' DataFrame
print(region_encoded.head())

# Concatenate the original DataFrame with the encoded 'region' DataFrame
df = pd.concat([df, region_encoded], axis=1)

# Drop the original 'region' column
df = df.drop(['region'], axis=1)

# Print the first 5 rows of the final DataFrame
print(df.head())

# Save the final DataFrame to a new CSV file, without including row indices
df.to_csv('ready_insurance.csv', index=False)