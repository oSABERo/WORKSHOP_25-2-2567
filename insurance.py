import pandas as pd

#อ่านไฟล์
df = pd.read_csv('insurance.csv')

print(df.info())

print(df['sex'].unique())