#
#  Date:  March 04, 2020
#  File:  functions-1.py
#  Auth:  monica@utk.edu
#  Desc:  Demonstrates different ways to create and call functions.




################################################################################################################

# function with no arguments and no return value
def print_str():
  print("This is a function with no arguments or return values.")

print_str() # call a function to print a string.
print('\n\n')


################################################################################################################
# function which accepts an argument but has no return value
def print_input(user_input):
  print("You entered: {}".format(user_input))

response = input("Please enter some text: ") # capture some text to a variable
print_input(response) # call the print_input() function and pass it the response variable
print('\n\n')


################################################################################################################
# function which both accepts an argument and returns a value
def validate(num_input):
  validated = False
  if num_input.isnumeric():
    if int(num_input) >= 1 and int(num_input) <= 10:
      validated = True
  return(validated)

demo_list = ["1", "2", "apples", "pie"]
for item in demo_list:
  outcome = validate(item)
  print("Is {} a valid number between 1 and 10?: {}".format(item, outcome))

print('\n\n')

################################################################################################################

# function that shows how you can reuse code. Also shows accessing the output of a function directly without
# assigning the returned value to a variable first (in the print statements)
import re

def clean(element):
  element = re.sub(r'[^\w\s]', '', element) # removes punctuation using a regular expression
  element = element.strip() # removes leading or trailing whitespace
  return(element) # return the cleaned piece of data

name="   .$ Sarah  "
major="  Accounting. #"
graduates="   $2021;"

print(clean(name))
print(clean(major))
print(clean(graduates))
print('\n\n')

################################################################################################################

# function showing passing multiple values, and use of keyword arguments
def merge_values(n,m,g):
  merged_string = n + " majors in " + m + " and will graduate in " + g
  return(merged_string)

name="George"
major="Cat Psychology"
graduates="2022"

merged_string = merge_values(name,major,graduates) # if keywords are not referenced, then the order will be assumed
print(merged_string)


name="Joana"
major="Moonshine Production Logistics"
graduates="2021"

merged_string = merge_values(g=graduates, n=name, m=major) # pass by argument keyword, doesn't have to be in order then
print(merged_string)
print('\n\n')


################################################################################################################

# function showing multiple return values

def do_maths(num1, num2):
  added = num1 + num2
  subtracted = num1 - num2
  return(added,subtracted)

return1, return2 = do_maths(5,3)
print("Returned values are {} and {}".format(return1, return2))


