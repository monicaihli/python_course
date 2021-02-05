import pandas as pd

possum_df = pd.read_csv("possum.csv", index_col=0)
print("\nColumns in DF:")
list_of_cols = possum_df.columns # the column names are stored as a list property of the DF
for col in list_of_cols: # so for every header name in that list
  print('\t' + col)   # print it off


possum_df = possum_df[['sex', 'age', 'totlngth', 'skullw']] # subsetting only a specific set of columns
print("\nColumns in DF after subsetting:")
list_of_cols = possum_df.columns
for col in list_of_cols:
  print('\t' + col)

print("\nAVERAGES BY SEX:")
print(possum_df.groupby('sex').mean())


print("MAX BY SEX:")
print(possum_df.groupby('sex').max())


print("MIN BY SEX:")
print(possum_df.groupby('sex').min())


print("\n"+ "#" *80)
print("ILOC - Integer based selection:")
# retrieving rows by loc method
row = possum_df.iloc[3] # will return a series containing the row data for position 3
print(row)

print("Range with iloc")

set_of_rows = possum_df.iloc[3:6]
print(set_of_rows)