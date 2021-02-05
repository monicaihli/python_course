# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Review of .strip() for cleaning whitespace characters from a string
# Recall that strings are immutable variables!
# Apr 20, 2020
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



str = "This is a string with a newline\n"
print(id(str))

str.strip() # This works, but there is nowhere for the resulting stripped copy of the string to go
print(id(str)) # The ID of str hasn't changed. It hasn't been altered in any way, just copied.


str = str.strip() # Since strings are immutable, we have to create a new variable for the copy to go
print("str ID: ", id(str))
print("cleaned_str ID: ", id(str))
