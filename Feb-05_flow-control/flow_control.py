# flow-control.py
# Feb 05, 2020
# monica@utk.edu

#######################################################################################################



#######################################################################################################
print("\n*** IF STATEMENTS ***\n")
#######################################################################################################


# if statement demo 1: simple if statement
name = "Sam"
if name == "George":
  print("Top of the morning, George!")


# if statement demo 2: if/else
# if/else means that if the first test fails, the else block is executed by default
# try uncommenting the different name examples and see how the outcome changes

name = "Sam"
#name = "Not Sam"
if name == "Sam":
  print('Hello Sam!')
else:
  print("Where is Sam?")



# if statement demo 3: if/elif/else. Uncomment different names to see different outcomes

#name = "Trudy"
#name = "Judy"
name = "Sam"
if name == "Sam":
  print('Howdy Trudy')
elif name == "Jane":
  print("Howdy Jane")
elif name == "Judy":
  print("Go away Judy")
else:
  print("Nothing to see here.")


# if statement demo 4: if/elif/else but demonstrates that even in the case of multiple true conditions, only the
# first passing conditional block will be executed

num = 123

if num < 10:
  print("Less than 10")
elif num < 500:
  print("Less than 500")
elif num == 123:
  print("We have a match!")
else:
  print('Nothing to see here.')


#######################################################################################################
print("\n*** FOR LOOPS ***\n")
#######################################################################################################


# for loop demo 1
grades = [88,100,93,100,80] # a list of grades. Lists are iterable. We'll learn more soon!

print("Here are your grades:")
for grade in grades:
  print(grade)
print("Done listing Grades")

print('\n')


# for loop demo 2: nested statements
grades = [88,100,93,100,80]
print("Some Other Grades")
for grade in grades:
  print(grade)
  if grade == 100:
    print("WOW AMAZING!")
print("Done listing Grades")


print('\n')


# for loop demo 3: nested statements with break
grades = [88,100,93,100,80]
print("Last Set of Grades")
for grade in grades:
  if grade == 93:
    break
  print(grade)
print("Done listing Grades")



#######################################################################################################
print("\n*** WHILE LOOPS ***\n")
#######################################################################################################

# while demo 1

count = 1
stop = 5
while stop > count:
  print(count)
  count += 1
print("All done.")


