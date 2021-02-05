# **********************************************************************************************************************
#
#          File: operators.py
#
#        Author: Monica Ihli
#
#          Date: Feb 03, 2020
#
#   Description: Demonstrates use of mathematical and assignment operators
#
#
# **********************************************************************************************************************


# MATH OPERATORS

# addition
print(10 + 20)  # prints 30

# subraction
print(30 - 10)  # prints 20

# multiplication
print(3*3)  #prints 9

# division
print(12 / 3)  # evaluates to 4.0 -- returns a float!
print(12.0 / 3) # 4.0
print(12 / 3.0) # all evaluate to 4.0

# modulo
print(10 % 3)  # evaluates to 1
print(10.0 % 3)  # evaluates to 1.0

# integer division (discards any remainder. Will actually return float or int)
print(10//4)  # evaluates to 2, but real answer is 2.5
print(10.0//4) # evaluates to 2.0, but real answer is 2.5

# exponent
print(2**3)  # evaluates to 4
print(2.0**3)  # evaluates to 4.0
print(2**3.0)  # evaluates to 4.0


print("***********************************************************")

# ASSIGNMENT OPERATORS
x = 8 # assign 8 to the value of x
print(x)

x += 2 # same as x = 8 + 2
print(x) # evaluates to 10

x -= 2 # same as x = 10 - 2
print(x) # evaluates to 8

x /= 2 # same as x = 8 / 2
print(x) # evaluates to 4.0

x *= 2 # equivelant of 4.0 * 2
print(x) # evaluates to 8.0

x %= 3 # same as remainder from 8.0 / 3 (leftover after division)
print(x) # evaluates to 2.0

x **= 4 # same as 2.0 raised to the 4th power
print(x) # evaluates to 16.0

x //= 3 # same as integer division of 16.0 / 3 (discard remainder)
print(x)




