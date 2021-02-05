import pandas as pd

salesreps_list_dicts = [dict(name='Samantha', avgannualsales=223876, yearsatcompany=1),
                  dict(name='Jason', avgannualsales=388331, yearsatcompany=3),
                  dict(name='Marcy', avgannualsales=123854, yearsatcompany=2),
                  dict(name='Susan', avgannualsales=564894, yearsatcompany=1),
                  dict(name='Tom', avgannualsales=410237, yearsatcompany=1)]

salesreps_df = pd.DataFrame(salesreps_list_dicts) # create a dataframe from the dictionary

print("\n  ***** Describe data ***** ")
print(salesreps_df.head(2)) # head prints the first few rows of data
print(salesreps_df.describe()) # describe gives some statistical information about numbers in the data and record count


print("\n  ***** Total Avg Annual Sales Across All Reps ***** ")
total = salesreps_df['avgannualsales'].sum()  # use an aggregate function to sum the rows
print("${:,.2f}".format(total))


print("\n  ***** With Lifetime Sales ***** ")
salesreps_df['lifetimesales'] = salesreps_df['avgannualsales'] * salesreps_df['yearsatcompany'] # create computed column
print(salesreps_df.head())
print(salesreps_df.describe())

print("\n ***** Display only top average annual sales ***** \n")
new_df = salesreps_df[salesreps_df['avgannualsales'] > 300000] # subsetting: only keep rows where sales meet condition
print(new_df.describe())
print(new_df.head(5))


###############################################################################

print("\n ######################### STORE DATA #############################\n")

# other strategy for creating a dataframe: one dict where keys are paired with lists as corresponding values

store_dict = { 'store_id' : ['123', '456', '789'],
               'store_city' : ['Knoxville', 'Oak Ridge', 'Chattanooga'],
               'store_sales' : [564846,787864,712687]
               }

stores_df = pd.DataFrame(store_dict)

print(stores_df.head(5))
print(stores_df.describe())


print("\n ######################### PRINTING TO FILE #############################\n")

stores_df.to_csv("stores.csv", index=False) # write to csv file and don't include autogenerated index
salesreps_df.to_csv("salesreps.csv")