# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Review of loading xml from strings in memory versus file on disk.
# Recall that strings are immutable variables!
# Apr 20, 2020
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import xml.etree.ElementTree as ET
import requests

tree = ET.parse('input.xml')  # loading xml from a file permanently stored on disk (ROM)
root1 = tree.getroot()
parents = root1.findall("parent") # search for any tag named parent and store the elements in a list
for parent in parents: # for every parent element in that list
  children = parent.findall("child") # look for all children of that parent, and store that in a new list
  for child in children: # for every child in the list
    print(child.text)

print('\n Using Requests:\n')
url = "http://kitty.ninja/input.xml"
r = requests.get(url)
root2 = ET.fromstring(r.text)
parents2 = root2.findall("parent") # search for any tag named parent and store the elements in a list
for parent2 in parents2: # for every parent element in that list
  children2 = parent2.findall("child") # look for all children of that parent, and store that in a new list
  for child2 in children2: # for every child in the list
    print(child2.text)

# handling no result returned from .find(), remember that .findall() by contrast returns empty list
if child2.find("bestfriend") != None:
  bestie = child2.find("bestfriend").text
else:
 bestie = "Not found"
 print(bestie)



