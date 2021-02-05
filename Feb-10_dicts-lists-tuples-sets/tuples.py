######################################################################################################
# File: tuples.py
# Date: Feb 10, 2020
# Author: Monica Ihli monica@utk.ed
# Description: Brief demo on tuples
######################################################################################################


print(' ################## TUPLES ##############')

# create an immutable tuple as a sequence of strings
my_tuple = ('a', 'b', 'c', 'd', 'e')
print(type(my_tuple))
print(my_tuple)

# create a tuple from a sequence of numbers
my_other_tuple = (1,2,3,4,5)
print(my_other_tuple)


# access elements with iteration
print('Iteration:')
for item in my_tuple:
  print(item)


# access elements based on position
print('By index:')
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[2])
print(my_tuple[3])
print(my_tuple[4])

