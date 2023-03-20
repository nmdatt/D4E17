
quizzes = [
    {
        'question': 'con chó có mấy chân?',
        'awnser': 3,
        'choices':[
            '2 chân',
            '3 chân',
            '5 chân',
            '4 chân'
        ]
    },
    {
        'question': 'con gà có mấy chân?',
        'awnser': 0,
        'choices':[
            '2 chân',
            '1 chân',
            '4 chân',
            '5 chân'
        ]
    },
    {
        'question': 'ô tô con có mấy bánh?',
        'awnser': 2,
        'choices':[
            '2 bánh',
            '6 bánh',
            '4 bánh',
            '5 bánh'
        ]
    }

]
count = 0
for quiz in quizzes:
    print(quiz['question'])
    for index in range(quiz['choices']):
        print(f"{index+1}. {quiz['choices'][index]}" , end='\t')
    print()
    awnser = int(input('your awnser (1,2,3,4): '))
    if awnser-1 == quiz['awnser']:
        print('bạn đã trả lời đúng!')
        count = count +1
    else:
        print('sai')