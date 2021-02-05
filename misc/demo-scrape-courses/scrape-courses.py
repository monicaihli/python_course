from selenium import webdriver
from bs4 import Tag, NavigableString, BeautifulSoup
import time
import pandas as pd

def main():
  url = "https://catalog.utk.edu/content.php?catoid=27&navoid=3520"
  driver = webdriver.Chrome(executable_path="./chromedriver")
  driver.get(url)  # fetch the page source at the URL
  time.sleep(1)
  soup = BeautifulSoup(driver.page_source)
  #<a> xpaths: /html/body/table/tbody/tr[3]/td[1]/table/tbody/tr[2]/td[1]/table/tbody/tr/td/table[2]/tbody/tr[3]/td[2]/a
  results = soup.find("td", class_="block_content").find_all('td', {'class': 'width'}) # 100 results per page by default

  course_data = [] # create empty list to hold results; it will become a list of lists.

  for result in results:
    try:
      print('*'*60)
      a_tag = result.a
      link = 'https://catalog.utk.edu/' + a_tag['href']
      print(link)
      course = a_tag.text
      print(course)
      driver.get(link)
      time.sleep(.3)

      soup = BeautifulSoup(driver.page_source)
      td_tag = soup.find('td', {'class': 'block_content', 'colspan': '2'})
      for index, content in enumerate(td_tag.contents):
        print(index, content)
      if td_tag != None:
        if isinstance(td_tag.contents[10], NavigableString):
          print("\t" + td_tag.contents[10])
        elif isinstance(td_tag.contents[10], Tag) and isinstance(td_tag.contents[12], Tag): # seems to indicate statement of cross-listing
          print("\t" + td_tag.contents[10].text + " " + td_tag.contents[12].text)
        elif isinstance(td_tag.contents[10], Tag): # if the both as tags hasn't triggered then check the [10] only as tag
          print("\t"+td_tag.contents[10].text)
        else:
          print(" ######### UNKNOWN OUTCOME ########### ")
        #print(type(td_tag.contents[10]))
        #if "Cross-listed:" in td_tag.contents[10]:
        #  print("\t" + td_tag.contents[10] + " " + td_tag.contents[11])
        #else:
        #  print("\t" + td_tag.contents[10])


        #for content in td_tag.contents:
        #  print(content)
        #desc = td_tag.text
        #print(desc)
      else:
        desc = "N/A"
      #course_data.append([link,course,desc])
    except Exception as e:
      print(e)

#  df = pd.DataFrame(course_data)
#  df.to_csv(course_data, "courses.csv")






if __name__ == "__main__":
  main()