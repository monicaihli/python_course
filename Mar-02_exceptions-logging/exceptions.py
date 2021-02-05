######################################################################################################
#   File: exceptions.py
#   Date: March 2, 2020
# Author: monica@utk.edu
#   Desc: Demonstrates several approaches to implementing exeptions for purposes of error handling
#
######################################################################################################


# SIMPLE EXCEPTION: TRY/EXCEPT/ELSE
try: # start of code block to attempt
  some_string = "Some string"
  print(some_string[100]) # trying to print the character at a nonexistent index
  print("Did something")  # Will never execute. It breaks before it gets this far.
except: # start of block of code to execute in event of problem in try block
  print("Invalid request")




# TRY/EXCEPT/ELSE - Else includes code to execute ONLY if try block successfully completes
while True:
  try: # attempts to execute code in this block
    entry = int(input("Please enter a number: "))
    print("Say something interesting")
  except: # If any failure, stops and executes THIS block
    print("That was not a valid number.")
  else:  # only executes else block if the try is successfully completed.
    print("You can follow directions. Good job!")
    break
  finally:
    print("Finished this pass.")


# MULTIPLE EXCEPTIONS INCLUDING BUILT-IN EXCEPTIONS
try:
  entry1 = float(input("Please enter a number:  "))
  entry2 = float(input("Please enter another number:  "))
  result = entry1/entry2
  print("{} divided by {} is: {}".format(entry1,entry2, result))
except ZeroDivisionError:
  print("You can't divide by zero")
except ValueError:
  print("Not valid numbers")
except:
  print("No idea what went wrong.")
finally:
  print("Thanks for playing!")



# TRY/EXCEPT ASSIGNING EXCEPTION TO VARIABLE
try:
  rain_odds = 80
  print("Today the chance of rain is " + rain_odds + "percent.")
except Exception as e:
  print("Error encountered:")
  print(e)