# **********************************************************************************************************************
#
#          File: booleans_numbers_fractions.py
#
#        Author: Monica Ihli
#
#          Date: Feb 03, 2020
#
#   Description: Numbers and fractions in Python. Best results: use debugging to go through each line
# **********************************************************************************************************************


# Combine comparison operations that return boolean objects with boolean logic: and or

print("Boolean Logic: OR") # Either value has to pass the test to return True
print(True or True)  # Returns True
print(True or False)  # Returns True
print(False or True)  # Returns True
print(False or False)    # Returns False
print("Boolean Logic: AND") # Both values must pass the test to return True
print(True and True) # Returns True
print(True and False)  # Returns False
print(False and True)  # Returns False
print(False and False)    # Returns False


print('/n/n')

print('Fractions')
from fractions import Fraction
print(Fraction(1/2))