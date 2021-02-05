#0#####################################################################################################
# File: lists.py
# Date: Feb 10, 2020
# Author: Monica Ihli monica@utk.ed
# Description: Demonstrates a variety of ways to create, use, and access lists.
######################################################################################################


my_list = ['bread', 'milk', 'eggs']  # create a simple list
print(my_list)

# length of list
count = len(my_list) # len() will return the length of items there are in a sequence, such as a list
print(count)


# iterate items
my_list = ['bread', 'milk', 'eggs']
for item in my_list: # we can use a for look to iterate over and access all the objects in a list
  print(item)


# append a new item to existing list
my_list = ['bread', 'milk', 'eggs']
my_list.append('apples')
print(my_list)


# extend an existing list by adding another sequence to it
list1 = [1,2,3]
list2 = [4,5,6]
list1.extend(list2)
print(list1) # prints list1 combined with list2
print(list2) # list 2 remains the same

# insert value at a specified index
list1 = [1,2,3]
list1.insert(1, 'a')   # .insert(<position>, <value>)
print(list1)
list1.insert(len(list1), 'b') # we can even use len() to help us put item at end of a list of any size
print(list1)

# remove all items which match a given value, returns ValueError if no such item found
my_list = ['bread', 'milk', 'eggs']
my_list.remove('milk') # you can pass a variable or a value, makes no difference
print(my_list)

# count all occurences of a given value and return that count as an integer
my_list = ['no','yes','no','no','yes','yes','no','no','yes']
print("{} people voted yes, and {} people voted no."
  .format(my_list.count('yes'), my_list.count('no'))) # Can you figure out how this fancy print statement works?


# sort values
list1 = ['d', 'g', 'c', 'a', 'b', 'f', 'e']
list1.sort()
print(list1)
list1.sort(reverse=True)  # can also sort descending order instead.
print(list1)

################################################################################################
# WORKING WITH SLICING



# slice a list based on indices:
# start at 0, and including 0, end before 3
start = 0 # position where to start the slice, inclusive
end = 3 # index of where to cut off the slice, NOT including this index
list1 = ['a','b','c','d','e','f','g','h','i']
print(list1[start:end]) # print all elements of list from index 0 to index 2
print(list1)

print(list1[2:6]) # start at index 3 and create a slice 2 elements long

# another slicing example
list1 = ['a','b','c','d','e','f','g','h','i']
print(list1[1:7])

# and another, this time with strings
shopping_list = ['milk', 'eggs', 'bread', 'cheesecake', 'coffee', 'rice']
print(shopping_list[2:5])


# deleting a slice
del shopping_list[2:5]
print(shopping_list)


# slicing works on strings too, incidentally.
# Here's an example of slicing a string with the same idea:
my_string = "Time for a coffee break."
print(my_string[11:17])



################################################################################################
# LIST OF LISTS

list_of_lists = []  # declare an empty list for a placeholder

list1 = ['a','b','c']
list2 = ['d','e','f']
list3 = ['g','h','i']

# append the lists to another list
list_of_lists.append(list1)
list_of_lists.append(list2)
list_of_lists.append(list3)

# access the elements using 2-dimensional indices
print(list_of_lists[0][2])  # prints c
print(list_of_lists[1][1])  # prints e
print(list_of_lists[0][0])  # prints a

