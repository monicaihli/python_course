###################################################################################################
# File: csv-module.py
# Date: Feb 19, 2020
# Author: Monica Ihli monica@utk.edu
# Description: Shows how to create csv file from list of dicts and to read a csv file
###################################################################################################
import csv

# create sample data
people_data = [
  {'name' : 'Mary','fav_color' : 'green', 'major' : 'Chemistry'},
  {'name' : 'Joe','fav_color' : 'blue', 'major' : 'Accounting'},
  {'name' : 'Jane','fav_color' : 'purple', 'major' : 'Information Science'},
]


with open ('./data/people.csv', 'w') as csvfile:
  fieldnames = ['name', 'fav_color', 'major']
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames) # expects a sequence of keys as header values
  writer.writeheader() # write field names as a header row. omit if you don't want them
  writer.writerows(people_data) # write all the rows of data


# read the data back in after we are done
with open ('./data/people.csv', 'r') as csvfile:
  reader = csv.reader(csvfile, delimiter=",")
  for row in reader:
    print(row)