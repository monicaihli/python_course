# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html#pandas.read_csv
# read data on measles fatalities in London from 1629 - 1939

import pandas as pd

measles_df = pd.read_csv("measles.csv", index_col=0) # this data set already has an index column in position zero

print(measles_df.head(n=5))
print(measles_df.describe())

print("\n *** DROP MISSING VALUES *** \n")

measles_df.dropna(inplace=True)# inplace means  you don't have to assign the result of the operation to a variable.
print(measles_df.describe())


print("\n *** STATISTICS *** \n")
min = measles_df['value'].min()
print("Min: {}".format(min))
max = measles_df['value'].max()
print("Max: {}".format(max))
