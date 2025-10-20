import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('titanic.csv')  

print("First 5 rows:")
print(df.head())

print("\nDataset info:")
print(df.info())

print("\nMissing values per column:")
print(df.isnull().sum())

df['Age'].fillna(df['Age'].median(), inplace=True)         
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)  
df.drop('Cabin', axis=1, inplace=True)                   

print("\nMissing values after cleaning:")
print(df.isnull().sum())

df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})    
df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)
scaler = StandardScaler()
numerical_features = ['Age', 'Fare']
df[numerical_features] = scaler.fit_transform(df[numerical_features])



