from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = requests.get(url)
soup=BeautifulSoup(page.text,"html.parser")
table_1 = soup.find("table")
print(table_1)

table_row= table_1.find_all("tr")
print(table_row)
temp_list=[]
for tr in table_row:
    td= tr.find_all("td")
    temp_list.append(td)
print(temp_list)


