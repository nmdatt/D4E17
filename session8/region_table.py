
import pymysql

client = pymysql.connect(
    host = 'localhost', 
    port = 3306,
    user = 'root',
    password = 'nmdat2000'
)

cursor = client.cursor()
list_region = [
    'NA_Sales',
    'EU_Sales',
    'JP_Sales',
    'Other_Sales',
    'Global_Sales'
]

for i in list_region:
    cursor.execute(f'''
            INSERT INTO games_db.region (
                name
            ) VALUES (
                "{i}"
            )
        ''')

client.commit()
