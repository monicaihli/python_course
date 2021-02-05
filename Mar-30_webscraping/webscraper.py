from selenium import webdriver
from bs4 import BeautifulSoup

def main():
  url = "http://kitty.ninja/demo.html"
  driver = webdriver.Chrome(executable_path="./chromedriver") # create a driver object
  driver.get(url) # fetch the page source at the URL
  soup = BeautifulSoup(driver.page_source, "html.parser") # by not specifying another parser, we use python built in html parser

  for child in soup.children:
    print(child.text)  # will print ALL the children of the top-level document

  print('\n')

  # search by tag
  paragraphs = soup.find_all('p') # find every html element with a P tag. returns a ResultSet (like a list) of tags
  for p in paragraphs: # iterate over all the tags in the set of results
    print(p.text) # print the text of the current tag
    if p.b:  # if searching for a <b> tag inside the current <p> doesn't return None
      print("{} is in BOLD!".format(p.b)) # then print something

  print(soup.p) # print just the first p soup finds
if __name__ == "__main__":
  main()