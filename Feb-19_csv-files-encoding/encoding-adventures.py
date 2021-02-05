###################################################################################################
# File: encoding-adventures.py
# Date: Feb 19, 2020
# Author: Monica Ihli monica@utk.edu
# Description: Demonstrates potential for encoding problems. Run the program first, and you will have
#              no problems, but if you uncomment the second block of code, which tries to decode the
#              file contents as ASCII, you will get an error. It doesn't know what to do with the
#              non-English characters
###################################################################################################



#with open("./data/hobbit.txt", "r", encoding="utf-8") as spanish_hobbit:
#  print(spanish_hobbit.read())



# this will generate an error if you uncomment and run it:
# UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3 in position 62: ordinal not in range(128)

with open("./data/hobbit.txt", "r", encoding="ascii") as spanish_hobbit:
  print(spanish_hobbit.read())


