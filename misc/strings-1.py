# **********************************************************************************************************************
#
#          File: strings-1.py
#
#        Author: Monica Ihli
#
#          Date: January 22, 2020
#
#   Description: Demonstrates some basic features of working with strings.
#                FOR BEST RESULTS step through each line at a time with debugging.
#
#
# **********************************************************************************************************************

my_string = "This is a test."  # how to declare a string variable.
print(my_string)

my_empty_string = ""  # an empty string. Creates an object we can add content to later.
print(my_empty_string)

my_empty_string += "Add some text. " # cool trick for concatenating (combining) strings with less code
print(my_empty_string)

my_empty_string += "Now even more text." # can just keep adding and adding to the same variable.
print(my_empty_string)

newline_string = "This\nis\na\nstring\nwith\nnewlines!" # show the use of \n escape sequence for line breaks
print(newline_string)

# it's actually not necessary to assign a string value to a variable to print it
print("We can also combine newlines with tabs. This is a newline\n\tfollowed by a tab.")

print("\n\n") # just throwing in some extra newlines can help make your output look less crowded

# you also have to use escape sequences if you want to literally print quotes instead of using quotes as coding syntax
print("My daughter said she needed to go to her friend's house to do \"homework\".")
print("What this really meant is she wanted to go spend 30 minutes doing homework and 3 hours playing Minecraft.")



print("\n"+"*"*80+"\n") # skip a line with newline, print * 80 times, then skip another line.

# Moving back and forth between data types


my_var = 3
print(type(my_var)) # type() returns the data type of a variable. At first, Python infers it's an integer.

my_var = float(my_var) # But we can cast that to a floating point which has decimal values
print(type(my_var)) # returns float
print(my_var) # still prints the value 3.0

# There are certain things you can do with strings that you can't do with numbers.
# For example, you can join two strings with +

string1 = "chocolate chip"
string2 = "cookies"

print(string1 + " " + string2) # prints: chocolate chip cookies

print(str(my_var) + " " + string1 + " " + string2) # have to convert the integer to a string to use + operator with it

print(  str(int(my_var)) + " " + string1 + " " + string2) # cast my_var to an int and then to string w/ nested functions!




