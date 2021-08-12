import pandas as pd
import numpy as np
from pandas.core.indexes import base

adp_df = pd.read_csv('FantasyPros_2021_Overall_ADP_Rankings.csv', index_col=0) # set index col = 0 to set the range index as our dataframes index
# instead of https://raw.githubusercontent.com/fantasydatapros/data/master/fantasypros/adp/PPR_ADP.csv

print(adp_df.head(10));