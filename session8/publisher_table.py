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
    publisher_name = row['Publisher']
    cursor.execute(f'''
        SELECT publisher_id FROM games_db.publisher
        WHERE name = "{publisher_name}"
    ''')
    publisher_found = cursor.fetchone()
    
    
    if not publisher_found:
        cursor.execute(f'''
            INSERT INTO games_db.publisher (
                name
            ) VALUES (
                "{publisher_name}"
            )
        ''')
client.commit()
