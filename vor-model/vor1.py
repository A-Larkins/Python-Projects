import pandas as pd
import numpy as np
from pandas.core.indexes import base

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



base_columns = ['Player', 'Tm', 'Pos']
rushing_columns = ['FantasyPoints', 'Rec', 'Rec Yds', 'Rec TDs', 'Rushes', 'Rush Yds', 'Rush TDs']

rb_df = df.loc[(df['Pos'] == 'RB', base_columns + rushing_columns)]

# print(rb_df.sort_values(by='Rush Yds', ascending=False).head(15))

# print(rb_df.describe().transpose())

# print(rb_df['Rushes'][:10])

# print(rb_df['Rushes'].max())

rb_df['RushingTDRank'] = rb_df['Rush TDs'].rank(ascending=False)
# print(rb_df.sort_values(by='RushingTDRank').head(5))

# print(rb_df['Rushes'].value_counts())

# import seaborn as sns
# sns.set_style('whitegrid')
# sns.displot(rb_df['Rushes'])

d_henry = rb_df.loc[rb_df['Player'] == 'Derrick Henry']
# d_henry.index = d_henry.index.rename('Category')
# d_henry.columns = ['Value']
print(d_henry.transpose())
#rb_df.values numpy array



