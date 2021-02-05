# files-read.py
# Date: Feb 19 2020
# Author: Monica Ihli monica@utk.edu
# Description: Demonstrate some basic abilities to read from files in Python
# *******************************************************************************************************

# *******************************************************************************************************
# OPEN() AND CLOSE() STATEMENTS vs WITH OPEN()
# *******************************************************************************************************

#my_file = open('cat-ipsum.txt') # default mode assumes read and utf-8 encoding
my_file = open('./data/cat-ipsum.txt', 'r') # or you can manually specify file mode


# read each line one at a time. a line is delimited by hidden line-terminator characters. view with debug
for line in my_file.readlines():
  print(line)
  #print(line.upper()) # can manipulate the contents of the text once it has been put in a variable like this
my_file.close() # close the file object, releasing system resources and preventing other potential problems

print('\n'+'*'*80+'\n')

# USING WITH OPEN TO AUTOMATICALLY CLOSE
with open('./data/cat-ipsum.txt') as cats:
  text_lines = cats.readlines() # .readlines() returns a list of lines as terminated in the file
  type(text_lines)
  # at the end of with code block, the file is automatically closed

for line in text_lines: # with a list of strings, we can use iterable functionality on the contents
  print(line)

# *******************************************************************************************************
# READ() - returns the entire contents of file as a single string variable
# *******************************************************************************************************
print('\n'+'*'*80+'\n')
with open('./data/cat-ipsum.txt') as cats:
  text_all = cats.read()

type(text_all)

# *******************************************************************************************************
# READLINE() returns a single line of text as a string variable
# *******************************************************************************************************

with open('./data/cat-ipsum.txt') as cats:
  text_all = cats.readline()

print('a')