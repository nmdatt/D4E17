import pymysql
from pymongo import MongoClient

client = pymysql.connect(
    host = 'localhost', 
    port = 3306,
    user = 'root',
    password = 'nmdat2000'
)


mongodb_client = MongoClient('10.1.9.62', 27017)

kpop_database = mongodb_client.get_database('kpopdatabase1')

idol_collection = kpop_database.get_collection('kpop_idol')


cursor = client.cursor()

# cursor.execute('CREATE DATABASE first_mysql_db')

cursor.execute('''
    CREATE TABLE first_mysql_db.movie(
        id int(11) PRIMARY KEY AUTO_INCREMENT,
        profile varchar(255),
        stage_name varchar(200),
        full_name varchar(200),
        korea_name varchar(200)
    )
''')

# cursor.execute('''
#     INSERT INTO first_mysql_db.kpop_idol(
#         profile, 
#         stage_name, 
#         full_name, 
#         korea_name
#     ) VALUES (
#         "https://dbkpop.com/2020/09/27/november-2020-k-pop-comebacks-and-debuts",
#         "psy",
#         "psyyyy",
#         "khong biet tieng han"
#     )
# ''')

# client.commit()

data = idol_collection.find(
    {
        '_id':{'$exists': True},
        'thumbnail':{'$exists':True},
        'stage_name':{'$exists':True},
        'full_name':{'$exists':True},
        'korean_name':{'$exists':True},
        'profile':{'$exists':True}}
)
for d in data:
    cursor.execute(f'''
    INSERT INTO first_mysql_db.kpop_idol(
        profile, 
        stage_name, 
        full_name, 
        korea_name
    ) VALUES (
        "{d['thumbnail']}",
        "{d['stage_name']}",
        "{d['full_name']}",
        "{d['korean_name']}"
    )
''')
client.commit()  
    