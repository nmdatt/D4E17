list_shop=['sweater', 'pant', 'hoodie']
choose= input('Welcome to our shop, what do you want? (C R U D):')

if choose=='R':
    print('Our item:')
    for i in range(len(list_shop)):
        print(i+1,'.',list_shop[i])
elif choose=='C':
    print('create new item:')
    list_shop.append(input())
    for i in range(len(list_shop)):
        print(i+1,'.',list_shop[i])
elif choose=='U':
    index=input('choose number you want to update:')
    new_item=input('type:')
    list_shop[int(index)+1]=new_item
else:
    print('a')