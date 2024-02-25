import pandas as pd

#Read the data
df = pd.read_csv('50_Startups.csv')

print(df.describe())

states_df = df.groupby('State')
for state, state_df in states_df:
    print(state)
    print(state_df.describe())

import matplotlib.pyplot as plt
cols = ['R&D Spend', 'Administration', 'Marketing Spend', 'Profit']
df.boxplot(column=cols)
#plt.show()
plt.savefig('boxplot.jpeg')
plt.clf() #clear image

state_df = df.groupby('State')
for state, state_df in states_df:
    cols = ['R&D Spend', 'Administration', 'Marketing Spend', 'Profit']
    state_df.boxplot(column=cols)
    plt.savefig(f'boxplot_{state}.jpeg')
    plt.clf() #clear image

from scipy import stats
# Analysis of Variance Test
# Caution: data used in the ANOVA must be normally distributed

df_california = df[df['State'] == 'California']
df_new_york = df[df['State'] == 'New York']
df_florida = df[df['State'] == 'Florida']

profit_california = df_california['Profit'].values
profit_new_york = df_new_york['Profit'].values
profir_florida = df_florida['Profit'].values

stat, p_value = stats.f_oneway(profit_california, profit_new_york, profir_florida)
print("p value: ", p_value)
#if < alpha, reject the null hypothesis of the same mean

if p_value < 0.05:  # Using a significance level of 0.05
    print("We reject the null hypothesis. The means are significantly different.")
else:
    print("We fail to reject the null hypothesis. The means are not significantly different.")

#Fishers