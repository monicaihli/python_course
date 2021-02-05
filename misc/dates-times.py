# **********************************************************************************************************************
#
#          File: dates-times.py
#
#        Author: Monica Ihli
#
#          Date: January 29, 2020
#
#   Description: Shows some examples of date and time manipulations in python.
#
#
#     Resources: https://docs.python.org/3/library/datetime.html
#                https://docs.python.org/3/library/time.html#module-time
#                https://docs.python.org/3/library/calendar.html#module-calendar
#
#
# **********************************************************************************************************************


from datetime import date
from datetime import datetime # import the datetime class from within the datetime module
import calendar
import time

today = date.today() # today will be a date object, not a string
# The below line would fail. You can only use the concatenation operator on strings, not date objects.
# msg = "Today's date is: " + today
msg = "Today is: " + str(today) # this works because we cast the date object to a string
print(msg)

# because month, date, and year are properties, not methods, they are are accessed without the ()
month = today.month  # the month, day, and year properties of a date object are stored as integers
day = today.day
year = today.year

print("Month: " + str(month))
print("Day: " + str(day))
print("Year: " + str(year))

# DATE AND TIME TOGETHER
right_now = datetime.now() # an instance of a datetime object
print("The time is: " + str(right_now))
# Formatting documentation is at https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior



day_of_week = today.weekday() # .weekday() returns an integer 0-6 for Monday through Sunday
print("Today is: " + str(day_of_week))


date_string_1 = "2020-01-29 16:40:00" # create a sample string that we know contains date info
datetime_obj_1 = datetime.strptime(date_string_1, "%Y-%m-%d %H:%M:%S")

# this one expects to interpret 12hour clock and am/pm format. But it will still store the hour as a 24 hour value.
date_string_2 = "2020-01-29 04:40:00 PM"
datetime_obj_2 = datetime.strptime(date_string_2, "%Y-%m-%d %I:%M:%S %p")

# Convert a date object into a string.
formatted_date_string = today.strftime("%m/%d/%Y")
print(formatted_date_string)


# Demonstrate time delta

next_class_period_string = "2020-02-03 04:40:00 PM"
next_class_period = datetime.strptime(next_class_period_string, "%Y-%m-%d %I:%M:%S %p")

# Date manipulations illustrate why you might not want to leave your time information in the form of a string
diff_timedelta = next_class_period - right_now # result is a timedelta object holding the difference.
print(diff_timedelta)
future_time = right_now + diff_timedelta
print(future_time)

# ************************************************************************************************************
# calendar.day_name returns an array containing days of the week ordered Monday through Sunday
print("Better known as: " + str(calendar.day_name[day_of_week])) # an array element is accessed using an integer position

# print a calendar object for a specified day and month
demo_year = 2020
demo_month = 1
# creates a string representation of the specified month
demo_calendar = calendar.month(demo_year,demo_month)
print(demo_calendar)

print(calendar.isleap(2020)) # returns true or false depending on is leap year.
# demonstration of iteration
object = calendar.Calendar

# ************************************************************************************************************

# time module

print(time.time()) # prints the current time in epoch time.

epoch_time = right_now.timestamp() # use datetime.timestamp to convert a datetime object to an epoch time float
print(epoch_time)
formatted_time_string = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch_time)) # time module also has .strftime()
print(formatted_time_string)


print("2a")
coffee = ""

print("2b")
added = 1 + 1