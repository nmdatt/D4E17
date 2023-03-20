import pyexcel
import pymysql

client = pymysql.connect(
    host = 'localhost', 
    port = 3306,
    user = 'root',
    password = 'nmdat2000'
)

cursor = client.cursor()

#Extract
data_source = pyexcel.get_records(file_name='vgsales.csv')
for row in data_source:
    platform_name = row['Platform']
    cursor.execute(f'''
        SELECT platform_id FROM games_db.platform
        WHERE name = "{platform_name}"
    ''')
    platform_found = cursor.fetchone()
    
    # Load
    if not platform_found:
        cursor.execute(f'''
            INSERT INTO games_db.platform (
                name
            ) VALUES (
                "{platform_name}"
            )
        ''')
client.commit()