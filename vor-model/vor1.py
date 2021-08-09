import pandas as pd
import numpy as np

df = pd.read_csv('2021projections.csv')
# get rid of second index column
df = df.iloc[:, 1:]

# print(type(df))
# print(df.head())
# print(df.tail())

# print(df.head(10))
# or
print(df[:10])

print(df.columns)
# or 
# ', '.join(df.columns)

