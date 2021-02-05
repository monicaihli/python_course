######################################################################################################
#   File: exceptions-and-logging.py
#   Date: March 2, 2020
# Author: monica@utk.edu
#   Desc: Demonstrates how to combine exception handling with logging to create a robust program
#
######################################################################################################

import logging
import datetime

logging.basicConfig(
    filename='log-exception-demo' + datetime.datetime.utcnow().strftime("%d%b%Y_%Hh%Mm") + '.log',
    format='%(asctime)s %(levelname)-8s %(message)s', level=logging.ERROR)


while True:
  try:
    answer = input("Want to play a game? Say yes to proceed:  ")
    if answer != "yes":
      break
    entry1 = float(input("Please enter a number:  "))
    entry2 = float(input("Please enter another number:  "))
    result = entry1 / entry2
    print("{} divided by {} is: {}".format(entry1, entry2, result))
  except ZeroDivisionError as e:
    print("You can't divide by zero. Game over.")
    logging.error("ZeroDivisionError: {}".format(e))
  except ValueError as e:
    print("You failed to enter a valid number. Game over.")
    logging.error("ValueError: {}".format(e))
  except Exception as e:
    print("No idea what went wrong. Game over.")
    logging.error("Uknown Error: {}".format(e))
  finally:
    print("Thanks for playing!")