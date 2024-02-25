import pandas as pd

#อ่านไฟล์
df = pd.read_csv('insurance.csv')

print(df.info())

print(df['sex'].unique())

#กำหนดการแปลง
sex_map = {
    'female': 0,
    'male': 1
}
df['sex']=df['sex'].map(sex_map) 

smoker_map = {
    'yes': 1,
    'no': 0
}
df['smoker']=df['smoker'].map(smoker_map)

region_encoded = pd.get_dummies(df, columns['region'])
df = pd.concat([df, region_encoded], axis=1)
df = df.drop('region', axis=1)

print(df.head())