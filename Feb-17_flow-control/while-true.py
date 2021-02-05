# File: while-true.py
# Date: Feb 17, 2020
# Description: Two approaches to a while loop
#

import datetime


# While loop demo 1
response = "yes" # initiate a variable to a value to start
while response == "yes":
  print("The time is: {}".format(datetime.datetime.now()))
  response = input("Would you like to continue? ")
  while not (response == "yes" or response == "no"):
    response = input("Invalid response. Enter \"yes\" or \"no\": ")
print("Bye!")



#while True:
#  print("The time is: {}".format(datetime.datetime.now()))
#  response = input("Would you like to continue? ")
#  while not (response == "yes" or response == "no"):
#    response = input("Invalid response. Enter \"yes\" or \"no\": ")
#  if response == "no":
#    break
#print("Bye!")