#
# Author: Monica Ihli monica@utk.edu
# Date: Feb 10, 2020
# Description: This shows you a simple way to accept input at the console/command line.
#

my_num = input("Enter a number: ") # Whatever user enters will go into the variable as a STRING
print('You entered: ' + my_num)  # display what was assigned to the variable
print('The type of this variable is: ' + str(type(my_num))) # show that the input was a string variable