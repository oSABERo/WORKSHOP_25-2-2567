import pandas as pd

df = pd.read_csv('50_Startups.csv')

print(df.describe())

states_df = df.groupby('State')
for state, state_df in states_df:
    print(state)
    print(state_df.describe())