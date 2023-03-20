from pymongo import MongoClient
client = MongoClient('localhost', 27017)

quizzes_database = client.get_database('question')

quizzes_collection = quizzes_database.get_collection('quizzes')

quizzes = quizzes_collection.find()
total_quizzes = quizzes_collection.count_documents({})

# for quiz in data_quizz:
#     quiz['choices'] = quiz['choices'].split(',')
#     quiz['choices'].pop(-1)
# print(data_quizz[1]['choices'])

count = 0 
for quiz in quizzes:
    print(quiz['question'])
    for i in range(len(quiz['choices'])):
        print(f'{i+1}: {quiz["choices"][i]}')
    use_choice = int(input('Enter correct position: ')) - 1
    if use_choice == quiz['awnser']:
        print('correct!!')
        count = count + 1
    else:
        print('wrong!!')

score = (count * 100) / total_quizzes
print(f'your score is {score}%')