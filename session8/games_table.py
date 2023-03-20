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
    # name_game = row['Name']
    # if not row['Year'] == 'N/A':
    #     year = row['Year']    
    
    platform_name = row['Platform']
    cursor.execute(f'''
                SELECT platform_id FROM games_db.platform
                WHERE name = "{platform_name}" 
    ''')
    platform_id = cursor.lastrowid
    print(platform_id)


    # cursor.execute(f'''
    #             INSERT INTO games_db.video_game (
    #                 name,
    #                 platform_id,
    #                 year,
    #                 genre_id,
    #                 publisher_id
    #             ) VALUES (
    #                 "{name_game}",

    #                 "{year}"


    #             )
    #         ''')