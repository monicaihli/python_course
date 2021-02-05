##########################################################################
#       Author: Monica Ihli monica@utk.edu
#         File: format.py
#         Date: Feb 10, 2020
#  Description: A short demo on the use of .format() for printing variables
#Documentation: https://docs.python.org/3/library/string.html#format-specification-mini-language
##########################################################################

var1 = "Curly"
var2 = "Larry"
var3 = "Moe"

print('The three stooges are {}, {}, and {}.'.format(var1, var2, var3))



print("\n ***** NUMBERS ***** \n")
num = 123

# f for floating point, default 6 places
print("Format the number {0:f}".format(num))

# specify 2 decimal places
print("Format the number {0:.2f}".format(num))

# scientific notation
print("Format the number {0:e}".format(num))

