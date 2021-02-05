# **********************************************************************************************************************
#
#          File: regex_demo.py
#
#        Author: Monica Ihli
#
#          Date: January 27, 2020
#
#   Description: Demonstrates the use of regular expressions on sample text.
#
#                Requirements: Given a list of Subject labels, such as found at https://libguides.utk.edu/az.php,
#                detect the labels that contain a word that indicates the content being described is datasets.
#                The regular expression has to return results that meet the following conditions:
#                    > The word "data" but not "database"
#                    > Any variant of "statistic" including "statistics" or "statistical"
#                    > The word "dataset" or "datasets"
#                    > Ignores differences in case/capitalization.
#

#     Resources: Python 3 Documentation https://docs.python.org/3/library/re.html
#                Online Regular Expressions Tester: https://regex101.com/
#
#
# **********************************************************************************************************************
import re


# This is an example of a list. We will learn about creating lists later in the semester.
subject_labels_list = [
  'English Databases',
  'Datasets (52)',
  'Data & Statistics (47)',
  'Datasets & Statistics (18)',
  'Property Data (13)',
  'Statistics (25)',
  'Statistical & Data Sources (23)',
  'Physics & Chemistry',
  'datasets (7)',
  'Polling and Statistics (15)',
  'Data (36)',
  'Statistics & Numerical Data (1)',
  'Map / Geospatial Data (2)',
  'Data Sets and Repositories (5)',
  'Datasets (25)',
  'Corporate Financial Data (9)',
  'Statistics & Datasets (35)',
  'Humanities (3)',
  'Data and Statistics (33)']

# Compiling a regular expression which meets all our conditions
regex = re.compile(r'(data)\b|(dataset)|(statistic)', flags=re.IGNORECASE)

# This for loop is an example of how to iterate over every item in a list
# We will talk techniques for flow control in class soon
for x in subject_labels_list:
  returned_value = regex.search(x) # uncomment if you want to watch what is being returned in debug mode
  if regex.search(x): # Returns None if the search expression cannot be found, or the found value
    print(x) # If a match is found, print this string
  else:
    print("no match: " + x) # otherwise, print "no match" before the label

