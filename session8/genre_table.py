import pyexcel
import pymysql

client = pymysql.connect(
    host = 'localhost', 
    port = 3306,
    user = 'root',
    password = 'nmdat2000'
)

cursor = client.cursor()

data_source = pyexcel.get_records(file_name='vgsales.csv')
for row in data_source:
    genre_name = row['Genre']
    cursor.execute(f'''
        SELECT genre_id FROM games_db.genre
        WHERE name = "{genre_name}"
    ''')
    genre_found = cursor.fetchone()
    
    
    if not genre_found:
        cursor.execute(f'''
            INSERT INTO games_db.genre (
                name
            ) VALUES (
                "{genre_name}"
            )
        ''')
client.commit()
