import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

web = requests.get('https://dantri.com.vn/')

content = BeautifulSoup(web.text)

highlight_area = content.find('div',{'class':'highlight-event'})

title_list = highlight_area.find_all('li')

# for title in title_list:
#     title_a_tag = title.find('a')
#     print(title_a_tag.text.strip())                     #title
#     print(title_a_tag['href'])                          #link

client = MongoClient('localhost',27017)
dantri_db = client.get_database('dantri')
title_collection = dantri_db.get_collection('title')


for title in title_list:
    title_a_tag = title.find('a')
    database = {
        'title': title_a_tag.text.strip(),
        'link': title_a_tag['href']
    }
   
    title_collection.insert_one(database)






