######################################################################################################
#   Desc: Demonstrates how to combine exception handling with logging to create a robust program
#
#
#
######################################################################################################

import logging

logging.basicConfig(
    filename='log-exception-demo.log',filemode='w',format='%(asctime)s %(levelname)-8s %(message)s', level=logging.ERROR)

try:  # try means "attempt to do this thing"
  entry1 = float(input("Please enter a number:  "))
  entry2 = float(input("Please enter another number:  "))
  result = entry1 / entry2
  print("{} divided by {} is: {}".format(entry1, entry2, result))
except ZeroDivisionError as e: # one possible exception. Only executes if a zero division error occurs
  print("You can't divide by zero. Game over.")
  logging.error("ZeroDivisionError: {}".format(e))
except ValueError as e: # another possible exception. only executes if fail to enter a valid number
  print("You failed to enter a valid number. Game over.")
  logging.error("ValueError: {}".format(e))
except Exception as e: # a final, "catch all" exception to handle problems that the the first 2 didn't catch
  print("No idea what went wrong. Game over.")
  logging.error("Uknown Error: {}".format(e))
finally: # finally block executes no matter what
  print("Thanks for playing!\n\n")
