# WORKSHOP_25-2-2567
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

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Import the pandas library as pd
    import pandas as pd

# Read the CSV file named '50_Startups.csv' and store the data in a DataFrame named 'df'
    df = pd.read_csv('50_Startups.csv')

# Print the statistical summary of the DataFrame
    print(df.describe())

# Group the DataFrame by 'State' and iterate over each group
    states_df = df.groupby('State')
    for state, state_df in states_df:
        # Print the name of the state and the statistical summary of the group
        print(state)
        print(state_df.describe())

# Import the matplotlib.pyplot library as plt
    import matplotlib.pyplot as plt

# Define the columns to be included in the boxplot
    cols = ['R&D Spend', 'Administration', 'Marketing Spend', 'Profit']

# Create a boxplot for the defined columns of the DataFrame
    df.boxplot(column=cols)

# Display the plot
    plt.show()

# Save the plot as 'boxplot.jpeg'
    plt.savefig('boxplot.jpeg')

# Clear the current figure
    plt.clf()

# Group the DataFrame by 'State' and iterate over each group
    state_df = df.groupby('State')
    for state, state_df in states_df:
        # Define the columns to be included in the boxplot
        cols = ['R&D Spend', 'Administration', 'Marketing Spend', 'Profit']

        # Create a boxplot for the defined columns of the group
        state_df.boxplot(column=cols)

        # Save the plot as 'boxplot_{state}.jpeg'
        plt.savefig(f'boxplot_{state}.jpeg')

        # Clear the current figure
        plt.clf()

# Import the stats module from the scipy library
    from scipy import stats

# Filter the DataFrame for each state and store the results in separate DataFrames
    df_california = df[df['State'] == 'California']
    df_new_york = df[df['State'] == 'New York']
    df_florida = df[df['State'] == 'Florida']

# Get the 'Profit' values for each state
    profit_california = df_california['Profit'].values
    profit_new_york = df_new_york['Profit'].values
    profir_florida = df_florida['Profit'].values

# Perform a one-way ANOVA test on the 'Profit' values of the three states
    stat, p_value = stats.f_oneway(profit_california, profit_new_york, profir_florida)

# Print the p-value of the test
    print("p value: ", p_value)

# If the p-value is less than 0.05, reject the null hypothesis and conclude that the means are significantly different
    if p_value < 0.05:  
        print("We reject the null hypothesis. The means are significantly different.")
# Otherwise, fail to reject the null hypothesis and conclude that the means are not significantly different
    else:
        print("We fail to reject the null hypothesis. The means are not significantly different.")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
