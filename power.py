#EXAMPLE1
import pandas as pd

#อ่านไฟล์
df = pd.read_csv('power.csv')
df = df.drop(['ts'], axis=1)
df = df[['irr', 'tamb', 'tmodule', 'wind', 'pack']]
print(df.info())