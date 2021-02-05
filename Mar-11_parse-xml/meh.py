import xml.etree.ElementTree as ET
tree = ET.parse("demo1.xml")
root = tree.getroot()

# notice how the inner value of the attribute in the search is inside single quotes
this_cookie = root.find(".//cookie[@sellby='03/15/2020']")
print("Cookie batch with sell by date of 03/15/2020: " + this_cookie.text)
