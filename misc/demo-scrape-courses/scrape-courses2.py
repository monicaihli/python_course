from selenium import webdriver
from bs4 import Tag, NavigableString, BeautifulSoup
import time
import csv
import random


def main():

  base_url = 'https://catalog.utk.edu/content.php?catoid=27&navoid=3520'
  start_query = '&filter[item_type]=3&filter[only_active]=1&filter[3]=1&filter[cpage]='
  end_query = '#acalog_template_course_filter'

  course_data = [] # store all data

  for page in range(42):
    print("Now capturing page {}".format(page+1))
    driver = webdriver.Chrome(executable_path="./chromedriver")
    driver.get(base_url + start_query + str(page+1) + end_query)
    time.sleep(1)
    soup = BeautifulSoup(driver.page_source)
    # <a> xpaths: /html/body/table/tbody/tr[3]/td[1]/table/tbody/tr[2]/td[1]/table/tbody/tr/td/table[2]/tbody/tr[3]/td[2]/a
    results = soup.find("td", class_="block_content").find_all('td',{'class': 'width'})  # 100 results per page by default
    for result in results:
      try:
        print('*' * 60)
        a_tag = result.a
        link = 'https://catalog.utk.edu/' + a_tag['href']
        print(link)
        course = a_tag.text
        print(course)
        driver.get(link)
        time.sleep(random.uniform(.1,3))

        soup = BeautifulSoup(driver.page_source)
        td_tag = soup.find('td', {'class': 'block_content', 'colspan': '2'})
        if td_tag != None:
          if isinstance(td_tag.contents[10], NavigableString):
            #print("\t" + td_tag.contents[10])
            desc = td_tag.contents[10]
          elif isinstance(td_tag.contents[10], Tag) and isinstance(td_tag.contents[12],Tag): # cross-listing
            #print("\t" + td_tag.contents[10].text + " " + td_tag.contents[12].text)
            desc = td_tag.contents[10].text + " " + td_tag.contents[12].text
          elif isinstance(td_tag.contents[10],Tag):  # if the both as tags hasn't triggered then check the [10] only as tag
            #print("\t" + td_tag.contents[10].text)
            desc = td_tag.contents[10].text
          else:
            print(" ######### UNKNOWN OUTCOME ########### ")
            desc = "N/A"
        else:
          desc = "N/A"
        course_data.append([link, course, desc])

      except Exception as e:
        print(e)

  with open("output.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(course_data)



if __name__ == "__main__":
  main()