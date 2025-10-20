# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

# 1. Load the dataset
df = pd.read_csv('titanic.csv')  # Make sure 'titanic.csv' is in the same folder as this script

# 2. Explore the dataset
print("First 5 rows:")
print(df.head())

print("\nDataset info:")
print(df.info())

print("\nMissing values per column:")
print(df.isnull().sum())

# 3. Handle missing values
df['Age'].fillna(df['Age'].median(), inplace=True)         # Fill Age with median
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)  # Fill Embarked with mode
df.drop('Cabin', axis=1, inplace=True)                     # Drop Cabin column (too many missing)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# 4. Convert categorical features to numerical
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})       # Map Sex
df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)  # One-hot encode Embarked

# 5. Normalize numerical features
scaler = StandardScaler()
numerical_features = ['Age', 'Fare']
df[numerical_features] = scaler.fit_transform(df[numerical_features])

