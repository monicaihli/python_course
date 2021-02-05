######################################################################################################
#   File: logging-demo.py
#   Date: March 2, 2020
# Author: monica@utk.edu
#   Desc: Demonstrates use of logging module to write information to a log file. part of the
#         configuration can adjust for different levels of logging, depending on whats uncommented
#         and commented.
#
######################################################################################################

import logging
import datetime

# configure this logger to produce an output file that uses the current datetime for name
# can modify the logging level by uncommenting one and commenting the other to see difference
logging.basicConfig(
    filename='log-demo' + datetime.datetime.utcnow().strftime("%d%b%Y_%Hh%Mm") + '.log',
    filemode="w",format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO)
    #format='%(asctime)s %(levelname)-8s %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.ERROR)

demo_list = [1,2,"3",4,5,"6"] # include some numbers and also some strings to break things on purpose

for item in demo_list:
  try:
    result = item - 1
    print("The result of {} - 1 is {}".format(item,result))
    logging.info("Now processing the value of {}".format(item)) # will not be logged if level is error
  except Exception as myexception:
    print("We had problems doing the math.")
    logging.error("Error processing {}".format(item))