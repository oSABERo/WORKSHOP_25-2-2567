# Import the pandas library as pd
import pandas as pd

# Read the CSV file named 'power.csv' and store the data in a DataFrame named 'df'
df = pd.read_csv('power.csv')

# Drop the 'ts' column from the DataFrame
df = df.drop(['ts'], axis=1)

# Select only the 'irr', 'tamb', 'tmodule', 'wind', and 'pack' columns from the DataFrame
df = df[['irr', 'tamb', 'tmodule', 'wind', 'pack']]

# Print information about the DataFrame, including the number of entries, the number of non-null entries for each column, the column data types, and memory usage
print(df.info())