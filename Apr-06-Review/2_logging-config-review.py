########################################################################################################################
# basicConfig does basic configuration of default values & behavior for different possible parameters
# https://docs.python.org/3/library/logging.html#logging.basicConfig
#
## format - You can add or modify what you'd like to be included in the message:
#          https://docs.python.org/3/library/logging.html#logrecord-attributes
#
# filemode - Just like regular file handlers, read, write, append, etc
#
# filename - what you would like to call the log file
#
# level - The log level to implement
#
########################################################################################################################

import logging

# a standard log file configuration
#logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',filemode='w',
#                    filename="config-review.log", level='DEBUG')

# You can add any text into the format= part; it won't interfere with the ability to read the attribute codes:
#logging.basicConfig(format='GO BIG ORANGE! %(asctime)s %(levelname)-8s %(message)s',filemode='w',
#                    filename="config-review.log", level='DEBUG')

# include the line number of the logging call:
logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s Line Number: %(lineno)d',filemode='w',
                    filename="config-review.log", level='DEBUG')

# include the name of the logger used to record the message (default is root, it's possible to have multiple loggers):
#logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s - Logger: %(name)s',filemode='w',
#                    filename="config-review.log", level='DEBUG')


fruits_list = ['apples', 'oranges', 'pears', 'bananas'] # contains some intentionally bogus values

for key, value in enumerate(fruits_list):
  logging.info("Now processing input {}: {}".format(key, value))
  print('Fruit {}: {}'.format(key+1, value))
  logging.info("Finished processing")


