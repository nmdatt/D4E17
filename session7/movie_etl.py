import pymysql
from pymongo import MongoClient

mongo_client = MongoClient('10.1.9.62', 27017)

mysql_client = pymysql.connect(
    host = 'localhost', 
    port = 3306,
    user = 'root',
    password = 'nmdat2000'
)

cursor = mysql_client.cursor()

movie_database = mongo_client.get_database('mongo_practice')
movie_collection = movie_database.get_collection('moives')

movie_data = movie_collection.find({'actor': {'$exists': True}})

for movie in movie_data:
    cursor.execute('''
        INSERT 

    ''')