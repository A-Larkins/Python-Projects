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
# print(df[:10])

# print(df.columns)
# or 
# ', '.join(df.columns)

scoring_weights = {
    'receptions': 0.5, # half PPR
    'receiving_yds': 0.1,
    'receiving_td': 6,
    'FL': -2, # fumbles lost
    'rushing_yds': 0.1,
    'rushing_td': 6,
    'passing_yds': 0.04,
    'passing_td': 4,
    'int': -2
}

# no fumbles lost...
df['FantasyPoints'] = (
    df['Rec']*scoring_weights['receptions'] + df['Rec Yds']*scoring_weights['receiving_yds'] + 
    df['Rec TDs']*scoring_weights['receiving_td']  + 
    df['Rush Yds']*scoring_weights['rushing_yds'] + df['Rush TDs']*scoring_weights['rushing_td'] + 
    df['Pass Yds']*scoring_weights['passing_yds'] + df['Pass TDs']*scoring_weights['passing_td'] + 
    df['Ints']*scoring_weights['int'] ) 

print(df.head())