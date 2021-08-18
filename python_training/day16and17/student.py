import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/")
mydatabase=client('StudentDb')
collection_name=mydatabase['students']
result=collection_name.find()
print(result)
for i in result:
    print(i)