from pymongo import MongoClient

client = MongoClient('localhost', 27017)

shoppee_database = client.get_database('DatNguyen')

product_collection = shoppee_database.get_collection('products')

# data = list(product_collection.find()) #load all data into ram #READ
data = product_collection.find()        #get on data at time
print(data[0]['name'])
# for d in data:
#     print(d)

# one_data = product_collection.find_one(
#     {'name': 'sanpham2','category':'dsp_3'})        #find record have name is sanpham2 
# print('only one', one_data)

# # insert_data= {
# #     'name': 'sanpham3',
# #     'category': 'dsp2',
# #     'supplier': 'ncc4'
# # }
# # product_collection.insert_one(insert_data)  #CREATE

# # product_collection.insert_many([{},{},{}])        #nếu dùng insert_one thì phải dùng vòng for còn insert_many thì k cần

# # query = {'name' : 'sanpham4'}
# # update = {'$set' :      #$set / $push va $pull 
# #         {
# #             'name' : 'sanpham4',
# #             'price': 40
# #     } 
# # }
# # product_collection.update_one(query,update)

# query = {'price': 40}
# product_collection.delete_one(query)