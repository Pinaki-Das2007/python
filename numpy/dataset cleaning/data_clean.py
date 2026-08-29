# importing necessary library
import pandas as pd
import numpy as np


# loading the dataset
df = pd.read_csv('numpy\dataset cleaning\employee_data_capstone.csv')
print(df.head())

# checking the missing values
print("Missing values in each column:")
print(df.isnull().sum())


df['salary (in)'] = df['salary'].replace('?', np.nan)