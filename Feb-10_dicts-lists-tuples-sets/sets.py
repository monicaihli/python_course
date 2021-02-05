######################################################################################################
# File: sets.py
# Date: Feb 10, 2020
# Author: Monica Ihli monica@utk.ed
# Description: Brief demo for sets. Step through with debug mode in PyCharm!
# Documentation: https://docs.python.org/3.8/library/stdtypes.html#set-types-set-frozenset
######################################################################################################


print('########## CREATING SETS ##########')

set1 = {'Knox', 'Anderson', 'Roane', 'Sevier'}
# only unique values will make it into the set. Duplicates ignored:
set2 = {'Anderson', 'Knox', 'Anderson', 'Knox', 'Knox', 'Roane', 'Sevier','Anderson'}
print(set1)
print(set2)


# create sets using the set() function, which accepts a sequence:
letters_set = set('supercalifragilisticexpialidocious')
print(letters_set)
print('There are {} letters in the word supercalifragilisticexpialidocious.'.format(len(letters_set)))


# set from a list
my_list = ['cookies', 'cookies', 'cake', 'pie', 'cookies', 'cake']
set3 = set(my_list)
print(set3)



print('########## MODIFYING SETS ##########')


#set3.add('churros') # add to an existing set
print(set3)

print('WITH REMOVE():')
set3.remove('cookies') # attempts to remove value from set, but raises ERROR if not found
print(set3)

print('WITH DISCARD():')
set3.discard('pie') # attempts to remove value from set, but does not raise any error if not found
print(set3)

print('###################### SET OPERATIONS ####################')


A = {93,67,92,73,88,14,85,68,68,19,97,79,59,10,40,8,28,92,87,79}
B = {86,10,66,97,92,73,79,11,88,14,68,68,19,79,59,40,8,27,92,87}


# UNION
print('Set A contains {} items'.format(len(A)))
print('Set B contains {} items'.format(len(B)))
#C = A|B # other way to do the same thing, using an operator instead of .union()
C = A.union(B)
print('A union B has {} items'.format(len(C))) # check out that triple nesting!: len() then .format() then print()


# INTERSECTION
C = A.intersection(B)
print('Items in both A and B include {}'.format(C))


# DIFFERENCE
C1 = A.difference(B)
print('Items in A, but not B, include: {}'.format(C1))
C2 = B.difference(A)
print('Items in B, but not A, include: {}'.format(C2))

# SYMMETRIC DIFFERENCE
C = A.symmetric_difference(B)
print('Unique items in A or B, but not in both, include: {}'.format(C))


