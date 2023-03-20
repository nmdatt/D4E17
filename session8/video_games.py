import pymysql 

client = pymysql.connect(
    host = 'localhost', 
    port = 3306,
    user = 'root',
    password = 'nmdat2000'
)

cursor = client.cursor()


# cursor.execute('''
#     CREATE TABLE games_db.platform(
#         platform_id int(11) PRIMARY KEY AUTO_INCREMENT ,
#         name varchar(255)
#     )
# ''')

# cursor.execute('''
#     CREATE TABLE games_db.genre(
#         genre_id int(11) PRIMARY KEY AUTO_INCREMENT ,
#         name varchar(255)
#     )
# ''')

# # cursor.execute('''
# #     CREATE TABLE games_db.region(
# #         region_id int(11) PRIMARY KEY AUTO_INCREMENT ,
# #         name varchar(255)
# #     )
# # ''')

# cursor.execute('''
#     CREATE TABLE games_db.publisher(
#         publisher_id int(11) PRIMARY KEY AUTO_INCREMENT ,
#         name varchar(45)
#     )
# ''')

# cursor.execute('''
#     CREATE TABLE games_db.video_game(
#         id int(11) PRIMARY KEY AUTO_INCREMENT ,
#         name varchar(45),
#         platform_id int(11),
#         year int(10),
#         genre_id int(11),
#         publisher_id int(11),
#         FOREIGN KEY (platform_id) REFERENCES games_db.platform(platform_id),
#         FOREIGN KEY (genre_id) REFERENCES games_db.genre(genre_id),
#         FOREIGN KEY (publisher_id) REFERENCES games_db.publisher(publisher_id)
#     )
# ''')

cursor.execute('''
    CREATE TABLE games_db.region(
        region_id int(11) PRIMARY KEY AUTO_INCREMENT ,
        name varchar(255)
    )
''')

cursor.execute('''
    CREATE TABLE games_db.video_games_sales(
        video_game_id INT(11),
        region_id INT(11),
        sales DECIMAL(9,0),
        FOREIGN KEY (video_game_id) REFERENCES games_db.video_game (id),
        FOREIGN KEY (region_id) REFERENCES games_db.region (region_id),
        PRIMARY KEY (video_game_id, region_id)
    )
''')

client.commit()
