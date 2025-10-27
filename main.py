import pandas as pd
import numpy as np

df = pd.read_csv('movies_metadata_v2.csv', encoding='iso-8859-1').dropna(axis=1, how='all')
print(df.head())
print("How many rows and columns in the whole dataset?")
print(df.shape)
print(df.info()) # summary of columns

# Filter films that cost over a million dollars
# df['budget'] grab the column you want
budget_df = df[ df['budget'] > 1000000 ]
print(budget_df.shape) # 7208 movies have a budget above 1mil

