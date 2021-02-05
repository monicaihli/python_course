# **********************************************************************************************************************
#
#          File: var_identity.py
#
#        Author: Monica Ihli
#
#          Date: January 22, 2020
#
#   Description: Uses the id() function to demonstrate concepts of identity, comparison, and mutability. id() returns
#                the unique identity of a variable-- in our case, the address in memory.
#                For best results, step through the program using PyCharm Debugging feature.
#
#
# **********************************************************************************************************************

# Immutable objects cannot change the value stored at that location in memory. If you try to change the value
# associated with a variable name (the label for that value), it will just create a brand new location in memory
# to store the value.

print("*"*80)
print("Behavior of IMMUTABLE Objects")
print("*"*80) # cool trick for printing 80 or however many of what's inside the quotes.


# two immutable objects with the same value will reference the same identity in memory
print("INSTRUCTOR:")
instructor = "Monica" # create a string variable; strings are examples of an immutable type in Python
print(instructor)
print(id(instructor)) # the id function is nested inside the print statement. So print the output of id()

print("STUDENT")
student = "Jane"
print(student)
print(id(student))


# Python will be efficient. If the value is the same, then both labels will point to the same place
print("LIBRARIAN")
librarian = "Monica"
print(librarian)
print(id(librarian)) # the id/address of librarian will be the same as instructor.

print("Test equality of Identity")
print(instructor is librarian) # is operator tests if identity is the same. In this case it will return True
print("Test equality of Value")
print(instructor == librarian) # this is an example of ==, an operator to test if two values are the same


print("**** Change Instructor ****")
instructor = "Iman"
print(instructor)
print(id(instructor))
print(instructor is librarian) # Now the test will return False. "Iman" has a different identity/memory address.

# **********************************************************************************************************************
# Mutable objects CAN change. You can repopulate the same piece of memory, pointed to by the same name, with a new value
# **********************************************************************************************************************

print("*"*80)
print("Behavior of Mutable Objects")
print("*"*80)

jack_grades = [80,80,100] # This is an object called a list. We'll learn more about these later.
print("Identity of grades for Jack:")
print(jack_grades)
print(id(jack_grades)) # For now just know that they are mutable objects.

print("Identity of grades for Jill:")
jill_grades = [80,80,100]
print(jill_grades)
print(id(jill_grades)) # Even though they have the same value, you'll see they are stored in two different places.

print("Test equality of identity:")
print(jack_grades is jill_grades) # Returns false. The immutable objects have their own identity, even if their value is equal
print("Test equality of value:")
print(jack_grades == jill_grades) # Returns true. Their identity (memory address) is different, but same value stored

print("Add new grade for Jack- Same identity:")
jack_grades.append(100)
print(jack_grades)
print(id(jack_grades))


# oops, Jack wants us to start using his full name, Jackson.
print("Create a new variable name jackson_grades and assign it to same content as jack_grades")
jackson_grades = jack_grades # assign the contents and memory location referenced by jack to jackson
print(jackson_grades)
print(id(jackson_grades))
print(jack_grades is jackson_grades)


print("Reassign values for Jill - New identity:")
print(jill_grades)
jill_grades = [90,90,100]
print(id(jill_grades))