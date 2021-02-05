#
#  Date:  March 04, 2020
#  File:  functions-1.py
#  Auth:  monica@utk.edu
#  Desc:  Demonstrates alternative way to structure program and functions
#

def main():
  other_function1() # call some other function inside main
  other_function2()

def other_function1():
  print("Calling another function")

def other_function2():
  print("And another function")


# very bottom of script
if __name__ == "__main__": # this works when you are running from the "main" program and not from a module being imported
  main()