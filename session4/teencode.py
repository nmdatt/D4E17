teencode = {'hc' : 'học',
        'ng': 'người',
        'pt': 'phát triển',
        'ns': 'nói',
        'lm': 'làm',
        'stt': 'số thứ tự'}
while True:
    print('*'*20)
    for key in teencode:
        print(key, end='        ')

    print()
    value = input('your code?: ')
    if value in teencode:
        print(f'trans: {teencode[value]}')
    else:
        print('not found, do you want to contribute this word? (Y/N):')
        answer = input()
        if answer == 'y' or answer =='Y':
            transport = input('enter your trans: ')
            teencode[value] = transport
        else:
            print('thank you')
            break
    

            