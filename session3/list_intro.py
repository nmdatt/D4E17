quanao=['a','b','c', 1,3]
print(quanao)
print(quanao[2])

quanao.append('d')   #create
print(quanao)

leng_list_quanao=len(quanao)        #index of list quanao
for i in range(leng_list_quanao):
    print('item', quanao[i])

for item in quanao:
    print(item)
index = quanao.index('a')   #print vi tri trong list
print('vi tri cua \'a\' la:', index) #print vi tri trong list

quanao[index]= 't'  #update

quanao.pop(1)   #delete b in list quanao
remove_item = quanao.pop(3)     #save before delete '1' in list quanao

print('check in list', 'a' in quanao)   #kiem tra xem a co ton tai trong list k 