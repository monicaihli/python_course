# https://docs.python.org/3/library/logging.html
# More advanced usage: https://docs.python.org/3/howto/logging-cookbook.html
#
# logging functions are named after the level or severity of the events they are used to track.
# The standard levels and their applicability are described below (in increasing order of severity):
#
#      __________________________
#     | Level    | Int Value|
#     |----------|----------|
#     | CRITICAL |    50    |
#     | ERROR    |    40    |
#     | WARNING  |    30    |
#     | INFO     |    20    |
#     | DEBUG    |    10    |
#     | NOT SET  |     0    |
#      ----------------------

# import the necessary module and set up the configuration for it
import logging

# Try changing the log level from ERROR to INFO to DEBUG, and see how the log file output changes each time!
# basicConfig does basic configuration of default values & behavior for different possible parameters
# https://docs.python.org/3/library/logging.html#logging.basicConfig
logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',filemode='w', filename="levels-review.log",
                    level='DEBUG')


inputs_list = [1, 2, "3", 4, "6", 7, 8] # contains some intentionally bogus values
logging.debug('Input data loaded.')


for key, value in enumerate(inputs_list):
  logging.info("Now processing input {}: {}".format(key, value))
  try:
    logging.debug('Preparing to add.')
    added = value + 1
    print("Addition - Original value: {}, Increased value: {}".format(value, added))

    logging.debug('Preparing to multiply.')
    multiplied = value * 2
    print("Multiplication - Original value: {}, Increased value: {}\n".format(value, multiplied))


  except Exception as e: # assign the exception message to a variable called "e"
    print('An error occurred.')
    logging.error(e)



