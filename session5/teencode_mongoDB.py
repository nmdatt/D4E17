from pymongo import MongoClient

client = MongoClient('localhost', 27017)

teencode_database = client.get_database('teencodedatabase')

teencode_collection = teencode_database.get_collection('teencode')

teencode = {'hc' : 'học',
        'ng': 'người',
        'pt': 'phát triển',
        'ns': 'nói',
        'lm': 'làm',
        'stt': 'số thứ tự'}

teencode_collection.insert_one(teencode)