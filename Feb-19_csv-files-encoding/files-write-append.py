# *******************************************************************************************************
# file: files-write-append.py
# Date: Feb 19, 2020
# Author: Monica Ihli  monica@utk.edu
# Description: Demo how to write to file and append to file
# *******************************************************************************************************

# WRITE TO FILE

my_list = ['eggs', 'milk', 'juice', 'bread']



output_file_name = "./data/output_file.txt"  # include both a path and file name if going anywhere other than same location
output_file = open(output_file_name, 'w') # open in write mode. if doesn't exist will make a new file
output_file.write(str(my_list))
output_file.close()

# use write again on same file name
output_file = open(output_file_name, 'w') # open same file in write mode.
for thing in my_list: # use iteration
  output_file.write(thing + '\n')  # write one line at a time. be use to add /n if you want to break lines
output_file.close()


# *******************************************************************************************************
# APPEND TO EXISTING FILE
# *******************************************************************************************************
new_list = ['cookies', 'coffee', 'cheesecake']
output_file = open(output_file_name, 'a') # open same file in APPEND mode.
for thing in new_list: # use iteration
  output_file.write(thing + '\n')  # write one line at a time.
output_file.close()