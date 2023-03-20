import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

web = requests.get('https://dbkpop.com/db/all-k-pop-idols')
content = BeautifulSoup(web.text)
highlight_area = content.find('div', {'class':'sidebar widget-area'})
top_posts = highlight_area.find_all('li')

client = MongoClient('localhost',27017)
kpop_db = client.get_database('kpop')
top_posts_collection = kpop_db.get_collection('list')

for posts in top_posts:
    post_a_tag = posts.find('a')
    data = {
        'post' : post_a_tag.text.strip(),
        'link' : post_a_tag['href']
    }
    top_posts_collection.insert_one(data)