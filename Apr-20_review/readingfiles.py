# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Review of read vs readline vs readlines
# Apr 20, 2020
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# reads entire file into a single string
with open("input.txt", "r") as f:
  input1 = f.read()

# readline reads a single line of the file, as divided by a newline, into a string
# honestly even though this example technically works, it's a terrible idea. There are better ways to iterate.
with open("input.txt", "r") as f:
  while True:
    line = f.readline()
    if not line:
      break
    input2 = line
    print(input2)

# reads the entire file into a list, with each newline separating items in the list.
with open("input.txt", "r") as f:
  input3 = f.readlines()

# iterate over lines without bothering with an intermediary step of storing in a variable.
with open("input.txt") as f:
  for line in f:
    input4 = line


