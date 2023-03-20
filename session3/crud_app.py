items = ['T-shirt', 'Sweater', 'Hoodie']

command = input('Welcome to our shop, what do you want? (C,R,U,D): ')
if command=='C':
    items.append(input('Enter your new item: '))
elif command=='U':
    update_position = int(input('Enter position you want to change: ')) - 1
    if update_position < len(items):
        update_item=input('Enter new items:')
        items[update_position] = update_item
    else:
        print('item not found')
#D
elif command=='D':
    delete_position = int(input('Enter position you want to delete: ')) - 1
    if delete_position < len(items):
        items.pop(delete_position)
    else:
        print('item not found')

#R
for i in range(len(items)):
    print(f'{i+1}.{items[i]}')