import pandas as pd

#อ่านไฟล์
df = pd.read_csv('insurance.csv')

print(df.info())

print(df['sex'].unique())

#กำหนดการแปบว
sex_map = {
    'female': 0,
    'male': 1
}
df['sex']=df['sex'].map(sex_map) 
print(df.head())