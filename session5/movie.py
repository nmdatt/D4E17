from pymongo import MongoClient

client = MongoClient('localhost', 27017)
movie_database = client.get_database('moviedatabase')
movie_collection = movie_database.get_collection('movies')

movie = movie_collection.find()

print('FIND MOVIE HAVE vote_average GREATER 7:')
# vote_avg = movie_collection.find({'vote_average':{'$gt': 7}})
for i in movie_collection.find({'results.vote_average':{'$gt': 7}}):
    print(i['title'])

