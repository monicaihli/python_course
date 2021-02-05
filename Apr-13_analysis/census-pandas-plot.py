from matplotlib import pyplot
import pandas as pd

# read a file called census-pop-data.csv
# expect tabs as the delimiter (not commas)
# the headers (column labels) are in the first row index
# only keep the year and population columns though
# when reading numbers, expect a comma as the thousands separator
pop_df = pd.read_csv('census-pop-data.tsv', sep='\t',header=0,
                   usecols=['year','population'], thousands=',')

print(pop_df.head(5))

pop_df.plot(kind='bar', x='year', y='population')
pyplot.show() # don't forget to show the plot!
