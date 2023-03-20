person = {'name':'Dat', 'yob' :00, 'job': 'sv'}         #key có thể đặt bằng kiểu dữ liệu int hoặc str(phân biệt hoa và thường)
print(person)
# C R U D

# READ
print(person['name'])
# READ ALL
name = person['name']           #gán name là key trong person để k phải khai báo person['name']
for key in person:
    print(key, end= ' ')        # in ra key của dictionary
    print(person[key])          # in ra value trong từng key của dictionary

#CREATE
person['height'] = 175 

#UPDATE
person['height'] = 180

#DELETE
del person['height']

if 'name' in person:            #check if key exist
    print('key existed')