from pymongo import MongoClient
from bson import ObjectId

client = MongoClient('localhost', 27017)

quizzes_database = client.get_database('question')

quizzes_collection = quizzes_database.get_collection('quizzes')

quizzes = [
    {
        'question': 'Con cò có mấy chân?',
        'awnser': 3,
        'choices': [
            '2 chân',
            '3 chân',
            '1 chân',
            '4 chân'
        ]
    },
    {
        'question': 'Con mèo có mấy chân?',
        'awnser': 2,
        'choices': [
            '1 chân',
            '3 chân',
            '2 chân',
            '4 chân'
        ]
    }
]
quizzes_collection.insert_many(quizzes)

query = {'_id' : ObjectId("5fae8ab43cd9935b748a9c94")}
push = {'$push' : 
        {
            'choices' : '5 tay'            
    } 
}
quizzes_collection.update_one(query,push)
